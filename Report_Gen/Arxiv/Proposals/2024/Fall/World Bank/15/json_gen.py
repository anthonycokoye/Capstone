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
            """15""",
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
            """Solomon Kagulura""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """HNP""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """P174185""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """John Makumba""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """Aya Kagota , wisdom Mulenga""",
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """National Health Accounts Producer Tool Use
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """National Health Accounts Data Analysis""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
Ministry Of Health
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """Early ideation
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
Yes. Need to produce NHA report 2018 to 2022
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "lead_meeting":
            """Yes""",
    },


    "Data": {
        # -----------------------------------------------------------------------------------------------------------------------
        "dataset_size":
            """Not Sure but constitute 5 questionnaires from several respondents
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_type":
            """
1. Text
2. Time series/Panel data
3. Tabular
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "data_details":
            """
Health Expenditure Tracking from Employers, Households, Donors , Government , NGOs , Insurance Firms analyzed by disease and health service providers
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """Students will need to collect the data. Data Not Available as at now""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """We need to know Performance of Health Financing Indicators such as Total Health Expenditure , Out of pocket expenditure , inpatient and outpatient costs etc
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "additional_comments":
            """This will be a national health accounts data collection, analysis and documentation exercise.""",
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