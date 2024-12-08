# MODEL = "gpt-4o-mini"

# from agents.teacher import AI_teacher

# COMPANY_CONTEXT = {
#     "name": "Aggie AI Society",
#     "description": "A club that teaches AI knowledge to the student body",
#     "mission": "To promote student literacy and engagement in the field of Artificial Intelligence",
# }
# AGENTS = [AI_teacher]
# INSTRUCTIONS = [
#     f"You are an intelligent team of AI club officers at {COMPANY_CONTEXT['name']} that {COMPANY_CONTEXT['description']}.", "Use the csv files"
#     f"Utilize a Chain of Thought approach to collaborate effectively, make informed decisions, and achieve the organization's mission to {COMPANY_CONTEXT['mission']}.",
#     f"Ensure that your actions align with your specific roles and responsibilities to drive the company's success on mission: {COMPANY_CONTEXT['mission']}.",
#     "Output a comprehensive report of your findings and recommendations."
# ]




MODEL = "gpt-4o-mini"

from agents.email_agent import EmailAgent

COMPANY_CONTEXT = {
    "name": "Email Prioritization System",
    "description": "A tool that helps users prioritize emails based on urgency.",
    "mission": "To streamline task management by identifying high-priority communications effectively.",
}

AGENTS = [EmailAgent]

INSTRUCTIONS = [
    f"You are part of the {COMPANY_CONTEXT['name']}, which {COMPANY_CONTEXT['description']}.",
    "Your goal is to analyze the email CSV file, determine priority levels, and help users manage emails efficiently.",
    f"Always align your actions with the mission: {COMPANY_CONTEXT['mission']}.",
    "Provide a clear and actionable summary for the user.",
]






