
from agent_framework import (
    Executor,
    WorkflowContext,
    handler,
)
from app.tools.websearch_tool import web_search_tool
from app.utils.azure_openai_agent import run_agent
from app.prompts.prompts import websearch_agent_prompt

class WebsearchAgent(Executor):
    @handler
    async def execute_websearch(self, message: str, ctx: WorkflowContext[str])-> None:
        print(f"Agent handling: {message}")
        user_query = await ctx.get_shared_state("message")
        response = await run_agent("websearch_agent", websearch_agent_prompt,user_query,[web_search_tool])
        await ctx.send_message({"response": response})


