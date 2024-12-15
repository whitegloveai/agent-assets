from phi.agent import Agent
from phi.tools.googlesearch import GoogleSearch
from dotenv import load_dotenv

# Load environment variables (for API keys or other credentials)
load_dotenv()

# Initialize the GoogleSearch tool and agent
google_agent = Agent(
    tools=[GoogleSearch()],
    description="You are a news agent that helps users find the latest news.",
    instructions=[
        "Given a topic by the user, respond with 4 latest news items about that topic.",
        "Search for 10 news items and select the top 4 unique items.",
        "Search in English",
    ],
    show_tool_calls=True,
    debug_mode=True,
)

# Function to prompt the user and search for the latest news about their input
def get_latest_news():
    query = input("Enter the name of the company or person you want to search for: ")
    print(f"\nSearching for latest news about: {query}\n")
    
    # Run the agent to fetch the latest news based on user input
    response = google_agent.print_response(query, markdown=True)
    print(response)

# Run the news search
if __name__ == "__main__":
    get_latest_news()
