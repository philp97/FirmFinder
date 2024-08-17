import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
#from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

from crewai import Crew
# from textwrap import dedent
# from agents import TravelAgents
# from tasks import TravelTasks

from dotenv import load_dotenv
load_dotenv()


# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self, var1):
        self.var1 = var1
        # self.var2 = var2

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        reader = agents.reader_agent()
        researcher = agents.researcher_agent()
        analysy = agents.analyst_agent()

        # Custom tasks include agent name and variables as input
        read_firms_task = tasks.read_firms_task(
            reader,
            self.var1
        )

        search_firms_task = tasks.search_firms_task(
            researcher
        )

        analyze_firms_task = tasks.analyze_firms_task(
            analysy
        )

        # Define your custom crew here
        crew = Crew(
            agents=[reader, researcher, analysy],
            tasks=[read_firms_task, search_firms_task,analyze_firms_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""Enter List of Firms: """))
    # var2 = input(dedent("""Enter variable 2: """))

    custom_crew = CustomCrew(var1)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)