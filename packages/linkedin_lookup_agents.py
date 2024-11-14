
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent, #very powerful
    AgentExecutor
)

from langchain import hub #to download prompts from the community


#from tool.tools import get_profile_url_tavily
from tool.tools import get_profile_url_tavily




#from third_parties.linkedin import scrape_linkedin_profile



def lookup(name:str) -> str:
    llm = ChatOpenAI(temperature=0,
                     model="gpt-4o-mini")
    
    template = """
        given the name {name_of_person} of the person, I want you to get me 
        the link to their LinkedIn profile page.
        your answer should contain only a URL.
        
    """
    
    prompt_template = PromptTemplate(input_variables=["name_of_person"], template=template)
    
    tools_for_agent=[
        Tool(
            #this "name" will be supplied to the reasoning agent and will be used a lot
            name="Crawl Google for LinekdIn profile page", 
            #python function that we want it to run
            func=get_profile_url_tavily,
            #description is very important as LLM will use this to check whether to run this or not
            description="useful for when you need to get the LinkedIn Page URL"
        )
    ]
    
    
    #this is a super powerful prompt which will be the reasoning engine of our code
    react_prompt = hub.pull("hwchase17/react")
    
    agent=create_react_agent(llm=llm, tools=tools_for_agent,
                             prompt=react_prompt)

    agent_executer=AgentExecutor(agent=agent,tools=tools_for_agent,verbose=True)
    
    result=agent_executer.invoke(
        input={"input":prompt_template.format_prompt(name_of_person=name)}
    )
    
    
    linkedin_profile_url=result["output"]
    
    return linkedin_profile_url

if __name__ == "__main__":
    
    linkedin_url = lookup("Parakh Singhal")
    print(linkedin_url)