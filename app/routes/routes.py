import datetime
import logging
import pytz

from app.models.schema import (
    ApiResponse,
    MessageRequest
)
from fastapi import APIRouter
from app.controllers.handle_messages import handle_messages

# Configure logger
logger = logging.getLogger(__name__)
router = APIRouter()

#Server Check API
@router.get("/server-check")
def server_check():
    try:
        # Get current time in IST
        ist = pytz.timezone('Asia/Kolkata')
        current_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
        logger.info(f"Server check endpoint hit at {current_time}")

        return ApiResponse(
            status_code=200,
            message="Server check successful. Welcome to ABHFL Middleware Server!",
            data={
                "serverName": "ABHFL Middleware Server",
                "timestamp": current_time
            }
        )

    except Exception as e:
        print(e)
        logger.error(f"An ERROR occurred in the Server check: {e}")
        return ApiResponse(
            status_code=500,
            message="Server check failed.",
            data={}
        )

@router.post("/chat")
async def chat(payload: MessageRequest):
    try:
        chat_response = await handle_messages(payload.message)
        print(f"Chat response: {chat_response}")
        if chat_response is None:
            return ApiResponse(
                status_code=500,
                message="Failed to process message",
                data={chat_response}
            )

        return ApiResponse(
            status_code=200,
            message="Message received successfully.",
            data={
                "message": chat_response
            }
        )

    except Exception as e:
        logger.exception("Error occurred in /chat API")
        return ApiResponse(
            status_code=500,
            message=str(e),   # ✅ string, not exception
            data={}
        )
