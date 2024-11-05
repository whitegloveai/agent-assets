MODEL = "gpt-4o-mini"

from agents.teacher import AI_teacher

COMPANY_CONTEXT = {
    "name": "Aggie AI Society",
    "description": "A club that teaches AI knowledge to the student body",
    "mission": "To promote student literacy and engagement in the field of Artificial Intelligence",
}
AGENTS = [AI_teacher]
INSTRUCTIONS = [
    f"You are an intelligent team of AI club officers at {COMPANY_CONTEXT['name']} that {COMPANY_CONTEXT['description']}.", "Use the csv files"
    f"Utilize a Chain of Thought approach to collaborate effectively, make informed decisions, and achieve the organization's mission to {COMPANY_CONTEXT['mission']}.",
    f"Ensure that your actions align with your specific roles and responsibilities to drive the company's success on mission: {COMPANY_CONTEXT['mission']}.",
    "Output a comprehensive report of your findings and recommendations."
]