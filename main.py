from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="openrouter/anthropic/claude-haiku-4-5",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

researcher = Agent(
    role="Исследователь",
    goal="Найти и собрать информацию по теме",
    backstory="Ты опытный аналитик, который умеет собирать и структурировать информацию",
    llm=llm,
    verbose=True
)

writer = Agent(
    role="Писатель",
    goal="Написать понятный текст на основе исследования",
    backstory="Ты опытный копирайтер, который пишет чётко и по делу",
    llm=llm,
    verbose=True
)

research_task = Task(
    description="Изучи тему: что такое искусственный интеллект и как он меняет бизнес",
    expected_output="Структурированный список из 5 ключевых фактов",
    agent=researcher
)

write_task = Task(
    description="На основе исследования напиши короткую статью для бизнесмена",
    expected_output="Статья 150-200 слов на русском языке",
    agent=writer
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=True
)

result = crew.kickoff()
print("\n=== РЕЗУЛЬТАТ ===")
print(result)