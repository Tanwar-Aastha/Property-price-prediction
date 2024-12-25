import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Plotting Demo")

with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.header("Enter your inputs")

# property_type
property_type = st.selectbox("Property Type", ['Flat','House'])
property_type = property_type.lower()  # Convert to lowercase

# Extract the valid categories for 'property_type' from the pipeline
valid_property_types = pipeline.named_steps['preprocessor'].transformers_[1][1].categories_[0]  # Adjust index as needed

# Validate 'property_type' input
if property_type.lower() not in valid_property_types:
    st.error(f"Invalid property type: {property_type}. Expected one of {valid_property_types}")
    st.stop()  # Stop execution if the input is invalid

# sector
sector = st.selectbox("Sector",sorted(df['sector'].unique().tolist()))

# bedroom
bedrooms = float(st.selectbox("Number of bedrooms",sorted(df['bedRoom'].unique().tolist())))

# bathroom
bathrooms = float(st.selectbox("Number of bathrooms",sorted(df['bathroom'].unique().tolist())))

# balcony
balcony = st.selectbox("Number of balconies",sorted(df['balcony'].unique().tolist()))

# agePossession
property_age = st.selectbox("Property Age",sorted(df['agePossession'].unique().tolist()))

# built_up_area
built_up_area = float(st.number_input("Built-up Area"))

# servant_room 
servant_room = st.selectbox('Servant Room', ['No', 'Yes'])
servant_room_value = 1.0 if servant_room == 'Yes' else 0.0

# store room
store_room = st.selectbox('Store Room', ['No', 'Yes'])
store_room_value = 1.0 if servant_room == 'Yes' else 0.0

# furnishing type
furnishing_type = st.selectbox("Furnishing Type",sorted(df['furnishing_type'].unique().tolist()))

# luxury_category
luxury_category = st.selectbox("Luxury Category",sorted(df['luxury_category'].unique().tolist()))

# floor_category
floor_category = st.selectbox("Floor Category",sorted(df['floor_category'].unique().tolist()))

# button
if st.button("Predict"):
    # form a dataframe
    data = [[property_type, sector ,bedrooms, bathrooms, balcony, property_age, built_up_area, 
             servant_room_value, store_room_value, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)
    st.dataframe(one_df)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22
    
    # display
    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2), round(high,2)))
