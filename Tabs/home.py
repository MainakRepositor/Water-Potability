"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Water Quality Inspector")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            This system incorporates advanced data analysis to gather real-time data on water parameters such as radiation level, bacteria concentration, dissolved salts, and chemical contaminants. The collected data is then analyzed and processed by the AI algorithms, which can quickly detect anomalies, identify potential pollutants, and assess the overall water health, thus making a sustainable health solution possible.
        </p>
    """, unsafe_allow_html=True)