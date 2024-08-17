from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def read_firms_task(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Read the list of firms and pass them to the Researcher Agent
            
            {self.__tip_section()}
    
            
            Use this list: {var1}
        """
            ),
            agent=agent,
            expected_output="""A list of firm names.
            Example Output: Tesla, Banco do Brasil"""
        )

    def search_firms_task(self, agent):
        return Task(
            description=dedent(
                f"""
            Take the input from previous agent and Search the internet for information on each firm.
                                       
            {self.__tip_section()}

            
        """
            ),
            agent=agent,
            expected_output="""Raw data about each firm's ownership and business."""
        )
    
    def analyze_firms_task(self, agent):
        return Task(
            description=dedent(
                f"""
            Take the input from previous agent and Analyze the search results to determine whether each firm is private or state-owned
            "and summarize their main line of business."
                                       
            {self.__tip_section()}

            
        """
            ),
            agent=agent,
            expected_output="""Classification of firms and a summary of their main business.
            Example Output: Tesla,Private,Technology\n
            Banco do Brasil,State,Bank"""
        )