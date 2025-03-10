import json
import os
import shutil
def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)




data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """2""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Fall""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Self Organizing Map (SOM) Package """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The goal of this project is to build a python Self Organizing Map (SOM) package can be used for Neural Network 
            community. We have the initial python training code which can be used and organized. The main goal is to create
            a user friendly python package which has all the necessary functionality like train and predict. The SOM package
            has a variety of visualization which we need to implement. We have the basic codes  however we want them to be
            used in the package. For example we have 4 different source of data like NLP, Computer Vision, Tabular and Timeseries.
            We have different way to visualize them (Basic figures like SOM grid and the distance will stay same accross all dataset)
            , however for specific data we will develop different figures. We need to use the basic built data from 
            different source like Sklearn, torch ,and etc. Then we will train the SOM and use the visualization to cluster the data.
            After the package is built we need to create multiple example for each dataset and compare them with Kmeans and other
            classical clustering algorithm.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            Built is dataset can be used for NLP, Computer Vision, Tabular and Timeseries datasets.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            This project is going to help machine learning and deeplearning researches to use the SOM for postprocessing 
            their models predictions. This package will be alternative to the minisom package which is not complete and
            it will be used across all the 4 type of datasets

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  
            
            1. Create the SOM class.
            2. Design the package and the folder structure.
            3. Create modular and reusable figure codes. 
            4. Work on the built in datasets of 4 datatypes.
            5. Complete the package with all the figures needed.
            6. Create a example folder and show the usage of the package.
            7. Use pypi to install the package.
            8. Create a documentation from the begging till the end of the product.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  
            
            - (1 Weeks) Create the SOM class structure .  
            - (2 Weeks) Design the folder and classes and utils functions.  
            - (1 Weeks) Modular widgets  
            - (2 Weeks) Built in dataset 
            - (2 Weeks) Complete all the figures codes and training and testing methods
            - (2 Weeks) Create a example folder  
            - (2 Weeks) Pypi installation
            - (2 Weeks) Documentation
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            For this project maximum 2 students can work on it.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            The challenge is on using the right built dataset and create a professional package with efficient training code.
            Also, installing as pypi and create clear instruction and documentation of the usage. 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Dr. Amir Jafari",
        "Proposed by email": "ajafari@gwu.edu",
        "instructor": "Amir Jafari",
        "instructor_email": "ajafari@gmail.com",
        "github_repo": "https://github.com/amir-jafari/Capstone",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(os.getcwd() + os.sep + f'Arxiv{os.sep}Proposals{os.sep}{data_to_save["Year"]}{os.sep}{data_to_save["Semester"]}{os.sep}{data_to_save["Version"]}',exist_ok=True)
output_file_path = os.getcwd() + os.sep + f'Arxiv\Proposals{os.sep}{data_to_save["Year"]}{os.sep}{data_to_save["Semester"]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy('json_gen.py',output_file_path )
print(f"Data saved to {output_file_path}")
