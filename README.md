🚁 Drone Intelligence System for India
An end-to-end, AI-powered Drone Knowledge Hub designed to provide comprehensive information on India's booming drone ecosystem. This system integrates Retrieval-Augmented Generation (RAG), custom calculation tools via an MCP Server, and a professional Streamlit Dashboard.

🌟 Key Features
Intelligent AI Advisor: A RAG-powered chatbot that provides accurate information on Drone Rules 2021, DGCA guidelines, and use cases.

Drone Calculation Suite:

Flight Time Calculator: Estimates endurance based on weight and battery capacity.

ROI Predictor: Detailed break-even and profitability analysis for drone businesses.

Compliance Checker: Instantly verifies if a drone meets Indian regulatory requirements.

Indian Startup Ecosystem: A structured database of leading Indian drone manufacturers and training institutes.

Interactive Dashboard: A clean, responsive interface with real-time data visualization and chat history.

🏗 System Architecture
The project follows a modular three-tier architecture:

Frontend: Built with Streamlit for a responsive user interface.

Backend: FastAPI serving as the central hub, integrating AI and calculation services.

Intelligence Layer:

RAG: Uses FAISS/ChromaDB for semantic search over unstructured drone documents.

MCP Server: Custom logic for specialized drone calculations.

📂 Repository Structure

drone-intelligence-system/
├── data/                  # Datasets (CSV, JSON, RAG docs)
│   ├── raw/               # Original lists of startups/regulations
│   └── rag/               # Processed text for vector embeddings
├── mcp_server/            # MCP server logic and specialized tools
├── api/                   # FastAPI backend routes and models
├── frontend/              # Streamlit source code and assets
├── tests/                 # Unit and integration test scripts
├── docs/                  # API documentation and user guides
└── Dockerfile             # Container configuration
🚀 Getting Started
Prerequisites
Python 3.9+

Docker (Optional for containerized setup)

OpenAI API Key (or local LLM environment)

Installation
Clone the Repository:

Bash

git clone https://github.com/your-username/drone-intelligence-system.git
cd drone-intelligence-system
Install Dependencies:

Bash

pip install -r requirements.txt
Initialize the Vector Database:

Bash

python scripts/initialize_rag.py
Run the System:

Start Backend: uvicorn api.main:app --reload

Start Dashboard: streamlit run frontend/src/app.py

📊 Sample Data: Indian Drone Ecosystem
The system comes pre-loaded with data on major Indian players: | Company Name | Primary Category | HQ / Location | | :--- | :--- | :--- | | ideaForge Technology | Defense & Civil | Mumbai | | Garuda Aerospace | Agriculture | Chennai | | Zen Technologies | Defense | Hyderabad | | Asteria Aerospace | Enterprise | Bengaluru |
