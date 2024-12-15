from phi.agent import Agent
from phi.tools.wikipedia import WikipediaTools
from dotenv import load_dotenv


load_dotenv()


wikipedia_tools = WikipediaTools()


wiki_agent = Agent(tools=[wikipedia_tools], show_tool_calls=True)


def get_wikipedia_info():
    query = input("Enter the name of the company or person you want to search on Wikipedia: ")
    print(f"\nSearching Wikipedia for: {query}\n")
    
    
    response = wiki_agent.print_response(f"Search wikipedia for '{query}'")
    print(response)


if __name__ == "__main__":
    get_wikipedia_info()
