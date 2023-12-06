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
            """19""",
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
            """Meghana Rao Pahlajani""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """2030 Water Resources Group - SWARG""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """P181147""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """TTL - Ajith Radhakrishnan - aradhakrishnan3@worldbank.org""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """Meghana Rao Pahlajani, Yogesh Bandhu Arya""",
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """Uttar Pradesh, India
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """Small and marginal farmers in India, currently have limited capacity to afford purchasing of farm equipment to support their agricultural processes. They rely on
Custom Hiring Centers (CHC) to rent out farm equipment based on their requirements.
However, there is a lack of standardization in the rates at which this equipment is available for rent, often leading to a distortion in the rental prices and preventing
access to these mechanization solutions. Additionally, when the demand for specific equipment increases, the prices for rental can become prohibitively high,
further restricting access to the rental market.
The challenge we are trying to solve for is the variability in the pricing strategy for farm equipment rental in agricultural areas to ensure increased access,
availability and affordability for small and marginal farmers to ensure increased agricultural productivity.
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
The beneficiaries of the solution would be:
A) Farmers: The standardizing of rates for farm equipment rental would allow for a more predictable budgeting by the farmers so they can avail of mechanization
services in their agricultural processes.
B) Custom Hiring Centers: The pricing guidelines can support the Custom hiring centers better manage their operations when faced with fluctuations in demand
C) Government: The Government would benefit from setting guidelines on the range of prices that the farm equipment can be rented out at to ensure that farm
equipment accessibility is increased and exploitative pricing is stopped.
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """The 2030 WRG is supported a program by the Government of Uttar Pradesh to support climate smart agriculture in the State. The program focuses on improving
agricultural productivity, enhancing water use efficiency and reducing carbon emissions.
The program was formalized in December 2022, and is currently in the implementation stage. The solution to address mechanization and develop farm equipment
rental pricing models is in the conceptualization stage.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
The program seeks to work closely on integrating the pricing strategy along with the other initiatives to support agricultural mechanization. The current tentative
timelines for this integration is between March - June 2024.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "lead_meeting":
            """Yes""",
    },


    "Data": {
        # -----------------------------------------------------------------------------------------------------------------------
        "dataset_size":
            """40 GB
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_type":
            """
1. Tabular
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "data_details":
            """
The data that will be provided on the current rental rates and equipment demand over time periods (daily, seasonally) for 30 Custom Hiring Centers across the
focus, Uttar Pradesh and for an additional 10 Custom Hiring Centers in other states as reference data.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """No Additional data or access will be required.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """The ultimate goal of this project is to develop a pricing strategy that would support affordability and access to farm equipment for small and marginal farmers. This
will be integration with policy and regulatory level guidelines that govern the operation of Custom Hiring Centers. The focus is on developing an algorithm and modelling framework that can be used for this context.
Yes, the data will have the essential information required to accomplish this goal.
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "additional_comments":
            """Once the results of this modelling have been validated at a field level, it can be scaled to similar applications across geographies as well. It will help in developing
pricing related strategies which can reflect in policy level mechanization decisions as well.""",
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