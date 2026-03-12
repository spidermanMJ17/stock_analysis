#this agent will help to know WHY STOCK MOVED

from agno.models.groq import Groq
from agno.agent import Agent
from tools.market_tool import get_stock_data
from tools.news_tool import search_news
from dotenv import load_dotenv
load_dotenv()

stock_agent = Agent(
    model=Groq(id="openai/gpt-oss-120b"),
    name="Stock Movement Analyst",

    instructions="""
    You are a financial analyst.

    Your job is to explain why a stock moved.

    Use market data and recent news to explain
    the possible reasons for stock depreciation or increase.
    """,

    tools=[
        get_stock_data,
        search_news
    ]
)