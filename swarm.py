
# import asyncio
# from phi.agent import Agent
# from dotenv import load_dotenv
# from config import COMPANY_CONTEXT, AGENTS, INSTRUCTIONS
# from agents.email_agent import EmailAgent

# load_dotenv()

# # Define the agent swarm
# swarm = Agent(
#     team=AGENTS,
#     instructions=INSTRUCTIONS,
#     show_tool_calls=True,
#     markdown=True,
# )

# # Deploy the email prioritization agent
# async def deploy():
#     EmailAgent.print_response("Analyze the given email CSV file and prioritize emails based on due dates.", stream=True)
#     swarm.print_response(COMPANY_CONTEXT)

# if __name__ == "__main__":
#     asyncio.run(deploy())


# import asyncio
# import pandas as pd
# from phi.agent import Agent
# from dotenv import load_dotenv
# from config import COMPANY_CONTEXT, AGENTS, INSTRUCTIONS
# from agents.email_agent import EmailAgent

# load_dotenv()

# # Define the agent swarm
# swarm = Agent(
#     team=AGENTS,
#     instructions=INSTRUCTIONS,
#     show_tool_calls=True,
#     markdown=True,
# )

# # Function to process the emails in smaller chunks
# def process_in_chunks(df, chunk_size=50):  # Reduce chunk size to avoid token overflow
#     total_emails = len(df)
#     all_prioritized_emails = []  # List to store prioritized emails

#     for i in range(0, total_emails, chunk_size):
#         chunk = df.iloc[i:i+chunk_size]
#         prioritized_chunk = process_chunk(chunk)
#         all_prioritized_emails.append(prioritized_chunk)

#     # Combine all chunks back into a single DataFrame
#     prioritized_df = pd.concat(all_prioritized_emails, ignore_index=True)
    
#     return prioritized_df

# # Function to process each chunk of emails and prioritize based on due dates
# def process_chunk(chunk):
#     # Example: Prioritize emails based on due date (you can modify this as needed)
#     chunk.loc[:, 'Due Date'] = pd.to_datetime(chunk['Due Date'], errors='coerce')
#     chunk.loc[:, 'Priority'] = chunk['Due Date'].apply(lambda x: 'High Priority' if x <= pd.Timestamp.now() + pd.Timedelta(days=1) else 
#                                                     'Medium Priority' if x <= pd.Timestamp.now() + pd.Timedelta(days=7) else 'Low Priority')

    
#     return chunk

# # Deploy the email prioritization agent
# async def deploy():
#     # Load the CSV file
#     emails = pd.read_csv("data/emails.csv")
    
#     # Process the emails in chunks and get the prioritized emails
#     prioritized_emails = process_in_chunks(emails)
    
#     # Save the prioritized emails to a new CSV file
#     prioritized_emails.to_csv('data/prioritized_emails.csv', index=False)
#     print("Prioritized emails have been saved to 'data/prioritized_emails.csv'")
    
#     # Run the email prioritization agent (printing responses as per your setup)
#     EmailAgent.print_response("Analyze the given email CSV file and prioritize emails based on due dates.", stream=True)
#     swarm.print_response(COMPANY_CONTEXT)

# if __name__ == "__main__":
#     asyncio.run(deploy())


import asyncio
import pandas as pd
from phi.agent import Agent
from dotenv import load_dotenv
from config import COMPANY_CONTEXT, AGENTS, INSTRUCTIONS
from agents.email_agent import EmailAgent

load_dotenv()

# Define the agent swarm
swarm = Agent(
    team=AGENTS,
    instructions=INSTRUCTIONS,
    show_tool_calls=True,
    markdown=True,
)

# Function to process the emails in smaller chunks
def process_in_chunks(df, chunk_size=50):  # Reduce chunk size to avoid token overflow
    total_emails = len(df)
    all_prioritized_emails = []  # List to store prioritized emails

    for i in range(0, total_emails, chunk_size):
        chunk = df.iloc[i:i+chunk_size]
        prioritized_chunk = process_chunk(chunk)
        all_prioritized_emails.append(prioritized_chunk)

    # Combine all chunks back into a single DataFrame
    prioritized_df = pd.concat(all_prioritized_emails, ignore_index=True)
    
    # Ensure the final emails are sorted by Due Date in ascending order
    prioritized_df = prioritized_df.sort_values(by='Due Date', ascending=True).reset_index(drop=True)
    
    return prioritized_df

# Function to process each chunk of emails and prioritize based on due dates
def process_chunk(chunk):
    # Ensure Due Date is in datetime format
    chunk['Due Date'] = pd.to_datetime(chunk['Due Date'], errors='coerce')

    # Apply priority rules based on due dates
    chunk['Priority'] = chunk['Due Date'].apply(lambda x: 
        'High Priority' if x <= pd.Timestamp.now() + pd.Timedelta(days=1) else 
        'Medium Priority' if x <= pd.Timestamp.now() + pd.Timedelta(days=7) else 
        'Low Priority'
    )

    return chunk

# Deploy the email prioritization agent
async def deploy():
    # Load the CSV file
    emails = pd.read_csv("data/emails.csv")
    
    # Process the emails in chunks and get the prioritized emails
    prioritized_emails = process_in_chunks(emails)
    
    # Save the prioritized emails to a new CSV file
    prioritized_emails.to_csv('data/prioritized_emails.csv', index=False)
    print("Prioritized emails have been saved to 'data/prioritized_emails.csv'")
    
    # Prevent double printing
    if not hasattr(deploy, "printed_response"):
        # Run the email prioritization agent (printing responses as per your setup)
        EmailAgent.print_response("Analyze the given email CSV file and prioritize emails based on due dates.", stream=True)
        swarm.print_response(COMPANY_CONTEXT)
        deploy.printed_response = True  # Mark the response as printed

if __name__ == "__main__":
    asyncio.run(deploy())
