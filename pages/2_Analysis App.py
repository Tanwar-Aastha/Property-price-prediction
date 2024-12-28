import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="Plotting Demo")

st.title("Analytics")

new_df  =pd.read_csv('data_visual1.csv')
feature_text = pickle.load(open('feature_text.pkl','rb'))

group_df = new_df.groupby(by='sector')[['price', 'price_per_sqft','built_up_area',
                                        'latitude','longitude']].mean()

# Geo map
st.header("Sector Price per Sqft Geomap")
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude",
                        size="built_up_area", 
                        color="price_per_sqft", 
                        zoom=10, 
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        mapbox_style="open-street-map",
                        text=group_df.index,
                        width=1200, height=700, 
                        hover_name=group_df.index)

st.plotly_chart(fig, use_container_width=True)

# Features WorlCloud
st.header("Features Wordcloud")

plt.rcParams['font.family'] = 'Arial'
wordcloud = WordCloud(width=800, 
                      height=800,
                      background_color='white',
                      stopwords=set(['s']),
                      min_font_size=10).generate(feature_text)

fig, ax = plt.subplots(figsize=(8,8), facecolor=None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
plt.tight_layout(pad=0)
st.pyplot(fig)

# Price vs Area scatter plot
st.header("Area Vs Price")

property_type = st.selectbox('Select Property Type',['flat','house'])
if property_type == 'flat':
    fig1  =px.scatter(new_df[new_df['property_type']=='flat'], x='built_up_area', 
                  y='price',
                  color='bedRoom',
                  title='Area Vs Price')
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1  =px.scatter(new_df[new_df['property_type']=='house'], x='built_up_area', 
                  y='price',
                  color='bedRoom',
                  title='Area Vs Price')
    st.plotly_chart(fig1, use_container_width=True)