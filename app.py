import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('data.csv')

st.set_page_config(page_title="Airline Demand Dashboard", layout="wide")
st.title("✈️ Airline Booking Market Demand Insights")

# Filters
st.sidebar.header("Filter Flights")
cities = sorted(set(df['From'].dropna().unique()))
selected_city = st.sidebar.selectbox("Select Departure City", cities)

filtered_df = df[df['From'] == selected_city]

# Show table
st.subheader(f"Flights from {selected_city}")
st.dataframe(filtered_df)

# Plot most popular destinations from that city
popular_routes = filtered_df['To'].value_counts().head(10).reset_index()
popular_routes.columns = ['Destination', 'Number of Flights']

fig = px.bar(popular_routes, x='Destination', y='Number of Flights', title=f"Top Destinations from {selected_city}")
st.plotly_chart(fig)
