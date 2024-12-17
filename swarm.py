import asyncio
from phi.agent import Agent
from dotenv import load_dotenv
from config import COMPANY_CONTEXT, INSTRUCTIONS
from agents.email_agent import EmailAgent  # Import EmailAgent

load_dotenv()

# Team definition
AGENTS = [EmailAgent]  # Load the email agent here

# Define the agent swarm
swarm = Agent(
    team=AGENTS,
    instructions=INSTRUCTIONS,
    show_tool_calls=True,
    markdown=True,
)

# Deploy the agent team
async def deploy():
    print("Starting the swarm...")
    # Send a task to the swarm
    swarm.print_response("Process the email CSV file and prioritize emails.")
    print("Swarm execution complete.")

if __name__ == "__main__":
    asyncio.run(deploy())
