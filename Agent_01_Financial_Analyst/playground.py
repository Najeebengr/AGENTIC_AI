from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
import phi.api
from os import getenv
from dotenv import load_dotenv

import os
import phi
from phi.playground import Playground, serve_playground_app

load_dotenv()

phi.api = os.getenv('PHI_API_KEY')

# Web Search Agent
web_search_agent = Agent(
    name='Web Search Agent',
    description='Search the web for information',
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
    description='A financial analyst agent that can give recommendations',
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview",api_key=getenv('GROQ_API_KEY')),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use Tables to display financial information"],
    show_tool_calls=True,
    markdown=True
)

app = Playground(agents=[web_search_agent, financial_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app("playground:app",reload=True)