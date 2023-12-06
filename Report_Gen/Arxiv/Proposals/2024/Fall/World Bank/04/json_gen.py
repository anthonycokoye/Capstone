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
            """04""",
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
            """Megersa Abate""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """Global Unit Transport""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """P179939""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """Charles Kunaka""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """Kisanet Haile Molla""",
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """Africa""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """The Transport Global Knowledge Unit is building a freight transport model to inform its investment prioritization and planning decision and respond to growing
global challenges such as decarbonization, food transportation and logistics. The modeling work aims to provide a fresh, independent, and comprehensive view of
connectivity needs of client countries in these regions and their decision-making processes. It draws upon and seeks to integrate existing work that the World
Bank and other stakeholders have carried out on infrastructure and logistics connectivity and propose a purely technical approach to support the coordination and
prioritization of projects.
The objective of the assignment is to update and continue further development of the transport model (FLOWMAX) and lay the ground for the detailed modelling
that needs to be carried out to identify and prioritize investments in trade and transport corridors linking parts of the MENA, SAR, North/East Africa and ECA to
their main trade partners. It is also aims to apply FLOWMAX to assess the nexus of transport and food and fertilizer systems in Sub-Sharan Africa by defining a
transport connectivity and logistics infrastructure improvement program to strengthen the resilience of food and fertilizer systems in Sub-Saharan Africa (SSA).""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
Bank staff, policy makers in client countries and their citizens.
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """Implementation n
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
project ending in FY24, but with possibility of extension
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "lead_meeting":
            """Yes""",
    },


    "Data": {
        # -----------------------------------------------------------------------------------------------------------------------
        "dataset_size":
            """100 GB""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_type":
            """
1. Text
2. Image
3. Time series/Panel data
4. Tabular
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "data_details":
            """
transport flows between regions, border crossing points
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """not at the movement.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """building a well functioning transport model""",
        # -----------------------------------------------------------------------------------------------------------------------
        "additional_comments":
            """NA""",
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