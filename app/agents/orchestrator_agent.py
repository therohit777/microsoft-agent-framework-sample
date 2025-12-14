from agent_framework import (
    Executor,
    WorkflowContext,
    handler,
)

from app.prompts.prompts import orchestrator_prompt
from app.utils.azure_openai_agent import run_agent

class OrchestratorAgent(Executor):
    """Main orchestrator that decides which agent to route to"""

    @handler
    async def execute_orchestrator(self, message: str, ctx: WorkflowContext[str]) -> None:
        routing_decision = await self.analyze_and_decide(message)
        await ctx.set_shared_state("message", message)
        await ctx.send_message(routing_decision)

    
    async def analyze_and_decide(self, message):
        """Analyze input and return routing decision using Azure OpenAI agent"""
        print(f"Orchestrator Agent analyzing: {message}")
        response = await run_agent("orchestrator_agent", orchestrator_prompt,message)
        routing_decision = response
        return routing_decision