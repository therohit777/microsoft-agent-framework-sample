from agent_framework import (
    AgentExecutor,
    Case,
    Default,
    WorkflowBuilder,
)
from app.agents.lead_agent import LeadAgent
from app.agents.orchestrator_agent import OrchestratorAgent
from app.agents.report_agent import ReportGenerateAgent
from app.agents.websearch_agent import WebsearchAgent
from app.agents.support_agent import SupportAgent

def agentworkflow():
    """
    Creates and returns a workflow with orchestrator-based routing.
    
    Returns:
        workflow: A configured workflow that routes messages based on 
                  orchestrator decisions
    """
    # Create executors
    orchestrator_executor = OrchestratorAgent(id="orchestrator")
    lead_executor = LeadAgent(id="lead")
    websearch_executor = WebsearchAgent(id="websearch")
    # report_executor = ReportGenerateAgent(id="report")
    support_executor = SupportAgent(id="support")

    # Build the workflow with switch-case routing
    builder = WorkflowBuilder()

    # Set orchestrator as the starting point
    builder.set_start_executor(orchestrator_executor)

    # The message received by the condition will be the routing_decision string
    builder.add_switch_case_edge_group(
        orchestrator_executor,
        [
            Case(
                condition=lambda message: message == "lead",
                target=lead_executor,
            ),
            Case(
                condition=lambda message: message == "websearch",
                target=websearch_executor,
            ),
            # Case(
            #     condition=lambda message: message == "report",
            #     target=report_executor,
            # ),
            Default(target=support_executor)  # Default fallback
        ],
    )

    # Build and return the workflow
    return builder.build()