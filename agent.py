# agent.py

from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import Tool
from dotenv import load_dotenv
import os
from agent_tools import CheckETHBalance, SendETH

load_dotenv()

# Initialize the OpenAI LLM (or switch to another LLM)
llm = ChatOpenAI(
    temperature=0.3,
    model="gpt-3.5-turbo",  # Update if you’re using GPT-4
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Register available tools
tools = [CheckETHBalance, SendETH]

# Initialize Langchain Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

def handle_prompt(prompt: str) -> str:
    """Passes user prompt to the Langchain agent and returns the response."""
    try:
        return agent.invoke(prompt)
    except Exception as e:
        return f"❌ Agent error: {e}"
