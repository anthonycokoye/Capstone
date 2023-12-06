import json
import os
import shutil
def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)


data_to_save = \
{
    "Project Location": {
        # -----------------------------------------------------------------------------------------------------------------------
        "Number":
            """10""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Fall""",
    },


    "Project Information": {
        # -----------------------------------------------------------------------------------------------------------------------
        "WB_lead":
            """Soazic Elise Wang Sonne""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """HAWH3""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """KOBIKISA / P167890""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """Djibrilla Karamoko""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """Soazic Elise Wang Sonne, Aubain Lepassa""",
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """Republic of Congo""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """Build a resilience-sensitive Health Facility geotagged prioritization map and empirically assess the nexus between climate change, WASH and health outcomes at
the health facility level""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
government, citizens, world bank
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """Concept note
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
Yes; September 2024
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "lead_meeting":
            """Yes""",
    },


    "Data": {
        # -----------------------------------------------------------------------------------------------------------------------
        "dataset_size":
            """5""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_type":
            """
1. Time series/Panel data
2. Satellite Data
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "data_details":
            """
We have a micro-level geo-coded dataset of health facilities to be combined with various satellite and climate change/ Weather geocoded datasets.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """yes the dataset could be freely made available to the students right away""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """The ultimate goal of this project is to build an interactive digital map of health facilities by highlighting those that are facing the double-burden or dual challenges
of low health system performance due to lack of basic infrastructures and increasing vulnerability to climate change and environmental hazards. The project also
intends to do a thorough empirical assessment of the relationship between extreme weather events (namely heavy rainfall/flooding, and heat stress) and maternal
and children health outcomes at the district and health facility level is key to further understand the nexus between climate change and health in the country.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "additional_comments":
            """The students would be supporting wit these two core tasks:
1) Empirically assess the relationship between extreme weather events due to climate change (namely flooding due to heavy rainfall and heat stress) and maternal
and children health outcomes at the health facility and district level. To achieve this objective, the team intends to use geo-coded and satellite historical seasonal
data (time-series) on climate-related risks and extreme weather events from the World Bank Climate Knowledge portal ; IMF climate data and IPCC data portals
combined with spatial and monthly data on maternal and children health outcomes from the country’s DHIS2 (District Health Information System).
2) Build a resilience-sensitive Health Facility geotagged prioritization map highlighting Primary Health Care centers and hospitals to prioritize based on their overall
health system performance to deliver basic quality health services and their vulnerability risks to climate change. To achieve this objective, the team intends to use
exhaustive geo-coded data from the general evaluation of health facilities concluded in July 2023 combined with geo-spatial and satellite data on climate risks
including flooding and heat stress from the World Bank Climate Knowledge portal ; IMF climate data , IPCC data and the United Nations Satellite Centre
(UNOSAT).""",
    },


        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "World Bank",
        "Proposed by email": "firstname_lastname@worldbank.org",
        "instructor": "Amir Jafari & Edwin Lo",
        "instructor1_email": "ajafari@gmail.com",
        "instructor2_email": "edwinlo@gwu.edu",
        "github_repo": "https://github.com/amir-jafari/Capstone",
        # -----------------------------------------------------------------------------------------------------------------------
}

os.makedirs(os.getcwd() + os.sep + f'Arxiv{os.sep}Proposals{os.sep}{data_to_save["Project Location"]["Year"]}{os.sep}{data_to_save["Project Location"]["Semester"]}{os.sep}World Bank{os.sep}{data_to_save["Project Location"]["Number"]}',exist_ok=True)
output_file_path = os.getcwd() + os.sep + f'Arxiv\Proposals{os.sep}{data_to_save["Project Location"]["Year"]}{os.sep}{data_to_save["Project Location"]["Semester"]}{os.sep}World Bank{os.sep}{data_to_save["Project Location"]["Number"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(os.path.abspath(os.path.join(os.path.dirname(__file__), 'json_gen.py')), output_file_path)
print(f"Data saved to {output_file_path}")