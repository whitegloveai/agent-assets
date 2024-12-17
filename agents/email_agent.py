from phi.agent import Agent
from phi.model.openai import OpenAIChat
from pathlib import Path
from phi.tools.csv_tools import CsvTools
import pandas as pd
from config import MODEL

# Paths to CSV files
email_csv = Path("./data/emails.csv")
prioritized_emails_csv = Path("./data/prioritized_emails.csv")

# Define the email prioritization agent
EmailAgent = Agent(
    tools=[CsvTools(csvs=[email_csv])],
    model=OpenAIChat(id=MODEL),
    name="Email Prioritization Agent",
    role="An assistant that prioritizes and reorganizes emails based on due dates.",
    show_tool_calls=True,
    instructions=[
        "List all available files.",
        "Check the columns in the email CSV file.",
        "Sort all emails by their due dates in ascending order.",
        "Categorize emails into 'High Priority', 'Medium Priority', and 'Low Priority' based on the proximity to the due date:",
        "  - High Priority: Emails due within 1 day.",
        "  - Medium Priority: Emails due within the next 7 days.",
        "  - Low Priority: Emails due in more than 7 days.",
        "Output a complete list of all emails with their assigned priority in a table.",
        "Ensure the table includes columns for 'Subject', 'Body', 'Sender', 'Received Date', 'Due Date', and 'Priority'.",
        "Save the reorganized data into a new CSV file named 'prioritized_emails.csv' in the data folder.",
    ],
)

# Functions for processing emails
def process_in_chunks(df, chunk_size=50):
    total_emails = len(df)
    all_prioritized_emails = []
    for i in range(0, total_emails, chunk_size):
        chunk = df.iloc[i:i+chunk_size]
        prioritized_chunk = process_chunk(chunk)
        all_prioritized_emails.append(prioritized_chunk)
    prioritized_df = pd.concat(all_prioritized_emails, ignore_index=True)
    return prioritized_df.sort_values(by='Due Date', ascending=True).reset_index(drop=True)

def process_chunk(chunk):
    chunk['Due Date'] = pd.to_datetime(chunk['Due Date'], errors='coerce')
    chunk['Priority'] = chunk['Due Date'].apply(lambda x: 
        'High Priority' if pd.notnull(x) and x <= pd.Timestamp.now() + pd.Timedelta(days=1) else
        'Medium Priority' if pd.notnull(x) and x <= pd.Timestamp.now() + pd.Timedelta(days=7) else
        'Low Priority')
    return chunk

def save_prioritized_emails():
    try:
        print("Loading the email CSV file...")
        emails = pd.read_csv(email_csv)
        if emails.empty:
            print("The provided CSV file is empty. Please upload a valid email CSV file.")
            return
        print("Processing emails in chunks...")
        prioritized_emails = process_in_chunks(emails)
        print("Saving prioritized emails...")
        prioritized_emails.to_csv(prioritized_emails_csv, index=False)
        print(f"Prioritized emails saved to {prioritized_emails_csv}")
    except FileNotFoundError:
        print(f"Error: The file {email_csv} was not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Starting email prioritization...")
    save_prioritized_emails()
    print("Email prioritization complete.")


# from phi.agent import Agent
# from phi.model.openai import OpenAIChat
# from pathlib import Path
# from phi.tools.csv_tools import CsvTools
# from config import MODEL
# import pandas as pd

# # Path to the email CSV file
# email_csv = Path("./data/emails.csv")
# # Path for the new prioritized emails file
# prioritized_emails_csv = Path("./data/prioritized_emails.csv")

# # Define the email prioritization agent
# EmailAgent = Agent(
#     tools=[CsvTools(csvs=[email_csv])],
#     model=OpenAIChat(id=MODEL),
#     name="Email Prioritization Agent",
#     role="An assistant that prioritizes and reorganizes emails based on due dates.",
#     show_tool_calls=True,
#     instructions=[
#         "List all available files.",
#         "Check the columns in the email CSV file.",
#         "Sort all emails by their due dates in ascending order.",
#         "Categorize emails into 'High Priority', 'Medium Priority', and 'Low Priority' based on the proximity to the due date:",
#         "  - High Priority: Emails due within 1 day.",
#         "  - Medium Priority: Emails due within the next 7 days.",
#         "  - Low Priority: Emails due in more than 7 days.",
#         "Output a complete list of all emails with their assigned priority in a table.",
#         "Ensure the table includes columns for 'Subject', 'Body', 'Sender', 'Received Date', 'Due Date', and 'Priority'.",
#         "Save the reorganized data into a new CSV file named 'prioritized_emails.csv' in the data folder.",
#     ],
# )

# # Optionally save the prioritized emails manually
# def save_prioritized_emails():
#     # Sample query logic for demonstration
#     # Replace with the actual logic if needed
#     emails = pd.read_csv(email_csv)

#     # Ensure 'Due Date' is in datetime format
#     emails['Due Date'] = pd.to_datetime(emails['Due Date'])

#     # Assign priorities
#     today = pd.Timestamp.today()
#     emails["Priority"] = emails["Due Date"].apply(
#         lambda due_date: "High Priority" if pd.Timestamp(due_date) < today + pd.Timedelta(days=1)
#         else "Medium Priority" if pd.Timestamp(due_date) < today + pd.Timedelta(days=7)
#         else "Low Priority"
#     )

#     # Save to a new CSV file
#     emails.to_csv(prioritized_emails_csv, index=False)
#     print(f"Prioritized emails saved to {prioritized_emails_csv}")

# if __name__ == "__main__":
#     # Run debugging or save prioritized emails manually
#     save_prioritized_emails()

