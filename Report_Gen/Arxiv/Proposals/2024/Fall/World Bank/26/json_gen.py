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
            """26""",
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
            """Eduardo Andres Espitia Echeverria""",
        # -----------------------------------------------------------------------------------------------------------------------
        "unit_name":
            """ECA Transport Global Practice (IECT1)""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Enhancing Transport Decarbonization in the European Union (ID:P501640)""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_lead":
            """Gozde Isik (gisik@worldbank.org)""",
        # -----------------------------------------------------------------------------------------------------------------------
        "team_members":
            """Szilvia Doczi (sdoczi@worldbank.org)
Joao Rampini (jrampini@worldbank.org)
Carolina Monsalve (mmonsalve@worldbank.org)
Daniel Pulido (dpulido@worldbank.org)
Luis Blancas (lblancas@worldbank.org)
Victor A Aragones (varagones@worldbank.org)
""",
    },


    "Challenge": {
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_location":
            """Europe region (European Union and accession countries)
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "challenge_type":
            """Transport decarbonization in the EU and fair transition: The European Union is the world’s third-largest emitter of greenhouse gases, and transportation is
currently the second-largest source of emissions in the EU, representing 29% of energy sector emissions. Unlike other EU economic sectors that have successfully
decreased emissions, the transport sector has witnessed a significant increase in emissions since 1990. Decarbonizing the transport sector by 2050, as per the EU
Green Deal ambition, will therefore require humongous efforts on technological transition, but also on policy and institutional frameworks that lead to more
sustainable transport systems (with higher modal shares of public transport and rail and intermodal freight transport). In addition, this transition needs to be done
in a fair manner, not leaving behind low-income households and small enterprises.
While the decarbonization objective is set at regional level, the challenges faced by different countries differ greatly, considering the different macroeconomic
conditions, energy-systems characteristics, market dynamics, and institutional frameworks. Identifying the key challenges faced by some of the countries in the
region to achieve the transport climate objective in a fair manner requires both quantitative and qualitative analysis.
The World Bank is developing analytical work to identify the key challenges to decarbonize the transport sector in Europe, looking at the specific challenges in
different transport subsectors, through the lenses of 3 cross-cutting areas: 1) Financing transport decarbonization, 2) Innovation and technology diffusion, and 3)
Institutional and governance reforms.
""",
        # -----------------------------------------------------------------------------------------------------------------------
        "solution_beneficiaries":
            """
Households, logistic companies and shippers, and State-Owned Enterprises, particularly in eastern EU member states and accession countries.
            """,
    },


    "Status and Timeline": {
        # -----------------------------------------------------------------------------------------------------------------------
        "project_status":
            """Concept note has been conducted. The analytical work has started.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "project_milestones":
            """
No hard deadlines in the short term. The work is developed under a PASA with completion date on December 31, 2025. Multiple intermediate deliverables are
envisioned throughout the PASA.
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
2. Tabular
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "data_details":
            """
The data consists of a collection of (.csv) datasets containing characterization of transport activity (pax-km, tonne-km, modal shares), transport equipment
(motorization levels, technology distribution, rolling stock), macroeconomic parameters (population, GDP) by country, cost evolution curves of different
technologies, and decarbonization trajectories of the transport sector produced by the World Bank.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "STC_requirement":
            """Students will be granted immediate access to the data.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "data_sample":
            """Yes""",
        # -----------------------------------------------------------------------------------------------------------------------
        "ultimate_goal":
            """The objective of the project is to identify the key challenges faced by countries in the region to achieve the transport decarbonization objectives, and provide
recommendations, based on data-analysis, to overcome these challenges and accelerate the transition. Based on the students’ interest, this could be focused on a
specific transport subsector (e.g., zero-emission trucks, sustainable mobility in metropolitan and urban areas, or strengthening of the rail freight sector), and the
analysis could focus on one of the following areas: 1) Analysis of trends that point to country-specific challenges to decarbonize the transport sector, assessing the
different contexts across EU member states and accession countries. For instance, using the data to analyze how growing motorization rates in some countries,
coupled with high reliance on second-hand imports and longer vehicle lifespans, may delay the decarbonization of the road sector; 2) Econometric analysis to
compute elasticities of transport demand with respect to a subset of variables, in order to improve future demand projections for the countries in the region under
different scenarios; 3) Analysis of potential innovative financing to accelerate transport decarbonization (e.g., introducing residual value guarantees to facilitate
leasing solutions for zero-emission vehicles); 4) Identification of potential green trade corridors in the region to catalyze innovation and accelerate green logistics;
5) Explore options to facilitate access to commercial financing for transport State-Owned Enterprises in the region and policies to improve their performance.
""",
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