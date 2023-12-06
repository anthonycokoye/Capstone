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
            """33""",
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
            """Michael Ilesanmi""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """Social Sustainability and Inclusion""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """P161364 and P179447""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """Audrey Sacks, Yetunde Fatogun, Fawah Akwo, Ida Mboob""",
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """Nigeria""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """NFWP utilizes Women Affinity Groups (WAGs), a variation of Self-Help Groups as platforms to build women’s human, financial and social capital. The WAGs meet
on a regular basis to (a) save, pool their savings, and lend money to each other on a rotating basis start or expand business, pay for healthcare or education
expenses, or meet other financial needs.; (b) receive training in key areas such as financial education, business skills, negotiation, gender, and life skills etc. from
Ward Facilitators. As a result, membership of WAGs helps women:
i. access to credit, savings, and insurance services that enable women to start and grow their businesses. This helps in generating income and achieving financial
independence, which leads to the economic empowerment of women
ii. improve the social status of women by giving them a voice in decision-making processes in their households and communities
iii. promote social capital by creating a supportive environment for women to share their experiences, ideas, and knowledge. This fosters self-esteem, self-confidence, and leadership skills, and enables women to participate in decision-making processes in their households and communities
iv. reduce poverty by providing an avenue for women to access credit and savings, thereby enabling them to invest in income-generating activities. This leads to
increased household income and improved standards of living.
v. engage in advocacy and collective action to address broader social and economic issues affecting their community.
We would like to digitize the processes of the Women Affinity Groups under the Nigeria for Women project. It is expected that by automating calculations for
savings, loan repayments, fines, and savings balances, such applications will reduce time spent on financial transactions that are core to the WAGs.
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
low-income unbanked women
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """Supervision
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
The NFWP Scale Up is expected to become effective by December 15 2023
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "lead_meeting":
            """Yes""",
    },


    "Data": {
        # -----------------------------------------------------------------------------------------------------------------------
        "dataset_size":
            """100GB
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_type":
            """
1. Text
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "data_details":
            """
Women's savings data
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """We hope the project can support the development of a digital savings group Application
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "additional_comments":
            """NIL""",
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