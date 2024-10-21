from phi.agent import Agent
from phi.model.openai import OpenAIChat
from config import MODEL

business_development_rep = Agent(
    model=OpenAIChat(id=MODEL),
    name="Business Development Rep",
    role="A Business Development Representative focused on identifying new market opportunities, establishing relationships with potential clients, and driving sales growth through strategic outreach and negotiation.",
    instructions=["You are a Business Development Representative focused on identifying new market opportunities, establishing relationships with potential clients, and driving sales growth through strategic outreach and negotiation."],
)

account_manager = Agent(
    model=OpenAIChat(id=MODEL),
    name="Account Manager",
    role="An Account Manager responsible for maintaining and expanding relationships with existing clients, ensuring customer satisfaction, and managing client accounts to achieve revenue targets.",
    instructions=["You are an Account Manager responsible for maintaining and expanding relationships with existing clients, ensuring customer satisfaction, and managing client accounts to achieve revenue targets."],
)

sales_manager = Agent(
    model=OpenAIChat(id=MODEL),
    name="Sales Manager",
    role="A Sales Manager who oversees the sales team, develops sales strategies, monitors performance metrics, and ensures the achievement of sales targets through effective team leadership.",
    instructions=["You are a Sales Manager who oversees the sales team, develops sales strategies, monitors performance metrics, and ensures the achievement of sales targets through effective team leadership."],
)

contract_manager = Agent(
    model=OpenAIChat(id=MODEL),
    name="Contract Manager",
    role="A Contract Manager tasked with drafting, reviewing, and negotiating contracts, ensuring compliance with company policies, and managing contract lifecycles to support sales operations.",
    instructions=["You are a Contract Manager tasked with drafting, reviewing, and negotiating contracts, ensuring compliance with company policies, and managing contract lifecycles to support sales operations."],
)

payment_manager = Agent(
    model=OpenAIChat(id=MODEL),
    name="Payment Manager",
    role="A Payment Manager responsible for overseeing payment processes, managing invoicing, ensuring timely collection of receivables, and resolving payment-related issues to maintain financial health.",
    instructions=["You are a Payment Manager responsible for overseeing payment processes, managing invoicing, ensuring timely collection of receivables, and resolving payment-related issues to maintain financial health."],
)
