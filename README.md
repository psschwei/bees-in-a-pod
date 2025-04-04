# Bees in a Pod

Run AI agents in Kubernetes.

See also the [hive cli](https://github.com/psschwei/hive-cli), a command line tool that simplifies the build/deploy process even more.

## Prereqs

* A Kubernetes cluster. We'll assume [kind](https://kind.sigs.k8s.io/)
* The [`kubectl` CLI](https://kubectl.docs.kubernetes.io/)
* Access to an OpenAI-compatible LLM provider

> Note: Using Kind+Ollama may require some extra config

## Usage

* Edit `deploy/deploy.yaml` to include proper values for `API_KEY` and `BASE_URL`
* Build your own [custom agent](agents/custom-agent/README.md)
* Run a [workflow](workflows/README.md)

## Example Agents

* [Using the BeeAI Framework](agents/bee-agent)
* [Using CrewAI](agents/crew-agent)


## To-Do

* ~~Add an example with another agent framework~~
* ~~Create a function signature for agents (to standardize output, etc.)~~
* ~~Use deployments instead of jobs~~
* ~~Simple build process for making containers from agents~~
* ~~Update agents to use custom build process~~
* ~~Orchestrate a multi-agent workflow using Argo or Tekton~~
* ...
* ...
