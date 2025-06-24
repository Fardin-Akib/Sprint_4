import streamlit as st 
import pandas as pd
import plotly.express as px

st.header("Sprint Four")
st.subheader("Vehicle Dashboard")
st.write("In this project you will see a historgram and scatterplot I quickly made from the 'vehicle_us.csv' dataset." \
"In the Histogram you will see the odometer reading for each brand of cars sold. In the scatterplot you will see a correlation between" \
"model year of a car and the price it was sold at.")

df = pd.read_csv('vehicles_us.csv')

for model in df['model'].unique():
    median_value = df[df['model'] == model]['cylinders'].median()
    
    df.loc[df['model']==model, 'cylinders'] = df.loc[df['model']==model, 'cylinders'].fillna(median_value)

df['is_4wd'] = df['is_4wd'].fillna(0.0)

df = df.dropna()

year_price_scatter = px.scatter(df, x="model_year", y="price", title="Price vs Model Year")
year_price_scatter.update_layout(
    xaxis_title="Model Year",
    yaxis_title="Price",
    title= "Price vs Model Year"
)
scatter_button = st.button("Scatter")

if scatter_button:
    st.plotly_chart(year_price_scatter)

brand_vs_odometer = px.histogram(df, x="model" , y="odometer", title= "Distance Travel via Brand")
brand_vs_odometer.update_layout(
    xaxis_title= "Model",
    yaxis_title= "Odometer",
    title= "Brand and Odometer Correlation"
)
histogram_button = st.button("Histogram")

if histogram_button:
    st.plotly_chart(brand_vs_odometer)

