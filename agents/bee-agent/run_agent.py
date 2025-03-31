import asyncio
import sys
import os

from beeai_framework import UnconstrainedMemory
from beeai_framework.agents.tool_calling.agent import ToolCallingAgent
from beeai_framework.tools.weather.openmeteo import OpenMeteoTool
from beeai_framework.tools.search.duckduckgo import DuckDuckGoSearchTool
from beeai_framework.adapters.openai.backend.chat import OpenAIChatModel


async def run_agent(prompt: str) -> str:
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model = "meta-llama/llama-3-1-70b-instruct"
    settings = {
        "extra_headers": { "RITS_API_KEY": api_key},
        "api_key": api_key,
        "base_url": f"{base_url}/v1",
    }

    llm = OpenAIChatModel(model_id=model, settings=settings)
    agent = ToolCallingAgent(llm=llm, tools=[DuckDuckGoSearchTool(), OpenMeteoTool()], memory=UnconstrainedMemory())

    response = await agent.run(prompt)
    print("Agent 🤖 : ", response.result.text)

    return response.result.text

if __name__ == "__main__":
    prompt = sys.argv[1]
    asyncio.run(run_agent(prompt))
