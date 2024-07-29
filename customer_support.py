import os
import warnings
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool

# Warning control
warnings.filterwarnings('ignore')

# Set up OpenAI API key and model
openai_api_key = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o-mini'

def create_agents():
    # Creating a support agent
    support_agent = Agent(
        role="Senior Support Representative",
        goal="Be the most friendly and helpful support representative in your team",
        backstory=(
            "You work at crewAI (https://crewai.com) and are now working on providing "
            "support to {customer}, a super important customer for your company."
            "You need to make sure that you provide the best support!"
            "Make sure to provide full complete answers, and make no assumptions."
        ),
        allow_delegation=False,
        verbose=True
    )

    # Creating our support QA agent
    support_quality_assurance_agent = Agent(
        role="Support Quality Assurance Specialist",
        goal="Get recognition for providing the best support quality assurance in your team",
        backstory=(
            "You work at crewAI (https://crewai.com) and are now working with your team "
            "on a request from {customer} ensuring that the support representative is "
            "providing the best support possible.\n"
            "You need to make sure that the support representative is providing full"
            "complete answers, and make no assumptions."
        ),
        verbose=True,
        allow_delegation=True
    )

    return support_agent, support_quality_assurance_agent

def create_tasks(support_agent, support_quality_assurance_agent):
    docs_scrape_tool = ScrapeWebsiteTool(
        website_url="https://docs.crewai.com/core-concepts/Crews/#crew-output-methods-and-properties"
    )

    inquiry_resolution = Task(
        description=(
            "{customer} just reached out with a super important ask:\n"
            "{inquiry}\n\n"
            "{person} from {customer} is the one that reached out. "
            "Make sure to use everything you know to provide the best support possible."
            "You must strive to provide a complete and accurate response to the customer's inquiry."
        ),
        expected_output=(
            "A detailed, informative response to the customer's inquiry that addresses "
            "all aspects of their question.\n"
            "The response should include references to everything you used to find the answer, "
            "including external data or solutions. Ensure the answer is complete, "
            "leaving no questions unanswered, and maintain a helpful and friendly tone throughout."
        ),
        tools=[docs_scrape_tool],
        agent=support_agent,
    )

    quality_assurance_review = Task(
        description=(
            "Review the response drafted by the Senior Support Representative for {customer}'s inquiry. "
            "Ensure that the answer is comprehensive, accurate, and adheres to the "
            "high-quality standards expected for customer support.\n"
            "Verify that all parts of the customer's inquiry have been addressed "
            "thoroughly, with a helpful and friendly tone.\n"
            "Check for references and sources used to find the information, "
            "ensuring the response is well-supported and leaves no questions unanswered."
        ),
        expected_output=(
            "A final, detailed, and informative response ready to be sent to the customer.\n"
            "This response should fully address the customer's inquiry, incorporating all "
            "relevant feedback and improvements.\n"
            "Don't be too formal, we are a chill and cool company "
            "but maintain a professional and friendly tone throughout."
        ),
        agent=support_quality_assurance_agent,
    )

    return [inquiry_resolution, quality_assurance_review]

def main():
    support_agent, support_quality_assurance_agent = create_agents()
    tasks = create_tasks(support_agent, support_quality_assurance_agent)

    crew = Crew(
        agents=[support_agent, support_quality_assurance_agent],
        tasks=tasks,
        verbose=2,
        memory=True
    )

    # We need to pass the inputs to override the interpolation variables:
    inputs = {
        "customer": "DeepLearningAI",
        "person": "Andrew Ng",
        "inquiry": "I need help with setting up a Crew "
                   "and kicking it off, specifically "
                   "how can I add memory to my crew? "
                   "Can you provide guidance?"
    }
    result = crew.kickoff(inputs=inputs)
    print(result)

if __name__ == "__main__":
    main()