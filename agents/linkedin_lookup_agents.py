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
    
    prompt_template = PromptTemplate(input_variables=["name_of_person"], template=template)
    
    tools_for_agent=[
        Tool(
            name="Crawl Google for LinekdIn profile page",
            func="?",
            description="useful for when you need to get the LinkedIn Page URL"
        )
    ]
    
    react_prompt = hub.pull("hwchase17/react")
    
    agent=create_react_agent(llm=llm, tools=tools_for_agent,
                             prompt=react_prompt)

    agent_executer=AgentExecutor(agent=agent,tools=tools_for_agent,verbose=True)
    
    result=agent_executer.invoke(
        input={"input":prompt_template.format_prompt(name_of_person=name)}
    )
    
    
    linkedin_profile_url=result["output"]
    
    return linkedin_profile_url