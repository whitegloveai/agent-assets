from phi.agent import Agent 
from phi.model.openai import OpenAIChat
from config import MODEL

bookkeeper = Agent(
    model=OpenAIChat(id=MODEL),
    name="Bookkeeper",
    role="A Bookkeeper who accurately records financial transactions, manages ledgers, and ensures the integrity of financial data for informed decision-making.",
    instructions=["You are a Bookkeeper who accurately records financial transactions, manages ledgers, and ensures the integrity of financial data for informed decision-making."],
    show_tools_calls=True,
    markdown=True
)

treasurer = Agent(
    model=OpenAIChat(id=MODEL),
    name="Treasurer",
    role="A Treasurer responsible for managing the company's cash flow, overseeing investments, and ensuring optimal liquidity to support business operations and growth.",
    instructions=["You are a Treasurer responsible for managing the company's cash flow, overseeing investments, and ensuring optimal liquidity to support business operations and growth."],
    show_tools_calls=True,
    markdown=True
)

controller = Agent(
    model=OpenAIChat(id=MODEL),
    name="Controller",
    role="A Controller overseeing financial reporting, budgeting, and compliance, ensuring that all financial activities align with organizational policies and regulatory requirements.",
    instructions=["You are a Controller overseeing financial reporting, budgeting, and compliance, ensuring that all financial activities align with organizational policies and regulatory requirements."],
    show_tools_calls=True,
    markdown=True
)
