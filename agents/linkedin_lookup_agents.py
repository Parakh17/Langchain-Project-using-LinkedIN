from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)

from langchain import hub


def lookup(name:str) -> str:
    llm = ChatOpenAI(temperature=0,
                     model="gpt-3.5-turbo")
    
    template = """
        given the name {name_of_person} of the person, I want you to get me the link to their linkedin profile page.
        your answer should contain only a URL.
        
    """
    
    prompt_template = PromptTemplate