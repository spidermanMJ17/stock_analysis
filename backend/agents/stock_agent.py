#this agent will help to know WHY STOCK MOVED

from agno.agent import Agent
from tools.market_tool import get_stock_data
from tools.news_tool import search_news


stock_agent = Agent(
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