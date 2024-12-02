# CrewAI Example Implementations

This repository contains example Python file implementations of Crews using CrewAI, based on the *first* course from DeepLearning.ai. A newer course has since released going more in-depth into real use-cases for CrewAI. The examples from this first course demonstrate how to create and use AI agent crews for various tasks.

It also includes detailed notes from the DeepLearning.ai course on how to successfully build incredible Multi-Agent systems using the CrewAI framework. You can find those below in this README.

## Table of Contents

1. [Dependencies](#dependencies)
2. [Introduction to CrewAI](#introduction-to-crewai)
3. [Key Concepts](#key-concepts)
4. [Agent Creation Framework](#agent-creation-framework)
5. [Key Elements of Agent Tools](#key-elements-of-agent-tools)
6. [Task Definition](#task-definition)
7. [Multi-Agent Collaboration](#multi-agent-collaboration)
8. [Example Implementations](#example-implementations)
   - [Collaboration on Financial Analysis](#collaboration-on-financial-analysis)
   - [Tailoring Job Applications](#tailoring-job-applications)
   - [Automating Event Planning](#automating-event-planning)
   - [Customer Outreach Campaign](#customer-outreach-campaign)
   - [Technical Articles Creation](#technical-articles-creation)
   - [Customer Support Crew](#customer-support-crew)
9. [Next Steps with AI Agent Systems](#next-steps-with-ai-agent-systems)
10. [Additional Resources](#additional-resources)

## Dependencies

The core dependencies for these examples are listed in the `requirements.txt` file:

## Introduction to CrewAI

CrewAI is a framework for creating and managing crews of AI agents that can work together to accomplish complex tasks. This repository provides practical examples of how to implement such crews using Python.

## Key Concepts

### What Makes an Agent Great?

There are 6 key things that make an agent great:

1. **Research (Data Collection)**: Ability to search online, in internal databases, or other sources. This includes comparison between findings and internal databases.

2. **Role Playing**: Carefully choosing the role, goal, and backstory with appropriate keywords to get better results.

3. **Focus**: The ability to handle the amount of content they receive and the tools they have. This often involves having many agents work together instead of one agent with many responsibilities.

4. **Tools**: Providing the key tools necessary for the job without overloading the agent. It's important to choose tools wisely.

5. **Cooperation**: The ability to take feedback and delegate tasks to each other. Agents should be set up to collaborate effectively.

6. **Guardrails**: Preventing hallucinations, random loops, or repetitive tool usage. Many of these are implemented at the framework level in CrewAI.

### Types of Agent Memory

Agents in CrewAI get three types of memory out of the box:

1. **Short-term memory**: Retains information during the execution of a task.
2. **Shared knowledge**: Allows agents to share information and learnings with other agents.
3. **Long-term memory**: Stores information after task completion for future use, leading to 'self-improving' agents.

## Agent Creation Framework

When creating agents, think like a manager:

1. Define the goal and process clearly.
2. Identify the roles needed to accomplish the task.
3. Create specific and well-defined roles (e.g., "HR Research Specialist" instead of just "Researcher").
4. Consider the backstory and goals for each agent.

## Key Elements of Agent Tools

Tools are crucial for connecting your agents to the external world. They act as a translation layer, allowing agents to communicate with existing programs. To work properly, tools should cover these three key aspects:

1. **Versatility**: Tools should accept different kinds of requests and fuzzy inputs.
2. **Fault-tolerance**: Tools should be able to handle exceptions gracefully.
3. **Caching**: Implement a caching layer to prevent unnecessary API calls or service requests.

## Task Definition

Well-defined tasks are crucial for effective multi-agent systems. When defining tasks, consider the following:

1. **Clear Description**: Explain the task very carefully and in detail.
2. **Clear Expectations**: Set clear and concise expectations for the task outcome.
3. **CrewAI Hyperparameters**: Utilize CrewAI's hyperparameters to fine-tune task execution.

## Multi-Agent Collaboration

Effective collaboration is key to the success of multi-agent systems. Consider these process types:

1. **Sequential**: Agents work one after another in a predetermined order.
2. **Hierarchical**: Involves a manager agent that delegates work to other agents.
3. **Asynchronous**: Agents work independently and simultaneously on different aspects of the task.

## Example Implementations

### Collaboration on Financial Analysis

File: `collaboration_financial_analysis.py`

This implementation demonstrates a crew of AI agents collaborating on financial analysis tasks.

#### Key Components:
1. **Agents**: Data Analyst, Trading Strategy Developer, Trade Advisor, Risk Advisor
2. **Tools**: SerperDevTool, ScrapeWebsiteTool
3. **Tasks**: Analyze Market Data, Develop Trading Strategies, Plan Trade Execution, Assess Trading Risks
4. **Process**: Hierarchical

#### How it works:
1. The crew is initialized with the agents and tasks.
2. The process runs hierarchically, allowing for complex decision-making.
3. The crew analyzes a specific stock based on user-defined parameters.
4. Each agent performs its specialized task, building upon the work of others.
5. The final output includes insights on market opportunities, trading strategies, execution plans, and risk analysis.

### Tailoring Job Applications

File: `tailor_job_applications.py`

This implementation demonstrates how a crew of AI agents can assist in tailoring job applications.

#### Key Components:
1. **Agents**: Tech Job Researcher, Personal Profiler for Engineers, Resume Strategist for Engineers, Engineering Interview Preparer
2. **Tools**: SerperDevTool, ScrapeWebsiteTool, FileReadTool, MDXSearchTool
3. **Tasks**: Extract Job Requirements, Compile Comprehensive Profile, Align Resume with Job Requirements, Develop Interview Materials

#### How it works:
1. The crew is initialized with the agents and tasks.
2. The process starts with analyzing a job posting URL and the applicant's GitHub profile.
3. Each agent performs its specialized task, from researching job requirements to preparing interview materials.
4. The output includes a tailored resume and interview preparation materials.

### Automating Event Planning

File: `automate_event_planning.py`

This implementation demonstrates how a crew of AI agents can automate the process of planning an event.

#### Key Components:
1. **Agents**: Venue Coordinator, Logistics Manager, Marketing and Communications Agent
2. **Tools**: SerperDevTool, ScrapeWebsiteTool
3. **Tasks**: Find and Book Venue, Coordinate Catering and Equipment, Promote the Event
4. **Custom Elements**: VenueDetails (Pydantic model), CustomTask (Extended Task class)

#### How it works:
1. The crew is initialized with the agents and tasks.
2. Each agent performs its specialized task based on the event details provided.
3. The Venue Coordinator outputs structured venue details in JSON format.
4. The Marketing and Communications Agent produces a marketing report in Markdown format.
5. The main function displays the venue details and marketing report after the crew completes its tasks.

### Customer Outreach Campaign

File: `customer_outreach_campaign.py`

This implementation demonstrates how a crew of AI agents can conduct a customer outreach campaign.

#### Key Components:
1. **Agents**: Sales Representative, Lead Sales Representative
2. **Tools**: DirectoryReadTool, FileReadTool, SerperDevTool, SentimentAnalysisTool (custom)
3. **Tasks**: Lead Profiling, Personalized Outreach

#### How it works:
1. The crew is initialized with the agents and tasks.
2. The Sales Representative conducts an in-depth analysis of a lead company.
3. The Lead Sales Representative crafts a personalized outreach campaign based on the lead profile.
4. The process uses a custom SentimentAnalysisTool to ensure positive communication.
5. The crew operates with verbose output and memory enabled for better tracking and context retention.

### Technical Articles Creation

File: `technical_articles.py`

This implementation demonstrates how a crew of AI agents can collaborate to create technical articles.

#### Key Components:
1. **Agents**: Content Planner, Content Writer, Editor
2. **Tasks**: Plan Content, Write Content, Edit Content

#### How it works:
1. The crew is initialized with the agents and tasks.
2. The Content Planner develops a comprehensive content plan for a given topic.
3. The Content Writer uses the plan to craft a blog post.
4. The Editor reviews and refines the blog post for publication.
5. The final output is a well-structured, SEO-optimized blog post in Markdown format.

### Customer Support Crew

File: `customer_support.py`

This implementation demonstrates how a crew of AI agents can handle customer support inquiries effectively.

#### Key Components:
1. **Agents**: 
   - Senior Support Representative
   - Support Quality Assurance Specialist
2. **Tools**: 
   - ScrapeWebsiteTool (for accessing documentation)
3. **Tasks**: 
   - Inquiry Resolution
   - Quality Assurance Review

#### How it works:
1. The crew is initialized with the support agent and quality assurance agent.
2. The Senior Support Representative addresses the customer's inquiry using the available documentation and tools.
3. The Support Quality Assurance Specialist reviews and refines the response to ensure high-quality support.
4. The process uses memory to maintain context throughout the interaction.
5. The final output is a comprehensive, friendly, and accurate response to the customer's inquiry.

This implementation showcases:
- The use of specialized roles for different aspects of customer support
- Integration of documentation scraping for up-to-date information
- A quality assurance process to ensure high-quality responses
- Maintaining a balance between professionalism and a friendly tone

## Next Steps with AI Agent Systems

To further explore and develop AI agent systems, consider the following:

1. **Practical Application**: Apply the concepts to real-world scenarios, such as maximizing interview chances or streamlining business processes.
2. **Explore CrewAI+**: For production deployments, consider using CrewAI+ which offers features like API deployment and secure hosting.
3. **Study Relevant Research**: Dive into papers on role-playing and agent collaboration to deepen your understanding of multi-agent systems.
4. **Dive into the Code**: Explore the CrewAI Github repository to understand the underlying mechanisms of the framework.

## Additional Resources

1. CrewAI Documentation: [\[Link to documentation\]](https://docs.crewai.com/)
2. CrewAI Custom GPT: A tool for writing CrewAI code and accessing CrewAI documents
3. Discord Community: Join for support and discussions with other CrewAI users
4. Research papers on role-playing and agent collaboration
5. ChatDev paper on complex problem-solving through agent communication

This README provides an overview of the key concepts and techniques learned from the CrewAI course, along with practical examples of their implementation. For more detailed information and hands-on experience, refer to the example implementations in this repository and explore the additional resources provided.
