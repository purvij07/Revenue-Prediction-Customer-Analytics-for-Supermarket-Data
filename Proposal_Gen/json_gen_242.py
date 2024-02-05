#%%
import json
import os
import shutil

#%%

def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

semester2code = { "sp":"01", "spr":"01", "spring":"01", "su":"02", "sum":"02", "summer":"02", "fa":"03", "fall":"03"}
thisfilename = os.path.basename(__file__)

data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """242""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """HNP - National Health Accounts Producer Tool Use""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The aim of this study is to describe and analyze weaknesses within the budget to generate resources for health. 
            This will involve analysis of health budget practices in Zambia including its trends, composition, fiscal space, 
            efficiency and its sustainability within the public financial management framework to explain why resources are 
            not used effectively and explore why the function of risk pooling is a problem in the Zambian health care 
            financing system.

            1. To examine the trends and composition of health sector budget in Zambia from 1990 to 2018
            2. To analyze the fiscal space and domestic resource mobilization in Zambia.
            3. To measure the budget efficiency for health in Zambia.
            4. To explore and describe health sector budget sustainability in Zambia.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
             The dataset for this project is sourced from various audited primary secondary sources. Primary data was collected
             using the standard questionnaire from donors, NGOs employers and private insruance schemes. Secondary data sources 
             were used for Government and Household expenditures. The data collection was conducted by trained research
             assistants who visited all sampled institutions under the supervision of the technical team. The team research
             vetted all the questionnaires used in collect primary data to ensure compliance with SHA 2011 methodology. 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            The rationale for this study is to justify the need for analyzing weaknesses within the budget process for health 
            resource generation in Zambia, including its trends, composition, fiscal space, efficiency, and sustainability, 
            in order to address the ineffective use of resources and the problem of risk pooling in the Zambian health care 
            financing system.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            1. Application of the SHA framework for systematic classification of health expenditures.
            2. Deployment of fiscal space decomposition on method using Cobb-Douglas production function.
            3. Accounting for fiscal space for health 1995 - 2018 using public expenditure on Health by Scheme.
            4. Measurement of budget efficiency using parametric and non-parametric methods, including DEA and FDH.
            5. To explore using Concept Mapping Financial Sustainability Framework approach.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (2 Weeks) Literature Review
            - (3 Weeks) Data collection 
            - (4 Weeks) Data Analysis
            - (3 Weeks) Budget Process Analysis
            - (1 Week)  Compiling Results  
            - (1 Week)  Submission
            - (1 Week)  Final Presentation  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            For this project maximum 3 students can work on it.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            The challenge is ensuring the availability and quality of data for the analysis of health budget trends, 
            fiscal space, and efficiency in Zambia. 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "The World Bank Group",
        "Proposed by email": "skagulura@worldbank.org",
        "instructor": "Dr. Edwin Lo",
        "instructor_email": "edwinlo@email.gwu.edu",
        "github_repo": "https://github.com/purvij07/24Spr_PJAIN_NHA_DataAnalysis",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
