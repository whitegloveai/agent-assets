from phi.agent import Agent
from phi.tools.youtube_tools import YouTubeTools
from dotenv import load_dotenv

load_dotenv()

youtube_tools = YouTubeTools()
youtube_agent = Agent(
    tools=[youtube_tools],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the youtube videos of the company or person provided by the user.",
)


