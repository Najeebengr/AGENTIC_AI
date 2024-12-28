# Financial and Web Search Multi-Agent System

This repository contains a multi-agent system designed to provide web search and financial analysis functionalities. The system leverages **Phi Tools** to implement agents capable of interacting with APIs for web search and financial data retrieval.

## 📌 Features

### Web Search Agent
- Performs web searches using **Google Search** and **DuckDuckGo** tools.
- Fetches the latest, relevant information from the web.
- Always includes the source and date in search results for reliability.
- Outputs results in a clean, markdown format.

### Financial Agent
- Provides financial analysis using **YFinanceTools**.
- Features include:
  - Stock price retrieval
  - Analyst recommendations
  - Stock fundamentals
  - Latest company news
- Displays financial data in well-structured tables for better readability.

### Multi-Agent System
- Combines the Web Search Agent and Financial Agent.
- Handles complex queries involving web information and financial data analysis.
- Operates with **Groq's AI Model** for robust natural language processing.

## 🛠️ Tech Stack

- **Phi Tools**: Agents, tools, and APIs for implementing a multi-agent system.
- **Groq AI Model**: A language model designed for seamless tool integration.
- **YFinanceTools**: Fetches financial data, stock prices, and more.
- **Google Search and DuckDuckGo Tools**: Fetches reliable web search results.
- **Python**: Core programming language for implementation.
- **FastAPI**: Used for hosting the playground application.

## 📂 Project Structure

```plaintext
.
├── financial_agent.py      # Handles the Financial Agent logic
├── playground.py           # Hosts the Playground app for Web and Financial Agents
├── .env                    # Environment variables (API keys)
└── requirements.txt        # Python dependencies