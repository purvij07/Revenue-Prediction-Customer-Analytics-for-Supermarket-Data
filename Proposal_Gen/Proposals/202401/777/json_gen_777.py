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
            """777""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """National Health Accounts Producer Tool Use- Data Analysis""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Introduction":
            """ 
            Over the years, Zambia's health care system has experienced a number of changes in an effort to adapt to the 
            country's changing economic and demographic conditions. The Ministry of Health's use of the National Health Accounts 
            (NHA), a mechanism that precisely tracks public and private health spending, demonstrates its dedication to a strong 
            and responsive health system. A detailed picture of the flow of health funds is given by the NHA's methodical approach, 
            which starts at their sources and ends with the final health services that are provided to Zambians.

	        This study attempts to extend the NHA estimations to 2021, offering a coherent and comparative view of health expenditures. 
	        It does this by using the NHA Production Tool (NHAPT) and the WHO's System of Health Accounts (SHA) 2011 framework. 
	        Understanding the Zambian health care system's past and present enables us to forecast its needs and prepare for its future. 
	        Therefore, this project is not merely an academic exercise but a strategic endeavor to inform policy-making and optimize 
            health service delivery for the nation's wellbeing.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The specific objectives are outlined as follows:
            * Assess Health Sector Budget Trends: To evaluate how the health sector budget in Zambia has evolved from 1990 to 2018, 
            with an emphasis on the changes in funding amounts and the structure of its allocation.
            * Analyze Fiscal Space for Domestic Resource Mobilization: To examine the fiscal capacity of Zambia to fund health services
            and determine the extent of domestic resource mobilization within the health sector.
            * Estimate Budget Efficiency for Health: To measure how effectively the health budget is utilized in Zambia, 
            ensuring that the allocated funds lead to the expected health outcomes without wastage.
            * Assess Health Sector Financial Sustainability: To evaluate the long-term financial viability of the health sector 
            in Zambia and the sustainability of health services provision within the context of public finance management.

            The focus is on understanding the inefficiencies in resource utilization and the challenges associated with risk pooling 
            in the Zambian healthcare financing system.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            * International databases such as the GHED, World Bank, and IMF databases for health spending data.
            * National sources including the Ministry of Finance Yellow Books for detailed budgetary information.
            * Complementary data from previous NHA studies, MTEF, and audit reports to enrich the analysis.

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Research Hypotheses":
            """
            The study will test the following hypotheses:
            * Null Hypothesis (H0): Budgetary practices have no significant effect on fiscal space, efficiency, and sustainability
            for health services provision in Zambia.
            * Alternative Hypothesis (H1): Budgetary practices significantly affect fiscal space, efficiency, and sustainability 
            for the attainment of health services in Zambia.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            The National Health Accounts (NHA) have historically provided a lens through which health expenditure in Zambia could 
            be viewed and assessed.By analyzing trends and compositions from the past decades, the study will highlight how 
            resource allocation has evolved and identify the leverage points for enhancing fiscal space and domestic resource 
            mobilization. The investigation into budget efficiency and sustainability aims to pinpoint the systemic inefficiencies 
            that hinder effective resource utilization.

            Understanding the causal relationships between budget practices and health service delivery outcomes will inform strategies 
            to improve risk pooling mechanisms, a critical component for achieving universal health coverage. The study's findings are 
            expected to offer actionable insights that could lead to significant reforms in the health sector, ultimately contributing 
            to the financial sustainability of health services in Zambia.

            The rationale for this research is, therefore, to support Zambia's Ministry of Health in its mission to provide 
            high-quality healthcare services by fostering a financially sustainable health system that effectively pools risks 
            and efficiently allocates and utilizes resources.

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            Application of the SHA framework for systematic classification of health expenditures.
            Deployment of the Fiscal Space decomposition method and the Cobb-Douglas production function.
            Measurement of budget efficiency using parametric and non-parametric methods, including DEA and FDH. 
            To explore using Concept Mapping Financial Sustainability Framework approach.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - ⁠(2 Weeks) Literature Review
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
            Data Availability and Reliability: It may be difficult to obtain complete, accurate, and current data. Incomplete or inconsistent 
            historical data may have an impact on trend analysis and the reliability of conclusions.

            Changing Economic Conditions: The examination of fiscal space and health expenditures may be impacted over time by changes in Zambia's 
            macroeconomic conditions, such as inflation rates, currency devaluations, or economic recessions.

            Methodological Restrictions: Because the study is based on particular approaches, such as the Cobb-Douglas production function, 
            it may not adequately capture the complexities of resource allocation in the health care industry due to its underlying assumptions.

            Healthcare System Complexity: Analyzing budget efficiency and resource mobilization might become more difficult due to the 
            healthcare system's multidimensional nature, which involves a variety of stakeholders and financial flows.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "The World Bank",
        "Proposed by email": "skagulura@worldbank.org",
        "instructor": "Edwin Lo",
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
