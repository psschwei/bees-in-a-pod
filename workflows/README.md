# Running Workflows

Running a workflow of containerized agents using Argo

## Prereqs

* Kubernetes cluster
* The sample Bee and Crew agent images built

## Getting started

### Install Argo workflows

For local testing, we'll use a quick-start install (production deploys should use the full version):

```bash
kubectl create namespace argo
kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/v3.6.5/quick-start-minimal.yaml
```

You'll also need to add the `argo` service account to the `executor` rolebinding.

```bash
kubectl edit rolebinding -n argo executor-default -o yaml
```

Final result should look something like this (last two lines are what need to be added):

```yaml
piVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  annotations:
  name: executor-default
  namespace: argo
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: executor
subjects:
- kind: ServiceAccount
  name: default
- kind: ServiceAccount
  name: argo
```


### Create a workflow



### Triggering the workflow remotely

https://argoproj.github.io/argo-events/sensors/triggers/argo-workflow/
