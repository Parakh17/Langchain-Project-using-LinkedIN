from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    load_dotenv()
    
    summary_template = """
        given the linkedin profile information {information} about a person, I want you to create:
            1. A short summary
            2. two interesting facts about them 
            
        and output them in a json format with key as:
        key 1 - short_summary
        key 2 - facts
    
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    
    
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    
    chain = LLMChain(llm =llm, prompt = summary_prompt_template)
    
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json"
    )
    
    res = chain.invoke(input={"information":linkedin_data})
    print(res)