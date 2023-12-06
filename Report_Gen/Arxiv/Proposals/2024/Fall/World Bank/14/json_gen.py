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
            """14""",
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
            """Alejandro Molnar""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """Development Research Group""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Economic Development through a Spatial Lens. RA-P180214-RESE-TF0B979""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """Forhad Shilpi, fshilip@worldbank.org""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """Matias Navarro, PhD student, Cornell University""",
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """Multiple projects, depending on student fit and interest:
- Bangladesh
- India
- Rwanda
- Cape Town, South Africa
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """- Bangladesh: value of bridges to transportation network connectivity
- India: analysis of freight costs using data from a digital freight matching platform
- Rwanda: analysis of telemetry data
- Cape Town: impact on commuters from transportation service quality""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
All projects are academic research, beneficiaries vary by project
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """Varies by project, can adapt to student requirements and availability
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
Varies by project, can adapt to student availability
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "lead_meeting":
            """Yes""",
    },


    "Data": {
        # -----------------------------------------------------------------------------------------------------------------------
        "dataset_size":
            """Varies, from 2 gb to 50gb
""",
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
Many types of data and tasks, can be adapted based on student capabilities and interest.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """The ultimate goals are estimating parameters in economic models, and producing quantitative insights from those models. The goal is not prediction.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "additional_comments":
            """A brief discussion w/ academic advisors might be required to identify fit.""",
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