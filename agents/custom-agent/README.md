# Running a custom agent

Go from a python script to a running container

## (Prereq) Build the base image

```bash
cd bees-in-a-pod/agents/base-image
docker build -t base-image .
```

> Note: eventually, this should be hosted on a container registry somewhere

## Implement the `run_agent` function

Create a file called `run_agent.py` and implement the following function:

```python
def run_agent(prompt: str) -> str:
```

If you have any additional dependencies, add them to a `requirements.txt` file.

## Build the custom image

```bash
docker build -t custom-agent .
```

> Note: eventually, this should be hosted on a container registry somewhere

## Deploy

```bash
kubectl apply -f deploy.yaml
```

## Run

```bash
kubectl port-forward svc/custom-agent 8080 &
curl -X POST -H "Content-Type: application/json" -d '{"prompt":"hello"}' localhost:8080
```

> Note: in production, you'd want to use an ingress rather than port-forwarding
