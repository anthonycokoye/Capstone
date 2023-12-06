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
            """03""",
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
            """Muneeza Alam""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """MENA Transport Global Practice""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """REGIONAL RAILWAY CONNECTIVITY IN MENA: BETWEEN GCC AND MASHREQ COUNTRIES AND BEYOND (P178510)""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """
Nobu Daito
Roger Gorham
Joanna Moody
Robin Carruthers
            """,
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """Middle East and North Africa""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """Assess the demand potential for high- and medium- speed passenger railways""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
The primary beneficiaries will be the transport ministries of countries in the Middle East and North Africa. High Speed and Medium Speed Railways are a new but potentially growing line of business in MNA. Many countries in the region are already building or have announced plans to build High Speed Railways . In the next five years, we expect countries in MENA to approach the WB for advice and support in the future Therefore, undertaking this activity will yield significant benefits in the future. The ASA is also expected to yield tangible benefits for the current pipeline portfolio and will inform the ongoing operational engagement. By examining the potential for HSRs, the ASA will contribute to ongoing Bank-financed investments supporting economic corridor development, with a long-term view of transforming MENA into a preeminent connectivity node.
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """We want to undertake some exploratory analysis to estimate the demand potential for high and medium speed railways in MENA.\ We want to estimate a gravity model to address the following questions:\ 1. Would High Speed or Medium Speed railways provide a competitive alternative within the MNA region that can shift travel away from more polluting modes, like air and road?\ 2. Under what circumstances (for example, pricing regimes) and on what routes would HSR or conventional railways have the most potential demand/ridership?\ We have access to aviation data that would be useful for this work and many other datasets.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
The exploratory work needs to be completed by end of December 2023. The eventual goal is that this model would become a Working Paper in the World Bank Working Paper Series.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "lead_meeting":
            """Yes""",
    },


    "Data": {
        # -----------------------------------------------------------------------------------------------------------------------
        "dataset_size":
            """1-5 GB""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_type":
            """
1. Tabular
2. We have different datasets that will be used. All of them are quantitate in nature. Geospatial elements will also be important.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "data_details":
            """
1. Aviation data (OAG-Official Airline Guide: the Official Airline Guide (OAG) is an air travel intelligence reference that provides data on airline schedules, cargo and aviation analytics)
2. Population data from WorldPop)
3. Data on AADT by highway sections
4. Border crossing data for cars
5. Proposed alignment of regional railways indicating which cities will be connected by highspeed and mediumspeed railways.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """The ultimate goal of the project is to assess how much modal shift from air transport and road transport) could be attracted to high and medium speed railways if 
            they were built in the Middle East and North Africa Region.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "additional_comments":
            """Nothing to be noted.""",
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