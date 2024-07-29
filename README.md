# CrewAI Example Crews

This repository contains example crews built based on the notebooks from the DeepLearning.ai Course on Multi-Agent Systems with CrewAI. These examples demonstrate various use cases and implementations of CrewAI for different scenarios.

## Files in this Repository

1. `technical_articles.py`: This script demonstrates a crew for creating technical articles. It includes agents for planning, writing, and editing content.

2. `customer_outreach_campaign.py`: This script showcases a crew designed for customer outreach campaigns. It includes agents for lead profiling and personalized outreach.

3. `customer_support.py`: This script illustrates a crew for handling customer support inquiries. It includes agents for support representation and quality assurance.

4. `instructions/enterprise_solutions_framework.md`: This markdown file provides guidelines for engaging with enterprise clients, focusing on strategic partnerships and innovation.

5. `instructions/small_business_engagement.md`: This markdown file offers guidance for engaging with small businesses, emphasizing personalization and efficiency.

6. `instructions/tech_startups_outreach.md`: This markdown file provides instructions for reaching out to tech startups, highlighting innovation and scalability.

7. `requirements.txt`: This file lists the core dependencies required to run the CrewAI examples in this repository.

## Dependencies

The core dependencies for these examples are listed in the `requirements.txt` file:

```
crewai==0.41.1
crewai-tools==0.4.26
langchain-community==0.2.10
```

To install these dependencies, run:

```
pip install -r requirements.txt
```

## Usage

Each Python script (`technical_articles.py`, `customer_outreach_campaign.py`, and `customer_support.py`) can be run independently to demonstrate different CrewAI implementations. Make sure you have installed the necessary dependencies from the `requirements.txt` file and set up the required API keys in your environment variables.

The markdown files in the `instructions` directory provide additional context and templates for specific outreach scenarios, which are utilized by some of the crews in their tasks.

## Note

These examples are based on the DeepLearning.ai Course on Multi-Agent Systems with CrewAI. They serve as practical demonstrations of how to implement CrewAI for various business processes and can be used as a starting point for building your own custom crews.

For more information on CrewAI and its capabilities, please refer to the official CrewAI documentation.