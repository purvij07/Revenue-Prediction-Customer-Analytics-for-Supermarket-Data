import streamlit as st
import pandas as pd
import os
import plotly.express as px
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import base64
from PIL import Image
import io
import joblib
from datetime import datetime

def resize_image(file_path, output_size=(1470, 894)):
    with Image.open(file_path) as img:
        # Use Image.Resampling.LANCZOS for high-quality downsampling
        img = img.resize(output_size, Image.Resampling.LANCZOS)
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')  # Make sure the format matches your image type
        return f"data:image/jpeg;base64,{base64.b64encode(img_byte_arr.getvalue()).decode()}"

# Use the function to get a resized Base64 string
image_path = '/home/ubuntu/Capstone Copy/code/datasets/updated_data/SalesOvrTime/retailimage.jpeg'
base64_string = resize_image(image_path, (250, 220))  

def add_bg_image(base64_string):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{base64_string}");
            background-size: cover%;  /* Ensures the entire image is visible */
            background-repeat: no-repeat;
            background-position: right top;  /* Centers the background image */
            background-attachment: fixed;  /* Keeps the background image fixed during scrolling */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_image(base64_string)

def add_bg_color():
    # Modify the color as needed
    color = "33CCFF"  # Light grey, change to any color you prefer (e.g., "#34ebd8" for teal)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_color() 

def custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-color:#adced9;  /* Light grey background */
        }
        div.stButton > button:first-child {
            background-color: rgb(255, 75, 75);
            color: white;
            border-radius: 10px;
            padding: 10px 24px;
            border: none;
        }
        div.stTextInput > input {
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
custom_css()

def load_model():
    model_path = '/home/ubuntu/Capstone Copy/code/code/xgb_model.pkl'
    return joblib.load(model_path)

model = load_model()
# Function to load data
def load_data(supermarket, report_type):
    if report_type == 'Revenue Prediction':
        file_path = f'/home/ubuntu/Capstone Copy/code/datasets/updated_data/sampled_test_datasets/test_set_data_{supermarket.lower()}.csv'
    else:
        file_path = f'/home/ubuntu/Capstone Copy/code/datasets/updated_data/updated_All_Data_{supermarket}.csv'
    try:
        df = pd.read_csv(file_path)
        if 'category' in df.columns:
            df['category'] = df['category'].astype('category')
        return df
    except Exception as e:
        st.error(f"Failed to load data: {str(e)}")
        return pd.DataFrame()

def prepare_input_data(date, category):
    # Adjust these calculations based on the actual features needed
    return pd.DataFrame({
        'category': [category],  # Make sure this is encoded the same way as during training
        'day_of_week_num': [date.weekday()],
        'week_of_month': [(date.day - 1) // 7 + 1],
        'sin_day': [np.sin(2 * np.pi * date.day/30)],
        'cos_day': [np.cos(2 * np.pi * date.day/30)],
        'sin_week': [np.sin(2 * np.pi * date.weekday()/7)],
        'cos_week': [np.cos(2 * np.pi * date.weekday()/7)],
        'Last_Seen_Days': [0],  # Placeholder for the actual calculation
        'Revenue_lag1': [0],    # Placeholder
        'Revenue_lag2': [0],    # Placeholder
        'Revenue_lag3': [0],    # Placeholder
        'sin_day_lag1': [0],    # Placeholder
        'cos_day_lag1': [0],    # Placeholder
        'sin_week_lag1': [0],   # Placeholder
        'cos_week_lag1': [0],   # Placeholder
        'weekly_rolling_avg': [0],  # Placeholder
        'weekly_rolling_std': [0]   # Placeholder
    })


def compare_brand_prices(data, product_name):
    data['names'] = data['names'].str.lower().replace('[^a-z\s]', '', regex=True).fillna('')
    data = data.drop_duplicates(subset=['names', 'price'])
    tfidf = TfidfVectorizer(stop_words='english', max_features=1000, ngram_range=(1, 2), min_df=2)
    tfidf_matrix = tfidf.fit_transform(data['names'])
    query_vector = tfidf.transform([product_name])
    cosine_sim = cosine_similarity(query_vector, tfidf_matrix).flatten()
    similar_indices = np.where(cosine_sim >= 0.1)[0]
    if len(similar_indices) == 0:
        return pd.DataFrame()
    similar_products = data.iloc[similar_indices]
    similar_products['similarity'] = cosine_sim[similar_indices]
    similar_products = similar_products.sort_values(by=['similarity', 'names', 'price'], ascending=[False, True, True])
    similar_products = similar_products.drop_duplicates(subset=['names'], keep='first')
    similar_products['price_difference'] = similar_products['price'] - similar_products['price'].min()
    return similar_products[['names', 'price', 'price_difference', 'similarity', 'own_brand', 'Quantity']]

def main():
    st.title('Supermarket Revenue Data Dashboard')
    supermarket = st.sidebar.selectbox('Select a Supermarket', ('Select', 'Aldi', 'ASDA', 'Morrisons', 'Sainsbury', 'Tesco'))
    report_type = st.sidebar.selectbox('Select a report', ('Select', 'Revenue Over Time', 'Sales Trends Over Time', 'Interactive Pie Chart: Distribution of Product Categories', 'Price Comparison', 'Revenue Prediction'))
    product_name = st.sidebar.text_input("Enter a product name for comparison:")
    
    if supermarket != 'Select':
        df = load_data(supermarket,report_type)
        if not df.empty:
            st.write(f"Data for {supermarket}:")
            st.dataframe(df.head())
            categories = df['category'].cat.categories.tolist()
        else:
            st.write("No data available or failed to load.")
            categories = []


    if report_type == 'Revenue Over Time':
        revenue_supermarket = st.selectbox('Select Supermarket for Revenue Data', ('Select', 'Aldi', 'ASDA', 'Morrisons', 'Sainsbury', 'Tesco'), key='revenue_supermarket')
        if revenue_supermarket != 'Select':
            image_path = f'/home/ubuntu/Capstone Copy/code/datasets/updated_data/RevenueImg/{revenue_supermarket.lower()}_revenue_over_time.png'
            if os.path.exists(image_path):
                st.image(image_path, caption=f'Average Daily Revenue Trend for {revenue_supermarket}')
            else:
                st.error("Image not found.")

    elif report_type == 'Sales Trends Over Time':
        sales_type = st.selectbox('Select Type of Sales Data', ('Select', 'Own Brand', 'Non-Own Brand'), key='sales_type')
        if sales_type != 'Select':
            filename_map = {'Own Brand': 'ownbrand', 'Non-Own Brand': 'nonownbrand'}
            filename_suffix = filename_map.get(sales_type)
            if filename_suffix:
                image_path = f"/home/ubuntu/Capstone Copy/code/datasets/updated_data/SalesOvrTime/{filename_suffix}.png"
                if os.path.exists(image_path):
                    st.image(image_path, caption=f'Sales Trends Over Time for {sales_type}')
                else:
                    st.error("Image not found.")
            else:
                st.error("Sales type is not recognized.")

    elif report_type == 'Interactive Pie Chart: Distribution of Product Categories':
        if supermarket != 'Select':
            fig = px.pie(df, values='Revenue', names='category', title=f'Distribution of Product Categories in {supermarket}')
            st.plotly_chart(fig, use_container_width=True)

    elif report_type == 'Price Comparison' and product_name:
        if st.button('Compare Prices'):
            results = compare_brand_prices(df, product_name)
            if not results.empty:
                st.subheader("Product Comparison Results:")
                st.dataframe(results)
            else:
                st.write("No similar products found. Please refine your search.")

    elif report_type == 'Revenue Prediction':
        if supermarket != 'Select':
            df = load_data(supermarket, report_type)
        if not df.empty:
            categories = df['category'].unique().tolist()
            category_product = st.sidebar.selectbox('Select Category/Product:', categories)
            date = st.sidebar.date_input('Select date for prediction', value=datetime.now())

            input_data = prepare_input_data(date, category_product)

            if st.sidebar.button('Predict Revenue'):
                prediction = model.predict(input_data)
                st.write(f"Predicted revenue for {category_product} on {date.strftime('%Y-%m-%d')}: ${prediction[0]:,.2f}")

if __name__ == "__main__":
    main()








