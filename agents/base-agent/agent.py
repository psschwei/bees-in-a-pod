import os
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from run_agent import run_agent

app = FastAPI()

class ACP(BaseModel):
    prompt: str
    response: Optional[str] = ""

@app.post("/")
async def main(acp: ACP):
    prompt = acp.prompt
    acp.response = await run_agent(prompt)
    return acp

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="warning")
