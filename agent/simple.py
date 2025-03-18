import asyncio
import os
import sys
import traceback

from beeai_framework import UnconstrainedMemory
from beeai_framework.agents.tool_calling.agent import ToolCallingAgent
from beeai_framework.errors import FrameworkError
from beeai_framework.tools.weather.openmeteo import OpenMeteoTool
from beeai_framework.adapters.openai.backend.chat import OpenAIChatModel


def print_event(event_data, event_meta) -> None:
    """Process agent events and log appropriately"""
    if event_meta.name == "error":
        error = event_data.error if hasattr(event_data, "error") else event_data
        print("Agent 🤖 : ", FrameworkError.ensure(error).explain())
    elif event_meta.name == "retry":
        print("Agent 🤖 : ", "retrying the action...")
    elif event_meta.name == "update":
        print(f"Agent({event_data.update.key}) 🤖 : ", event_data.update.parsed_value)


async def main() -> None:
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model = "meta-llama/llama-3-1-70b-instruct"
    settings = {
        "extra_headers": { "RITS_API_KEY": api_key},
        "api_key": api_key,
        "base_url": f"{base_url}/v1",
    }

    llm = OpenAIChatModel(model_id=model, settings=settings)
    agent = ToolCallingAgent(llm=llm, tools=[OpenMeteoTool()], memory=UnconstrainedMemory())

    prompt = "What's the current weather in New York?"
    response = await agent.run(prompt).on("*", print_event)
    print("Agent 🤖 : ", response.result.text)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except FrameworkError as e:
        traceback.print_exc()
        sys.exit(e.explain())
