# Focus Group Transcript Analysis with CrewAI

## Project Objective

This project demonstrates the power of the CrewAI framework in assisting market researchers with rapid and efficient analysis of focus group transcripts. By leveraging multiple AI agents, each specialized in different aspects of the analysis process, I showcase how complex tasks can be broken down, processed, and synthesized into actionable insights.

The primary objectives of this project are:

1. To illustrate how CrewAI can be used to automate and streamline the focus group analysis workflow.
2. To demonstrate the effectiveness of using multiple specialized agents for different stages of the analysis process.
3. To showcase the ability to generate comprehensive, well-structured reports from raw focus group transcripts.

This approach can significantly reduce the time and effort required for qualitative data analysis, allowing researchers to focus on strategic decision-making rather than time-consuming manual analysis.

## Project Structure

The project consists of several key components:

1. Configuration files (`agents.yaml` and `tasks.yaml`)
2. Python scripts (`crew.py` and `main.py`)
3. Input files (focus group objectives and transcript)
4. Output file (final report)

## Code Walkthrough

### Configuration Files

The `agents.yaml` and `tasks.yaml` files define the roles, characteristics, and tasks of our AI agents. For detailed content, see the respective code snippets below.

summarizer:
  role: >
    Focus Group Transcript Condenser
  goal: >
    Create accurate, concise, and objective summaries of focus group 
    transcripts, capturing key themes and diverse viewpoints while maintaining 
    chronological integrity
  backstory: >
    You are a specialized Focus Group Transcript Summarizer with 
    a remarkable talent for distilling lengthy discussions into clear, concise 
    summaries. Your expertise lies in capturing the essence of focus group 
    conversations without losing critical details.

analyst:
  role: >
    Focus Group Insights Analyst
  goal: >
    Analyze condensed focus group transcripts in the context of research 
    objectives to extract actionable insights and meaningful patterns.
  backstory: >
    You are an expert Focus Group Insights Analyst with a keen eye for 
    uncovering valuable patterns and insights from qualitative data. Your analytical 
    skills are honed to interpret condensed focus group transcripts within the framework 
    of specific research objectives.

report_writer:
  role: >
    Focus Group Insights Report Writer
  goal: >
    Transform analytical insights into a comprehensive, well-structured, 
    and persuasive report that effectively communicates focus group findings, 
    insights, and actionable recommendations to stakeholders.
  backstory: >
    You are a highly skilled Focus Group Insights Report Writer with 
    a talent for translating complex analytical findings into clear, compelling 
    narratives. Your expertise lies in crafting reports that not only present data 
    and insights but tell a coherent story that resonates with diverse stakeholders.

### Python Scripts

#### crew.py

This script sets up the CrewAI environment and defines the agents and tasks. See the `crew-py` code snippet for details.

#### main.py

This simple script runs the entire process. See the `main-py` code snippet for details.

## Project Output

The final output of this project is a comprehensive markdown report (`final_fg_report.md`) that provides a detailed analysis of the focus group discussion. An excerpt from the report is available in the `final-report-excerpt` code snippet.

This output demonstrates the power of using CrewAI for focus group analysis. The AI agents have successfully condensed hours of discussion into a clear, actionable report that can guide business decisions and marketing strategies.

By leveraging this automated approach, market researchers can significantly reduce the time and effort required for qualitative data analysis, allowing them to focus on strategic interpretation and implementation of insights.

## Code Snippets

See the code snippets below for detailed implementation of key components:

- `agents-yaml`: Configuration of AI agents
- `tasks-yaml`: Definition of tasks for each agent
- `crew-py`: Main CrewAI setup and execution
- `main-py`: Entry point for running the analysis
- `final-report-excerpt`: Sample output from the AI-generated report
