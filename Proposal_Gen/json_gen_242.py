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
            """Time Series Forecasting for UK Supermarkets""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The main objective of this proposal is to optimize sales and profitability for the supermarkets through comprehensive
            data analysis and strategic decision-making. We will leverage the provided datasets for forecasting and predective 
            analytics to enhance sales performance and customer analytics.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
             The dataset is primarily sourced from Kaggle. This dataset contains time series data for Aldi, ASDA, Morrisons, 
             Tesco and Sainsbury's. The data is daily from 20240109 until the last update.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            In our proposal for this project, we emphasize the importance of comprehensive customer analytics, forecasting and 
            predictive analytics, and sales analytics to drive informed decision-making and strategic planning for UK 
            supermarkets. Through customer analytics, we aim to identify top-selling products, discern trends in purchasing 
            behavior across product categories, and determine which supermarket exhibits the highest customer retention rate 
            based on repeat purchases. These insights enable us to tailor marketing strategies, optimize inventory management, 
            and enhance customer satisfaction. In forecasting and predictive analytics, we leverage historical data to predict 
            future sales for each supermarket, identify seasonal trends, forecast sales for upcoming seasons, and utilize machine 
            learning algorithms to predict products likely to experience increased demand. Finally, in sales analytics, we analyze 
            revenue distribution across categories to identify high-performing segments and assess revenue variation over time to 
            understand sales trends and fluctuations, empowering supermarkets to optimize their operations and drive sustainable 
            growth.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            1. Gather historical sales data from all UK supermarkets, ensuring data consistency and completeness.
            2. Cleanse the data to remove duplicates, handle missing values, and standardize formats for analysis.
            3. Conduct exploratory data analysis to gain insights into sales patterns, customer behavior, and product performance 
            across supermarkets.
            4. Analyze customer purchasing behavior to understand preferences and trends across product categories.
            5. Develop forecasting models to predict future sales for each supermarket based on historical data.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (1 Week)  Literature Review
            - (2 Weeks) Data collection and preparation
            - (2 Weeks) Exploratory Data Analysis
            - (2 Weeks) Customer Analytics
            - (2 Weeks) Forecasting and Predictive Analytics
            - (2 Weeks) Sales Analytics and Insights 
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
            The challenge are the exxternal factors, such as economic downturns, changes in consumer preferences, or unforeseen 
            events (e.g., pandemics), can significantly impact sales trends and forecast accuracy.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Sowmya Maddali, Purvi Jain, and Mohamed Kanu",
        "Proposed by email": "sowmyamaddali@gwmail.gwu.edu, pjain07@gwu.edu, sillahkanu@gwmail.gwu.edu",
        "instructor": "Dr. Edwin Lo",
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
