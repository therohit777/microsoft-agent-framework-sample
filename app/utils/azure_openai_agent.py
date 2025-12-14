from dotenv import load_dotenv
load_dotenv()
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from typing import List, Optional
import asyncio
import os

AZURE_OPENAI_ENDPOINT=os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION=os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_API_KEY=os.getenv("AZURE_OPENAI_API_KEY")

client = AzureOpenAIChatClient(
        deployment_name=AZURE_OPENAI_CHAT_DEPLOYMENT_NAME,
        endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=AZURE_OPENAI_API_VERSION,
        credential=AzureCliCredential()
)

async def run_agent(
    agent_name: str,
    instructions: str,
    message: str,
    tools: Optional[List[object]] = None
):
    tools = tools if tools is not None else []

    agent = client.create_agent(
        name=agent_name,
        instructions=instructions,
        tools=tools,         
        enable_tracing=False
    )
    result = await agent.run(message)
    return result.text

    
    