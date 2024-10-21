# General Purpose Agents
Select the agents you want to use from the `agents` folder in the .

## Setup
```bash
export OPENAI_API_KEY="sk-..." # or set in .env
python -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```
Choose your agents and instruction for the swarm in `swarm.py`.
The agents are defined in the `agents` folder.
Currently, only OpenAI models are supported.
Generic accounting, marketing, sales agents are included.
```python
COMPANY_CONTEXT = {
    "name": "Acme Inc.",
    "description": "A company that sells widgets.",
    "mission": "To sell widgets to the world.",
}
AGENTS = [copy_writer, strategist, social_media_manager] # add or remove agents as needed
```

## Deploy
Run `python swarm.py` to deploy the agents.
