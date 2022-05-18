?> In this task we will run a job in k8s.

## Manifest

A one time job can be coded like this:

```yaml
# job.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    spec:
      containers:
        - name: pi
          image: perl
          command: ['perl', '-Mbignum=bpi', '-wle', 'print bpi(2000)']
      restartPolicy: Never
  backoffLimit: 4
```

Create the job.

```bash
k create -f job.yaml
```

Inspect the job result.

```
$ k logs pi-22fd7
3.14159265358979323846264338327950288...
```

However, we usually want to perform the job regularly, based on a schedule.

```yaml
# job-cron.yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: '*/1 * * * *'
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: hello
              image: busybox
              imagePullPolicy: IfNotPresent
              command:
                - /bin/sh
                - -c
                - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure
```

## Command

```bash
k create -f job-cron.yaml
k get cj
k get jobs
```

## Shortcut

```
kubectl create cronjob hello --image=busybox  --schedule="*/1 * * * *" -- echo "Hello World"
```
