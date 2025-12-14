from fastapi import FastAPI
from app.log_config import LOGGING_CONFIG
import logging.config
from fastapi.middleware.cors import CORSMiddleware

# Import for lifespan event
from contextlib import asynccontextmanager
# from .tools.sql_tool import initialize_global_financial_agent÷\

# Initialize logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)  # get a logger instance

# Lifespan context manager for startup and shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    logger.info("Application startup: Initializing the EY Server...")
    # await initialize_global_financial_agent()
    logger.info("✅ EY Server initialization process complete.")
    yield
    # Code to run on shutdown (if any)
    logger.info("Application shutdown.")

# Create FastAPI app with OpenAPI documentation configuration and lifespan
app = FastAPI(
    title="ABHFL Middleware Server",
    description="API for ABHFL AI Portal !",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    swagger_ui_parameters={
        "persistAuthorzation":True
    },
    lifespan=lifespan  # Add the lifespan manager
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
    
)

# Import and include the router
from app.routes.routes import router
app.include_router(router)