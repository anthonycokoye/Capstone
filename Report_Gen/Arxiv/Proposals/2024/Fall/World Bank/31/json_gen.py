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
            """31""",
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
            """Joachim Vandercasteelen""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """South Asia Agriculture and Food Practice""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Food Security and Agricultural Productivity Project P155513""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """Sheu Salau ssalau@worldbank.org""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """None
""",
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """Bhutan
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """The agricultural sector in Bhutan is at a crossroad with market opportunities arising from growing demand for high value products in urban and domestic markets
while at the same time the sector struggles with low productivity, limited value addition, and increasing vulnerability to climate change. Agriculture continues to be
Bhutan’s main employer (48%), especially in rural areas, despite declining contribution to GDP (19%). Bhutan has experienced only slow growth in agricultural
value added per worker (1% annually) which is dwarfed by the performance of aspirational peer countries undergoing a successful structural transformation. The
main constraints to productivity are crop damages caused by wildlife, pests, and diseases; irrigation and water management issues; limited access to modern
inputs and technologies; and climate-change induced yield variability. While half of Bhutan’s harvested area comes from irrigated and rainfed paddy and rainfed
maize, the area dedicated to these crops and their yield has declined in recent year. In contrast, agricultural production for selected cash crops (cardamom and
areca nuts) and fruits (mandarins) has increased in recent years, suggesting that the agricultural sector is gradually transitioning from traditional to higher value
products where the country has a comparative advantage.
Yet, we currently have limited analytical and quantitative evidence of the actual changes that the agricultural sector is undergoing, how the sector is contributing
to the rural transformation process, and whether and how it has contributed to the impressive poverty reduction in Bhutan in the recent years. This is despite a
wealth of data: several governmental agencies and departments collect data on agricultural production and decision-making, poverty and resilience indicators, and
there is a global wealth of geospatial data available. The activity would address this evidence by integrating all the useful data and analyzing recent patterns in the
agricultural and rural transformation process in Bhutan. Particular research questions could be: in which agricultural and forestry products does Bhutan have a
comparative advantage? How has growth in the agricultural sector contributed to jobs creation, labor reallocation, and poverty reduction in Bhutan? What are the
expected outcomes from inducing more agricultural productivity growth and trade on rural areas? Which crops and areas are most vulnerable to natural disasters,
human-wildlife conflict, disease past attacks, and the impacts of climate change?
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
The direct beneficiaries would be Bhutanese policy makers in the agricultural and rural sector to improve their decision making using big data and empricial
evidence. The indirect beneficiaries are actors in the agricultural value chain - ranging from farmers, to traders and comsumers, who would benefit from better
information and informed. evidence-based decision making.
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """We have started to collect and merge the data and done some first analysis. However, we need a dedicated effort to look at the details and complexity of the data
and provide more granular analysis
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
The FSAPP ends in dec 2024
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "lead_meeting":
            """Yes""",
    },


    "Data": {
        # -----------------------------------------------------------------------------------------------------------------------
        "dataset_size":
            """5 gb
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_type":
            """
1. Time series/Panel data
2. Geospatial
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "data_details":
            """
Agricultural production data
Renewable Natural Resources census
Poverty, vulnerability, and Labor indicators
geospatial data on climate indicators, market access, etc.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """The work can start imeediately.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """generate analytical evidence for informed decision making in the agricultural and rural sector in Bhutan
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "additional_comments":
            """Thanks for providing this opportunity.""",
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