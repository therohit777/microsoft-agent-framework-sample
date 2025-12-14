from datetime import datetime
from app.workflows import workflow
from app.workflows.workflow import agentworkflow
import asyncio
import os
from app.db.mongodb_database import get_mongo_connection


async def handle_messages(message: str):
    try:
        collection =  get_mongo_connection()
        user_data = {
            "user_type": "user",
            "message": message,
            "timestamp": datetime.now()
        }
        # Insert into user data 
        collection.insert_one(user_data)
        workflow =  agentworkflow()
        result = await workflow.run(message)
        # Streaming execution - get events as they happen
        # async for event in workflow.run_stream(message):
        #     if isinstance(event, WorkflowOutputEvent):
        #         print(f"Workflow completed: {event.data}")
        final_reponse=result[4].data[0]["response"]
        assitant_data = {
            "user_type": "assistant",
            "message": final_reponse,
            "timestamp": datetime.now()
        }
        # Insert into AI Assistant data 
        collection.insert_one(assitant_data)
        return final_reponse
    except Exception as e:
        print(f"An error occurred in workflow: {e}")
        return None  
