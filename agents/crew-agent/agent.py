import os
from typing import Optional

from crewai import Crew, LLM, Agent, Task, Process
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class ACP(BaseModel):
    prompt: str
    response: Optional[str] = ""

@app.post("/")
async def main(acp: ACP):
    # Define your custom LLM configuration
    my_llm = LLM(
        base_url = f"{os.getenv('BASE_URL')}/v1",
        model = "openai/meta-llama/llama-3-1-70b-instruct",
        api_key = os.getenv("API_KEY"),
        extra_headers = {"RITS_API_KEY": os.getenv("API_KEY")}
    )

    # Create a researcher agent
    researcher = Agent(
      role='Senior Researcher',
      goal='Discover groundbreaking technologies',
      verbose=True,
      llm=my_llm,
      backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.'
    )

    # Task for the researcher
    research_task = Task(
        description = acp.prompt,
        expected_output = 'A summary of the results',
        agent = researcher
    )

    # Instantiate your crew
    tech_crew = Crew(
      agents=[researcher],
      tasks=[research_task],
      process=Process.sequential
    )

    # Begin the task execution
    crewoutput = tech_crew.kickoff()
    acp.response = crewoutput.raw
    return acp

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="warning")
