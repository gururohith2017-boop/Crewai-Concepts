from crewai import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()

researcher = Agent(
    role="Researcher",
    goal="Research a topic and provide clear, useful information",
    backstory="You are an experienced research assistant who finds and organizes information clearly.",
    verbose=True
)

research_task = Task(
    description="Research the benefits of Generative AI in software testing.",
    expected_output="A clear summary of the key benefits of Generative AI in software testing.",
    agent=researcher
)

crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    verbose=True
)

print("Crew created successfully!")

result = crew.kickoff()

print("\n===== FINAL RESULT =====")
print(result)