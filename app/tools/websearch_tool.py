from pydantic import Field
from typing_extensions import Annotated
from agent_framework import HostedWebSearchTool
from tavily import TavilyClient
import os



# def get_hosted_web_search_tool():
#     """
#     Returns a HostedWebSearchTool configured with user location metadata.
#     """
#     return HostedWebSearchTool(
#         additional_properties={
#             "user_location": {
#                 "city": "Delhi",
#                 "country": "IN"
#             }
#         }
#     )

TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(
        api_key=os.getenv("TAVILY_API_KEY")
)

def web_search_tool(
    query: Annotated[str, Field(description="The search query")],
) -> str:
    """
    Perform a web search for current and factual information.
    """
    search_response =  tavily_client.search(
        query=query,
        search_depth="advanced",
        include_answer=True,
        include_sources=True,
        max_results=5
    )
    # print(f"Websearch Tool response: {search_response}")
    return search_response
