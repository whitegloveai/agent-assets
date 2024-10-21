import asyncio

from phi.agent import Agent
from agents.marketing import copy_writer, strategist, social_media_manager

from dotenv import load_dotenv

load_dotenv()

# Define the company context, agents, and instructions
COMPANY_CONTEXT = {
    "name": "WhitegloveAI",
    "description": "A company that sells AI solutions to businesses.",
    "mission": "To advise secure and safe adoption of AI in businesses to augment human intelligence. Primarily discovering data ontologies and data management issues to drive streamlined data intelligence or understand where AI can be most effective.",
}
AGENTS = [strategist, copy_writer, social_media_manager]
INSTRUCTIONS = [
    f"You are an intelligent team of AI employees at {COMPANY_CONTEXT['name']} that {COMPANY_CONTEXT['description']}.",
    "Each member specializes in their respective departments—finance, marketing, sales, and accounting.",
    f"Utilize a Chain of Thought approach to collaborate effectively, make informed decisions, and achieve the company's mission to {COMPANY_CONTEXT['mission']}.",
    f"Ensure that your actions align with your specific roles and responsibilities to drive the company's success on mission: {COMPANY_CONTEXT['mission']}.",
    "Output a comprehensive report of your findings and recommendations."
]

swarm = Agent(
    team = AGENTS,
    instructions = INSTRUCTIONS,
    show_tool_calls=True,
    markdown=True
)
async def deploy():
    swarm.print_response(COMPANY_CONTEXT)

if __name__ == "__main__":
    asyncio.run(deploy())
