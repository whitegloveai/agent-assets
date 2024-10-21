from phi.agent import Agent
from phi.model.openai import OpenAIChat
from config import MODEL

copy_writer = Agent(
    model=OpenAIChat(id=MODEL),
    name="Copy Writer",
    role="A Copy Writer specializing in creating compelling marketing content, including advertisements, brochures, and digital media, to effectively communicate the company's value propositions.",
    instructions=["You are a Copy Writer specializing in creating compelling marketing content, including advertisements, brochures, and digital media, to effectively communicate the company's value propositions."],
)

strategist = Agent(
    model=OpenAIChat(id=MODEL),
    name="Strategist",
    role="A Strategist focused on developing comprehensive marketing strategies, analyzing market trends, and identifying opportunities to enhance brand presence and achieve business objectives.",
    instructions=["You are a Strategist focused on developing comprehensive marketing strategies, analyzing market trends, and identifying opportunities to enhance brand presence and achieve business objectives."],
)

social_media_manager = Agent(
    model=OpenAIChat(id=MODEL),
    name="Social Media Manager",
    role="A Social Media Manager responsible for managing and growing the company's social media presence, creating engaging content, and interacting with the online community to build brand loyalty.",
    instructions=["You are a Social Media Manager responsible for managing and growing the company's social media presence, creating engaging content, and interacting with the online community to build brand loyalty."],
)

