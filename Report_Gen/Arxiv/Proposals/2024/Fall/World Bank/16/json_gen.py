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
            """16""",
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
            """William Seitz""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """EAP Poverty and Equity""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Indonesia Poverty and Equity Program (P181107)""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """Ririn Salwa Purnamasari; Samuel Nursamsu; Bambang Suharnoko Sjahrir; Imam Setiawan; Cigdem Celik.""",
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """Indonesia
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """Spatial transformation and connectivity flagship report.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
The people of Indonesia
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """In preparatory stage (all data are available).
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
Preparatory stage through June 2024.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "lead_meeting":
            """Yes""",
    },


    "Data": {
        # -----------------------------------------------------------------------------------------------------------------------
        "dataset_size":
            """There are several datasets that will be used including AIS (shipping transponder) data, household survey, and census data
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_type":
            """
1. Tabular
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "data_details":
            """
There are several datasets that will be used including AIS (shipping transponder) data, household survey, and census data.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """Yes, students could being immediately.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """Insights into structural transformation for Indonesia.
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "additional_comments":
            """No""",
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