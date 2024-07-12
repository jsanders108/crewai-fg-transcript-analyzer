# CrewAI Focus Group Transcript Analyzer

## Project Objective

I developed this project to demonstrate the power of the CrewAI framework in assisting market researchers with challenging tasks such as summarizing and analyzing focus group transcripts. By leveraging multiple AI agents working in concert, I showcase how complex analytical tasks can be completed quickly and efficiently.

The primary goals of this project are:

1. To automate the process of summarizing focus group transcripts
2. To perform in-depth analysis of the summarized content
3. To generate a comprehensive report with actionable insights

By achieving these objectives, I illustrate how CrewAI can significantly enhance the productivity and effectiveness of market research processes.

## Code Walkthrough

In this project, I utilized the latest version of CrewAI, showcasing its updated features and syntax. Let's break down the key components of my implementation:

### 1. Agent Configuration (agents.yaml)

I defined the roles and responsibilities of the AI agents in the `agents.yaml` file:

```yaml
summarizer:
  role: Focus Group Transcript Condenser
  goal: Create accurate, concise, and objective summaries of focus group transcripts...

analyst:
  role: Focus Group Insights Analyst
  goal: Analyze condensed focus group transcripts in the context of research objectives...

report_writer:
  role: Focus Group Insights Report Writer
  goal: Transform analytical insights into a comprehensive, well-structured, and persuasive report...
```

I assigned each agent a specific role in the analysis process, ensuring a clear division of labor and expertise.

### 2. Task Definition (tasks.yaml)

I outlined the specific tasks for each agent to perform in the `tasks.yaml` file:

```yaml
summarize_task:
  description: Read the provided focus group transcripts and create a comprehensive summary...

analysis_task:
  description: Analyze the summary of the focus group transcripts provided by the Summarizer Agent...

report_writing_task:
  description: Using the comprehensive analysis provided by the Analyst Agent, create a polished, well-structured markdown report...
```

These task definitions guide the agents through the process of transforming raw transcript data into actionable insights.

### 3. Crew Assembly (crew.py)

The `crew.py` file is the heart of my CrewAI implementation, where I assembled the team of AI agents:

```python
@CrewBase
class FgTranscriptAnalyzerCrew():
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

    # ... [similar methods for analyst and report_writer]

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=2,
            memory=True
        )
```

In this class, I set up the agents with their respective configurations and tools, and assembled them into a crew that works sequentially to complete the analysis.

### 4. Execution (main.py)

Finally, I created a `main.py` file to kick off the entire process:

```python
#!/usr/bin/env python
from fg_transcript_analyzer.crew import FgTranscriptAnalyzerCrew

def run():   
    FgTranscriptAnalyzerCrew().crew().kickoff()
    
if __name__ == "__main__":
    run()
```

This simple script creates an instance of the `FgTranscriptAnalyzerCrew` and initiates the analysis process.

## Output Showcase

The culmination of the AI agents' work is a comprehensive markdown report (`final_fg_report.md`) that provides valuable insights from the focus group discussion. Here's a glimpse of what the report contains:

1. Executive Summary
2. Introduction (including background and objectives)
3. Key Findings
4. Analysis of patterns and trends
5. Recommendations
6. Conclusions and Next Steps

This report demonstrates the power of CrewAI in distilling complex qualitative data into actionable insights, showcasing how AI can augment and accelerate the market research process.

## Conclusion

Through this project, I've provided a compelling example of how CrewAI can be leveraged to streamline and enhance market research processes. By automating the tedious tasks of transcript summarization and preliminary analysis, researchers can focus their efforts on deeper interpretation and strategy development.

The modular nature of the CrewAI framework allows for easy adaptation to various research scenarios, making it a valuable tool for any organization looking to gain deeper insights from qualitative data more efficiently.

