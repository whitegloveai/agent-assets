import os
from phi.agent import Agent
from phi.tools.wikipedia import WikipediaTools
from phi.tools.youtube_tools import YouTubeTools
from phi.tools.googlesearch import GoogleSearch
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("YOUTUBE_API_KEY")



wikipedia_tools = WikipediaTools()
youtube_tools = YouTubeTools()
google_tools = GoogleSearch()


agent = Agent(
    tools=[wikipedia_tools, youtube_tools, google_tools],
    description="I am an aggregate agent capable of finding the latest news, Wikipedia information, and YouTube video summaries for companies or people. Ask me anything!",
    instructions=[
        "1. When searching for a person or company, retrieve the latest news from Google.",
        "2. Fetch any relevant Wikipedia information about the entity.",
        "3. If applicable, search for YouTube videos and summarize them.",
    ],
    show_tool_calls=True,
    debug_mode=True,
)


def search():
    query = input("Enter the name of the company or person you want to search for: ")
    response = agent.print_response(f"Find the latest news, wikipedia information and give youtube videos {query}", markdown=True)
    print(response)


search()
