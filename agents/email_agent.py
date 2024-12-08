from phi.agent import Agent
from phi.model.openai import OpenAIChat
from pathlib import Path
from phi.tools.csv_tools import CsvTools
from config import MODEL
import pandas as pd

# Path to the email CSV file
email_csv = Path("./data/emails.csv")
# Path for the new prioritized emails file
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

# Optionally save the prioritized emails manually
def save_prioritized_emails():
    # Sample query logic for demonstration
    # Replace with the actual logic if needed
    emails = pd.read_csv(email_csv)

    # Ensure 'Due Date' is in datetime format
    emails['Due Date'] = pd.to_datetime(emails['Due Date'])

    # Assign priorities
    today = pd.Timestamp.today()
    emails["Priority"] = emails["Due Date"].apply(
        lambda due_date: "High Priority" if pd.Timestamp(due_date) < today + pd.Timedelta(days=1)
        else "Medium Priority" if pd.Timestamp(due_date) < today + pd.Timedelta(days=7)
        else "Low Priority"
    )

    # Save to a new CSV file
    emails.to_csv(prioritized_emails_csv, index=False)
    print(f"Prioritized emails saved to {prioritized_emails_csv}")

if __name__ == "__main__":
    # Run debugging or save prioritized emails manually
    save_prioritized_emails()

