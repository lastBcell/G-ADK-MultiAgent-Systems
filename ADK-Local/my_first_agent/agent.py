from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
import os

# Load variables from the .env file into the environment
load_dotenv()


root_agent = Agent(
    model=os.getenv('MODEL'),
    name='math-tutor-agent',
    description='Help students understand maths problems guiding them through problem solving solution',
    instruction='you are a patient math tutor,helps students with algebraic problems ',
)
