from agent_framework import (
    Executor,
    WorkflowContext,
    handler,
)

class ReportGenerateAgent(Executor):
    @handler
    async def execute_report(self, message: str, ctx: WorkflowContext[str])-> None:
        print(f"Agent handling: {message}")
        await ctx.send_message({"status": "Report Created sucessfully"})

