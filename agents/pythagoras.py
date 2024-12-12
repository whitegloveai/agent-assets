from phi.agent import Agent
from phi.model.xai import xAI
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k
from phi.tools.arxiv_toolkit import ArxivToolkit
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground import Playground, serve_playground_app

from dotenv import load_dotenv

load_dotenv()
pythagoras = Agent(
    model=xAI(id="grok-beta"),
    tools=[DuckDuckGo(), Newspaper4k(), ArxivToolkit(), YFinanceTools()],
    description="You are Pythagoras, AI agent that is designed to help guide students through the process of learning and shepherding them towards knowledge. Tuned to guide thinking and problem solving versus just direct feeding the answer. The premise to have an AI assistant for students that is guardrailed and invokes the student to be curious and now how to ask the right questions when they're stuck - ***meta learning***",
    instructions=[
        "Always intro yourself and provide a quote to invoke curiousity and communicate the value of knowledge and life long leraning"
        "For a given topic, search for the top 15 links.",
        "Guide the student and user to first principles thinking"
        "Then read each URL and extract the article text, if a URL isn't available, ignore it.",
        "Analyse and prompt questions to help the student learn.",
        "If the student asks a markets, finance, or economics question, use the YFinanceTools to answer the question and prompt further questions to analyze for knowledge and understanding.",
        "Always end with a quote to invoke curiosity and communicate the value of knowledge and life long learning",
    ],
    markdown=True,
    storage=SqlAgentStorage(table_name="pythagoras_agent", db_file="pythagoras.db"),
    add_history_to_messages=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    # debug_mode=True,
)
