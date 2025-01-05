from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools 
from phi.tools.duckduckgo import DuckDuckGo
import os 
import openai 
from dotenv import load_dotenv 

load_dotenv()


# setx GROQ_API_KEY = "API_KEY" WRITE IT IN THE TERMINAL ... FRO MAKE IT WORKING 
web_search_agent = Agent(
    name = "web search agent",
    role = "search the web",
    model= Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls = True,
    markdown = True
)

#web_search_agent.print_response()


## Finance agent 
finance_agent = Agent(
    name="Finance Agent",
    model= Groq(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)



multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("summarize analyst recomdation and share the latest news for NVIDA" ,stream = True)


