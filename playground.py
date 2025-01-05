## USED FOR CREATING THE PLAYGROUND -> connecting to playground UI

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv 
from phi.model.groq import Groq 

load_dotenv()

web_search_agent = Agent(
    name = "web search agent",
    role = "search the web",
    model= Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls = True,
    markdown = True
)

## Finance agent 
finance_agent = Agent(
    name="Finance Agent",
    model= Groq(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
