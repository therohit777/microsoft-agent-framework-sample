
from agent_framework import (
    Executor,
    WorkflowContext,
    handler,
)

from app.prompts.prompts import support_agent_prompt
from app.utils.azure_openai_agent import run_agent

class SupportAgent(Executor):
    @handler
    async def execute_support(self, message: str, ctx: WorkflowContext[str])-> None:
        print(f"Agent handling: {message}")
        response = await run_agent("support_agent", support_agent_prompt,message)
        await ctx.send_message({"response": response})