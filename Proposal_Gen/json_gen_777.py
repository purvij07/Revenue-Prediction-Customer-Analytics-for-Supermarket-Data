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
            """Time Series Forecasting for UK Supermarkets""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Introduction":
            """ 
            The UK's supermarket sector is witnessing transformative changes, demanding an acute analysis to forecast future trends
            accurately. One important participant in this market, ASDA, provides a wealth of data for researching customer habits 
            and sales patterns. Through strategic data analysis and forecasting, this initiative seeks to optimize sales and 
            profitability by extending approaches to other big supermarkets in addition to analyzing ASDA's data.

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            Our objective is to use predictive analytics to accurately forecast future sales by analyzing sales trends at ASDA 
            and other supermarkets. In order to compare consumer reactions to own brand versus competition items, we plan to 
            closely examine ASDA's pricing methods and assess how they affect sales. This analysis will improve overall sales 
            performance and consumer analytics and lay the groundwork for more extensive uses throughout the UK grocery industry.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            Primarily centered around the ASDA dataset, our analysis extends to encompass datasets from four other UK supermarkets 
            - Aldi, Morrisons, Tesco, and Sainsbury's, sourced from Kaggle. This comprehensive data collection, spanning from 
            January 9, 2024, to the latest update, allows for a robust cross-comparison and predictive analytics application.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
    
        "Rationale":
            """
            By dissecting ASDA's time series data, we aim to uncover the underlying patterns that define its market performance. The study's 
            rationale is rooted in the need to adapt to the dynamic retail environment, with a focus on maximizing sales and understanding the 
            market's pulse. Findings from this research could potentially steer ASDA's strategic planning and pricing policies. The same can 
            be followed for other four different UK supermarkets datasets.

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            The research will be approached in several phases: Detailed data preprocessing to ensure dataset quality and reliability. Application 
            of time series analysis techniques, including ARIMA and exponential smoothing models. Utilization of machine learning methods for 
            predictive analytics, such as neural networks. Comparative analysis of pricing strategies between ASDA's own brand and other brands.
            This same approach can be applied to other four different UK supermarkets datasets.

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - ⁠(2 Weeks) Initial Data Cleaning and Preprocessing 
            - (2 Weeks) Exploratory Data Analysis and Model Selection 
            - (2 Weeks) Model Development and Validation 
            - (1 Weeks) Comparative Analysis of Pricing Strategies 
            - (1 Week)  Finalizing the Forecasting Model 
            - (1 Week)  Drafting the Final Report, Presentation Preparation and Review

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            This project can accommodate 3 students, allowing for a division of tasks ranging from data preprocessing
            to model development and analysis.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            * Data Completeness: Missing values or inaccuracies within the ASDA dataset could impact the quality of the forecasts. 
            * Model Overfitting: Ensuring the model generalizes well to unseen data while maintaining accuracy is a critical concern.
            * Dynamic Market Conditions: The influence of external factors such as economic shifts and competitive actions may affect the predictability of sales trends. 
            * Technological Limitations: The complexity of models may be constrained by available computational resources.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Sowmya Maddali, Purvi Jain, Mohammed Kanu",
        "Proposed by email": "sowmyamaddali@gwu.edu, pjain07@gwmail.gwu.edu, sillahkanu@gwmail.gwu.edu",
        "instructor": "Edwin Lo",
        "instructor_email": "edwinlo@email.gwu.edu",
        "github_repo": "https://github.com/purvij07/24Spr_PJAIN_TimeSeries_SuperMarket",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
