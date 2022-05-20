"""devops demo"""
import time
import uuid

from flask import Flask, Response, request, jsonify, g
from loguru import logger
import prometheus_client
from prometheus_client import Counter, Summary
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.contrib.opentracing import Tracer
from playhouse.pool import PooledMySQLDatabase
import redis


from utils import get_output, setup_logger
from config import setting

db = PooledMySQLDatabase(
    setting.mysql_db, user=setting.mysql_uname, password=setting.mysql_pwd,
    host=setting.mysql_host, charset='utf8mb4',
    max_connections=300, stale_timeout=300
)

redis_conn = redis.Redis(connection_pool=redis.ConnectionPool(
    host=setting.redis_host, port='6379'))

setup_logger()

app = Flask(__name__)
app.logger.disabled = True

requests_total = Counter("request_count", "Total request count of the host")
invoke_summary = Summary('invoke_duration', 'invoke latency', ['service'])
request_latency_summery = Summary('request_latency', 'request latency', ['path', 'status_code'])

app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': f'python-{setting.flask_env}',
    'SECRET_TOKEN': setting.apm_token,
    'SERVER_URL': setting.apm_url,
    'ENVIRONMENT': setting.flask_env
}

apm = ElasticAPM(app)
tracer = Tracer(client_instance=apm.client)


@app.route('/api/a')
def demo():
    """demo url"""
    # just for opentracing
    item = invoke_summary.labels(service='mysql')
    start = time.time()
    try:
        db.execute_sql("select 1;")
    except:
        pass
    item.observe(time.time() - start)

    item = invoke_summary.labels(service='redis')
    redis_conn.get("test")
    item.observe(time.time() - start)
    return jsonify({"data": get_output()})


@app.route('/api/double/')
def double():
    """demo url"""

    item = invoke_summary.labels(service='mysql')
    start = time.time()
    db.execute_sql("select 1;")
    item.observe(time.time() - start)

    item = invoke_summary.labels(service='redis')
    redis_conn.get("test")
    item.observe(time.time() - start)

    num = int(request.values.get('num', 0))
    return jsonify({"data": int(num) * 2})


@app.route('/metrics')
def metrics():
    from prometheus_client.registry import CollectorRegistry
    r = CollectorRegistry()
    r.register(requests_total)
    r.register(invoke_summary)
    r.register(request_latency_summery)
    return Response(prometheus_client.generate_latest(r), mimetype="text/plain")


@app.route('/heath')
def heath():
    return Response('ok')

@app.errorhandler(Exception)
def handle_exception(e):
    request_id = ""
    for cross_header, value in g.cross_headers:
        if cross_header == "Http-X-Requestid":
            request_id = value
    logger.bind(request_id=request_id, service_name="python").exception(e)
    return 'interval error'


@app.before_request
def before_request():
    # db.connect()
    apm.request_started(app)
    cross_headers = []
    request_id = ""
    for header, value in request.headers:
        if header.startswith("Http-X"):
            cross_headers.append((header, value))
        if header == "Http-X-Requestid":
            request_id = value
    if not request_id:
        cross_headers.append(('Http-X-Requestid', uuid.uuid4().hex))
    g.cross_headers = cross_headers
    g.api_request_time = time.time()


@app.after_request
def after_request(resp):
    requests_total.inc()

    item = request_latency_summery.labels(path=request.path, status_code=resp.status_code)
    item.observe(time.time() - g.api_request_time)

    request_id = ""
    for cross_header, value in g.cross_headers:
        if cross_header == "Http-X-Requestid":
            request_id = value
        resp.headers[cross_header] = value
    if 'heath' in request.path or 'metrics' in request.path:
        pass
    else:
        logger.bind(ip=request.remote_addr, path=request.path, status_code=resp.status_code, request_id=request_id,
                    service_name="python") \
            .info(f'{request.method} {request.path} {request.environ.get("SERVER_PROTOCOL") } - {resp.status_code}')
    for cross_header, value in g.cross_headers:
        resp.headers[cross_header] = value
    apm.request_finished(app, resp)
    return resp


if __name__ == '__main__':
    logger.info(f'server started on {setting.flask_env} - {setting.port}')
    app.run(host='0.0.0.0', port=setting.port)



