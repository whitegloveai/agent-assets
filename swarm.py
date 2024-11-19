import asyncio
from phi.agent import Agent
from dotenv import load_dotenv
from config import COMPANY_CONTEXT,AGENTS,INSTRUCTIONS
from agents.teacher import AI_teacher

load_dotenv()

swarm = Agent(
    team = AGENTS,
    instructions = INSTRUCTIONS,
    show_tool_calls=True,
    markdown=True
)

async def deploy():
<<<<<<< HEAD
    AI_teacher.print_response("Analyze the given CSV file and teach me about AI's data analysis capability", stream=True)
    
=======
    swarm.print_response(COMPANY_CONTEXT)
>>>>>>> 6c56fcd47a129395d22d9302c4b226dd107ebd97

if __name__ == "__main__":
    asyncio.run(deploy())
