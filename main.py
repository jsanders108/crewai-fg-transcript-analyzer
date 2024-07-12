#!/usr/bin/env python
from fg_transcript_analyzer.crew import FgTranscriptAnalyzerCrew


def run():   
    FgTranscriptAnalyzerCrew().crew().kickoff()
    

if __name__ == "__main__":
    run()