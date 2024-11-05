from phi.agent import Agent
from phi.model.openai import OpenAIChat
from config import MODEL

from pathlib import Path
from phi.tools.csv_tools import CsvTools


known_output_csv = Path("./data/Energy_consumption.csv")


AI_teacher = Agent(
    tools=[CsvTools(csvs=[known_output_csv])],
    model=OpenAIChat(id=MODEL),
    name="AI Teacher",
    role="A Teacher that provides general knowledge about AI",
    show_tool_calls=True,
    instructions=[
        "First always get the list of files",
        "Then check the columns in the file",
        "Then run a general analysis acting as a data analysis teacher, explaining how AI can supercharge and help humans",
    ],
)





