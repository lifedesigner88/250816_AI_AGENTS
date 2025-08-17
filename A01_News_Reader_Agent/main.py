import dotenv

dotenv.load_dotenv() # 환경변수 세팅


from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from tools import count_letters

@CrewBase
class TrnslatorCrew:

    @agent
    def translator_agent(self):
        return Agent(
            config=self.agents_config["translator_agent"]
        )

    @agent
    def counter_agent(self):
        return Agent(
            config=self.agents_config["counter_agent"],
            tools=[count_letters]
        )

    @task
    def translate_task(self):
        return Task(
            config=self.tasks_config["translate_task"]
        )

    @task
    def retranslate_task(self):
        return Task(
            config=self.tasks_config["retranslate_task"]
        )

    @task
    def reretranslate_task(self):
        return Task(
            config=self.tasks_config["reretranslate_task"]
        )

    @task
    def count_task(self):
        return Task(
            config=self.tasks_config["count_task"],
        )

    @crew
    def assemble_crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True
        )

TrnslatorCrew().assemble_crew().kickoff(
    inputs={
        "sentence" : "I'm Nico I like to ried my bicicle in Napoli"
    }
)