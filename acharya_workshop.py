#Edit the 8th to 12th line code before upload to github
# Import necessary libraries
import streamlit as st
import seaborn as sns
import plotly.express as px
import pandas as pd


# --- Title and Introduction ---
st.title("Interactive Visualizations with Plotly and Streamlit")


# --- Input for Author Information ---
st.sidebar.header("Visualization skill workshop - Plotly")
name = st.sidebar.text_input(“Shrinidhi Acharya”)
usn = st.sidebar.text_input(“41”)
instructor_name = st.sidebar.text_input(“Ashwini Kumar Mathur”)


# Display author information if provided
if name and usn and instructor_name:
    st.markdown(
        f"<h5 style='color: teal;'>Created by:</h5>"
        f"<p style='color: white;’>{Shrinidhi Acharya} (USN: {41})</p>"
        f"<p style='color: white;'>Instructor: {Ashwini Kumar Mathur}</p>",
        unsafe_allow_html=True
    )


# --- Load Dataset ---
tips = sns.load_dataset('tips')  # Loading the tips dataset


# Display the first few rows of the dataset
st.write("## Dataset Overview")
st.write(tips.head())


# --- Task 2: Interactive Bar Chart ---
st.subheader("Task 2: Bar Chart - Average Tip by Day")
# Bar Chart: Average Tip by Day with color for each day
fig2 = px.bar(
    tips, x='day', y='tip', color='day',
    title='Average Tip by Day',
    labels={'tip': 'Average Tip ($)', 'day': 'Day of the Week'},
    template='plotly_white'
)
st.plotly_chart(fig2)  # Display the chart in Streamlit

#4. Scatter Plot: Total Bill vs. Tip (Color-coded by Gender)
# Write the code below this line
fig4 = px.scatter(
dataset, x='total_bill', y='tip', color='sex',
title='Total bill vs tip(colored by gender)',
labels={'totalbill':'Total Bill ($)', 'tip':'Tip($)' },
template='plotly_dark', #clean cool dark background
size='size'
)
fig4.show()
