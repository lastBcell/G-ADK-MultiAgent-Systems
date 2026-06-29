from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
import os

# Load variables from the .env file into the environment
load_dotenv()


root_agent = Agent(
    model=os.getenv('MODEL'),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
