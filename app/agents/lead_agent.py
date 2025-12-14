from agent_framework import (
    Executor,
    WorkflowContext,
    handler,
)
from app.utils.azure_openai_agent import run_agent
from app.prompts.prompts import lead_agent_prompt

class LeadAgent(Executor):
    @handler
    async def execute_lead(self, message: str, ctx: WorkflowContext[str]):
        print(f"Agent handling: {message}")
        response = await run_agent("lead_agent", lead_agent_prompt,message) 
        await ctx.send_message({"response": response})

