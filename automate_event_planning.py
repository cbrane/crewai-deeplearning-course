import os
import warnings
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from pydantic import BaseModel
from IPython.display import Markdown
import json
from pprint import pprint
from crewai import Task as BaseTask

# Warning control
warnings.filterwarnings('ignore')

# Set up OpenAI API key and model & Serper API Key
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o'
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

class VenueDetails(BaseModel):
    name: str
    address: str
    capacity: int
    booking_status: str

def create_agents():
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    
    venue_coordinator = Agent(
        role="Venue Coordinator",
        goal="Identify and book an appropriate venue based on event requirements",
        tools=[search_tool, scrape_tool],
        verbose=True,
        backstory="With a keen sense of space and understanding of event logistics, you excel at finding and securing the perfect venue that fits the event's theme, size, and budget constraints."
    )
    
    logistics_manager = Agent(
        role='Logistics Manager',
        goal="Manage all logistics for the event including catering and equipment",
        tools=[search_tool, scrape_tool],
        verbose=True,
        backstory="Organized and detail-oriented, you ensure that every logistical aspect of the event from catering to equipment setup is flawlessly executed to create a seamless experience."
    )
    
    marketing_communications_agent = Agent(
        role="Marketing and Communications Agent",
        goal="Effectively market the event and communicate with participants",
        tools=[search_tool, scrape_tool],
        verbose=True,
        backstory="Creative and communicative, you craft compelling messages and engage with potential attendees to maximize event exposure and participation."
    )
    
    return venue_coordinator, logistics_manager, marketing_communications_agent

class CustomTask(BaseTask):
    def _save_file(self, result):
        if self.output_file:
            directory = os.path.dirname(self.output_file)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            
            with open(self.output_file, "w", encoding="utf-8") as file:
                if isinstance(result, dict):
                    json.dump(result, file, indent=2)
                elif isinstance(result, str):
                    file.write(result)
                else:
                    file.write(str(result))

def create_tasks(venue_coordinator, logistics_manager, marketing_communications_agent):
    venue_task = CustomTask(
        description="Find a venue in {event_city} that meets criteria for {event_topic}.",
        expected_output="All the details of a specifically chosen venue you found to accommodate the event.",
        human_input=True,
        output_json=VenueDetails,
        output_file="venue_details.json",
        agent=venue_coordinator
    )
    
    logistics_task = CustomTask(
        description="Coordinate catering and equipment for an event with {expected_participants} participants on {tentative_date}.",
        expected_output="Confirmation of all logistics arrangements including catering and equipment setup.",
        human_input=True,
        async_execution=True,
        agent=logistics_manager
    )
    
    marketing_task = CustomTask(
        description="Promote the {event_topic} aiming to engage at least {expected_participants} potential attendees.",
        expected_output="Report on marketing activities and attendee engagement formatted as markdown.",
        output_file="marketing_report.md",
        agent=marketing_communications_agent
    )
    
    return venue_task, logistics_task, marketing_task

def main():
    venue_coordinator, logistics_manager, marketing_communications_agent = create_agents()
    venue_task, logistics_task, marketing_task = create_tasks(venue_coordinator, logistics_manager, marketing_communications_agent)
    
    event_management_crew = Crew(
        agents=[venue_coordinator, logistics_manager, marketing_communications_agent],
        tasks=[venue_task, logistics_task, marketing_task],
        verbose=True
    )
    
    event_details = {
        'event_topic': "Tech Innovation Conference",
        'event_description': "A gathering of tech innovators and industry leaders to explore future technologies.",
        'event_city': "San Francisco",
        'tentative_date': "2024-09-15",
        'expected_participants': 500,
        'budget': 20000,
        'venue_type': "Conference Hall"
    }
    
    result = event_management_crew.kickoff(inputs=event_details)
    
    # Display venue details
    try:
        with open('venue_details.json', 'r') as f:
            venue_data = json.load(f)
        print("Venue Details:")
        pprint(venue_data)
    except FileNotFoundError:
        print("Venue details file not found.")
    except json.JSONDecodeError:
        print("Error decoding venue details JSON.")
    
    # Display marketing report
    try:
        with open('marketing_report.md', 'r') as f:
            marketing_report = f.read()
        print("\nMarketing Report:")
        print(marketing_report)  # Print the content directly
    except FileNotFoundError:
        print("Marketing report file not found.")

if __name__ == "__main__":
    main()