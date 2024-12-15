import os
from phi.agent import Agent, RunResponse
from phi.model.google import Gemini
from dotenv import load_dotenv


load_dotenv()


api_key = os.getenv("GOOGLE_API_KEY")




model = Gemini(id="gemini-1.5-flash", api_key=api_key)


agent = Agent(
    model=model,
    markdown=True,
)


def provide_emotional_support(user_input):
    """
    Provides empathetic and supportive responses to the user.
    
    :param user_input: The user's message describing their feelings or situation.
    :return: The chatbot's supportive response.
    """
    response = agent.run(
        f"As a therapeutic chatbot, respond empathetically and supportively to the following: {user_input}"
    )
    return response.content


def therapeutic_chatbot():
    print("Hello! I'm here to provide emotional support. Feel free to share how you're feeling.")
    print("Type 'exit' anytime to end our chat.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Take care! Remember, you're not alone.")
            break

        try:
            response = provide_emotional_support(user_input)
            print(f"Therapeutic Bot: {response}")
        except Exception as e:
            print(f"Oops! Something went wrong: {e}")

# Run the chatbot
if __name__ == "__main__":
    therapeutic_chatbot()
