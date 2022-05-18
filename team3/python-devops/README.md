# PYTHON DEVOPS
![python version](https://img.shields.io/pypi/pyversions/bandit.svg)

## 一、 CI检查
 ### 1. 代码规范

```
 pylint src/ --reports=y > ./tmp/pylint-report.txt
```

### 2. 单元测试并生成allure报告
```
pytest src/tests.py --alluredir=./tmp/allure-reports 

allure generate ./tmp/allure-reports -o ./tmp/allure-report --clean 
```


### 3. 覆盖率生成
```
coverage run -m pytest src/tests.py

coverage xml -o ./tmp/coverage.xml
```

### 4. 质量门径
```
# 检查是否有安全漏洞
bandit -r ./src -f html -o ./tmp/bandit.html
# 检查依赖是否符合规定
python package_checker
```

### 5. sonar
```
sonar-scanner -Dproject.settings=./sonar-project.properties
```











