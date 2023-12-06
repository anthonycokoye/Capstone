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
            """23""",
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
            """Ryan Rafaty""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """Public Institutions Data and Analytics Unit of the Governance Global Practice""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Political Economy of Climate Change - P180308""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """Laura Zoratto - lzoratto@worldbank.org""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """Verena Fritz - vfritz@worldbank.org
Ryan Rafaty - rrafaty@worldbank.org
Abdulaziz Almuzaini - aalmuzaini@worldbank.org
Chiara Bronchi - cbronchi@worldbank.org""",
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """Low- and Middle-Income Countries (LMIC), broadly speaking, with particular attention to the LMICs with whom the Bank's Governance Global Practice is currently
engaged in public financial management reforms that will support national responses to the risks of climate change.
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """Mitigating and adapting to the risks of anthropogenic climate change requires foresighted, strategic, and expeditious action from national governments. Countries
have adopted different approaches to climate change, both with respect to mitigation and adaptation, and we don’t fully
understand why. While much is already known about the inherent difficulties of climate policymaking, much less is known about (1) the institutional design
features that may help in mitigating or overcoming fundamental problems in the global cooperative effort; (2) factors that are driving variation in climate policies at
national and subnational levels; and (3) driving forces
of climate policy beyond the state, in particular civil society, the science-policy interface, and public opinion. The Climate Change Institutional Assessment (CCIA)
and the Country-Level Institutional Assessment and Review (CLIAR) database are two of the products of the World Bank's Governance Global Practice. Working
with our Unit, the student will apply their applied econometric and/or data science skills to help us further develop the data and analytics underpinning CCIAs and
CLIAR. The work will assist in providing guidance on conducting systematic, context-driven, and empirically grounded reviews of national institutions, with the goal
of influencing climate policy dialogue and informing the design of country engagement products.
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
The World Bank's Public Institutions Data and Analytics Unit, within the Governance Global Practice, provides strategy and support for within-country governance
reforms, serves as a hub for data on government and governance patterns in developing countries, and supports a repository of key global, regional, and country
analytical studies. The main beneficiaries of the data and analytics produced in this project will be the client governments, civil servants, and citizens of the lowand middle-income countries with whom the Bank's Governance Global Practice is engaged in climate-related lending, public financial management reform, and
development policy financing.
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """Stage II (currently undergoing internal quality enhancement review, with a view towards launching a revamped version of both CCIAs and the CLIAR database).
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
CCIA enhancement is an ongoing endeavor, while the CLIAR database (2.0) will be launched in the first quarter of 2024. We will be regularly updating and
upgrading the underlying data and analytics that feed into both of these knowledge products.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "lead_meeting":
            """Yes""",
    },


    "Data": {
        # -----------------------------------------------------------------------------------------------------------------------
        "dataset_size":
            """Less than 1 GB
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_type":
            """
1. Time series/Panel data
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "data_details":
            """
The CLIAR database consists of a large number of variables from multiple (World Bank and other) data sources. The variables are in panel time series format
(cross-country, 1990-2022), with over 180 countries included. The data contained within it relate to political, institutional, economic, and policy-related features of
countries, and the information is used to inform the Bank's Climate Change Institutional Assessment (CCIA) of countries, a data product that feeds into the Bank's
Country Climate and Development Reports (CCDR).
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """The student would be able to access the underlying data immediately upon commencement of the project.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """The ultimate goal of the project is to (i) identify additional variables that could be included in the database, either through the identification of new sources of data
or through manipulation of existing variables in the database; (ii) to produce compelling visualizations of the panel data that can be used to compare how
countries are situated across multiple dimensions in relation to other countries; (iii) to enhance our understanding of how different institutional features are linked
to particular climate and development policy outcomes.
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "additional_comments":
            """N/A""",
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