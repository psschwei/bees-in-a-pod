import asyncio
import os
from crewai import Crew, LLM, Agent, Task, Process

async def run_agent(prompt: str) -> str:
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
        description = prompt,
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
    return crewoutput.raw

if __name__ == "__main__":
    asyncio.run(run_agent("How many albums did Bob Dylan release before his motorcycle accident?"))
