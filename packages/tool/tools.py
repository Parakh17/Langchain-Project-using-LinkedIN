#Tavily - search API optimised for LLM and RAG
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
load_dotenv()



import linkedin

#import third_parties.linkedin
def get_profile_url_tavily(name:str):
    search = TavilySearchResults()
    res = search.run(f"{name}")
    
    return res[0]["url"]

print("hi")

