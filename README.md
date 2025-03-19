# Bees in a Pod

Run AI agents in Kubernetes

## Prereqs

* A Kubernetes cluster. We'll use [kind](https://kind.sigs.k8s.io/)
* The [`kubectl` CLI](https://kubectl.docs.kubernetes.io/)
* Access to an OpenAI-compatible LLM provider

> Note: Using Kind+Ollama may require some extra config

## Usage

* Edit `deploy/deploy.yaml` to include proper values for `API_KEY` and `BASE_URL`
* (optional) Edit `deploy/deploy.yaml` with a new `PROMPT` for the agent
* Build the `agent` image: `docker build -t agent .` from the `agent/` directory
* Load container to Kubernetes: `kind load docker-image agent:latest`
* Deploy to kubernetes: `kubectl apply -f deploy/`
* Expose the agent: `kubectl port-forward svc/bee-agent 8080`
* Send a query to the agent: `curl -X POST localhost:8080`
* Stream logs: `kubectl logs deploy/bee-agent -f`

## To-Do

* Add sidecar for standardizing agent I/O
* Add an example with another agent framework
* Create a function signature for agents (to standardize output, etc.)
* ~~Use deployments instead of jobs~~
* Simple build process for making containers from agents
* Orchestrate an agentic workflow using Argo or Tekton
* ...
* ...
