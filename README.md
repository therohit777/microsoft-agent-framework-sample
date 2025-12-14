# Multi-Agent Orchestration System

A sophisticated multi-agent system built with **Microsoft Azure AI Agent Framework** that intelligently routes user queries to specialized agents for web search, financial information retrieval, and lead capture.

## Overview

This project implements an orchestrator-based multi-agent architecture where a central orchestrator agent analyzes user queries and delegates tasks to specialized agents based on intent and requirements.

## Key Features

### 🤖 Intelligent Agent Orchestration
- **Orchestrator Agent**: Central coordinator that analyzes user queries and routes them to appropriate specialized agents
- **Web Search & Finance Agent**: Performs comprehensive web searches, retrieves relevant information, and handles financial queries and market data
- **Lead Capture Agent**: Collects and stores customer information including name, phone number, email, address, and monthly income
- **Support Agent**: Provides customer support and assistance
- **Report Agent**: Generates reports and analytics(To be added)

### Specialized Functionalities

#### 1. Web Search & Financial Information Service
- Real-time web search capabilities powered by Tavily API
- Financial insights and market analysis
- Investment-related queries
- Intelligent information extraction and summarization
- Context-aware responses

#### 2. Lead Management
- Captures customer details:
  - Full Name
  - Phone Number
  - Email Address
  - Physical Address
  - Monthly Income
- Stores lead data in MongoDB for persistence

## Microsoft Azure AI Agent Framework Highlights

The project leverages the powerful capabilities of Microsoft's Agent Framework:

### Core Features
- **Multi-Agent Orchestration**: Seamlessly coordinate multiple specialized agents with intelligent routing and delegation
- **Built-in Memory & State Management**: Maintain conversation context, user preferences, and interaction history across sessions
- **Tool Integration Support**: Native support for external APIs, databases, and third-party services with easy integration
- **Flexible Agent Communication**: Agents can collaborate, share information, and work together on complex tasks

### Workflow Types
The framework provides built-in support for various workflow patterns:

- **Sequential Workflows**: Execute tasks in a predefined order with dependency management
- **Parallel Workflows**: Run multiple agents simultaneously for faster processing
- **Conditional Workflows**: Dynamic routing based on conditions and business logic
- **Human-in-the-Loop**: Seamless integration for human oversight and approval steps
- **Event-Driven Workflows**: Reactive agents that respond to events and triggers

### Advanced Capabilities
- **Scalable Architecture**: Enterprise-grade reliability with horizontal scaling support
- **Error Handling & Retry Logic**: Built-in resilience with automatic retry mechanisms
- **Monitoring & Observability**: Comprehensive logging and tracing for debugging and optimization
- **Security & Compliance**: Role-based access control and audit trails

## Prerequisites

- Python 3.8 or higher
- MongoDB instance
- Tavily API account (for web search)
- Azure OpenAI credentials

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd backend-copilot
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with the following credentials:

```env
# MongoDB Configuration
MONGODB_URI=your_mongodb_connection_string

# Tavily API (Web Search)
TAVILY_API_KEY=your_tavily_api_key

# Azure OpenAI Credentials
AZURE_OPENAI_ENDPOINT=your_azure_endpoint
AZURE_OPENAI_API_KEY=your_azure_api_key
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
AZURE_OPENAI_API_VERSION=your_api_version
```

### 5. Run the Application

```bash
python main.py
```

## Usage

Once the application is running, interact with the orchestrator agent by submitting queries:

- **For Web Search & Finance**: "Find information about renewable energy trends" or "What's the current market outlook for tech stocks?"
- **For Lead Capture**: "I'd like to sign up" or "Capture my information"
- **For Support**: "I need help with my account"
- **For Reports**: "Generate a summary report of recent activities"

The orchestrator will automatically route your query to the appropriate specialized agent.

## Project Structure

```
backend-copilot/
├── app/
│   ├── __pycache__/
│   ├── agents/
│   │   ├── __pycache__/
│   │   ├── lead_agent.py          # Lead capture agent
│   │   ├── orchestrator_agent.py  # Main orchestrator
│   │   ├── report_agent.py        # Report generation agent
│   │   ├── support_agent.py       # Customer support agent
│   │   └── websearch_agent.py     # Web search & finance agent
│   ├── controllers/               # API controllers
│   ├── db/                        # Database configurations
│   ├── mcps/                      # MCP integrations
│   ├── middlewares/               # Custom middlewares
│   ├── models/                    # Data models
│   ├── prompts/                   # Agent prompts
│   ├── routes/                    # API routes
│   ├── scripts/                   # Utility scripts
│   ├── tools/                     # Agent tools
│   ├── utils/                     # Helper utilities
│   ├── workflows/                 # Workflow definitions
│   ├── __init__.py
│   └── log_config.py              # Logging configuration
├── logs/                          # Application logs
├── venv/                          # Virtual environment
├── .env                           # Environment variables
├── .gitignore                     # Git ignore rules
├── docker-compose.yml             # Docker composition
├── Dockerfile                     # Docker configuration
├── main.py                        # Application entry point
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies
```

## Docker Deployment

The project includes Docker support for easy deployment:

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build manually
docker build -t multi-agent-system .
docker run -p 8000:8000 multi-agent-system
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
