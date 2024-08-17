from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="crewai-llama3.1:8b")

    # def __init__(self):
    #     # self.llm = ChatGroq(
    #     #    api_key=os.getenv("GROQ_API_KEY"),
    #     #    model="llama3-70b-8192"
    #     # )
    #    self.llm = ChatOpenAI(
    #          model="crewai-llama3.1:8b",
    #         base_url="http://localhost:11434/v1",
    #         api_key="NA"
    #      )

    def reader_agent(self):
        return Agent(
            role="Firm Name Reader",
            backstory=dedent(f"""You are responsible for reading and extracting the names of firms from a given list."""),
            goal=dedent(f"""Extract and pass firm names to the Researcher Agent"""),
            # tools=[SearchTools.search_internet],
            allow_delegation=False,
            memory=True,
            verbose=True,
            llm=self.Ollama,
        )

    def researcher_agent(self):
        return Agent(
            role="Firm Researcher",
            backstory=dedent(f"""You are an expert in finding information online. Your role is to gather detailed information about the firms."""),
            goal=dedent(f"""Search the internet for information about the firm"""),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            memory=True,
            verbose=True,
            llm=self.Ollama,
        )
    
    def analyst_agent(self):
        return Agent(
            role="Firm Analyst",
            backstory=dedent(f""""You analyze data to determine whether a firm is private or state-owned. "
        "You also identify their primary business activities."""),
            goal=dedent(f"""Determine ownership type (private/state) and main line of business"""),
            # tools=[SearchTools.search_internet],
            allow_delegation=False,
            memory=True,
            verbose=True,
            llm=self.Ollama,
        )