from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Web Search Agent
web_search_agent = Agent(
    name='Web Search Agent',
    description='Search the web information',
    role="Search the web for information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview",api_key=getenv('GROQ_API_KEY')),
    tools=[GoogleSearch(fixed_language='english',fixed_max_results=5),DuckDuckGo(fixed_max_results=5)],
    instructions=["Always include source and date in your search results"],
    show_tool_calls=True,
    markdown=True
)

# Financial Agent
financial_agent = Agent(
    name='Financial Agent',
    description='An agent that can provide financial information',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview",api_key=getenv('GROQ_API_KEY')),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use Tables to display financial information"],
    show_tool_calls=True,
    markdown=True
)

# Multi-Agent
multi_ai_agent = Agent(
    team=[web_search_agent, financial_agent],
    instructions=["Always include source and date in your search results", "Use Tables to display financial information"],
    show_tool_calls=True,
    model=Groq(api_key=getenv('GROQ_API_KEY')),
    markdown=True
)

# Response
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Tesla", stream=True)