import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, MDXSearchTool
from langchain_openai import ChatOpenAI
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Construct full file paths
transcript_path = os.path.join(script_dir, 'white-strawberry-focus-group-transcript.md')
objectives_path = os.path.join(script_dir, 'white-strawberry-focus-group-objectives.md')

# FileReadTool allows the agent to read a specific file
read_transcript = FileReadTool(file_path=transcript_path)
read_fg_objectives = FileReadTool(file_path=objectives_path)

# MDXSearchTool allows us to perform RAG over our mock focus group transcripts
search_transcript = MDXSearchTool(mdx=transcript_path)


@CrewBase
class FgTranscriptAnalyzerCrew():
	"""FgTranscriptAnalyzer crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self) -> None:
		self.OpenAIGPT35 = ChatOpenAI(
			model_name="gpt-3.5-turbo", 
			temperature=0)
		
		self.OpenAIGPT4o = ChatOpenAI(
			model_name="gpt-4o", 
			temperature=0)

	@agent
	def summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['summarizer'],
			tools=[read_transcript, search_transcript], 
			allow_delegation=False,
			llm=self.OpenAIGPT4o,
			verbose=True
		)

	@agent
	def analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['analyst'],
			tools=[read_fg_objectives], 
			allow_delegation=False,
			llm=self.OpenAIGPT4o,
			verbose=True
		)
	
	@agent
	def report_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['report_writer'],
			tools=[read_fg_objectives], 
			allow_delegation=False,
			llm=self.OpenAIGPT4o,
			verbose=True
		)

	@task
	def summarize_task(self) -> Task:
		return Task(
			config=self.tasks_config['summarize_task'],
			agent=self.summarizer()
		)

	@task
	def analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['analysis_task'],
			agent=self.analyst(),
		)
	
	@task
	def report_writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['report_writing_task'],
			agent=self.report_writer(),
			output_file="final_fg_report.md"
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the FgTranscriptAnalyzer crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			memory=True
		)