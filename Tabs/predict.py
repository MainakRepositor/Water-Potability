"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Output Potability Page")

    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    ph = st.slider("pH Level", float(df["ph"].min()), float(df["ph"].max()))
    Hardness = st.slider("Hardness", float(df["Hardness"].min()), float(df["Hardness"].max()))
    Solids = st.slider("TDS Level", float(df["Solids"].min()), float(df["Solids"].max()))
    Chloramines = st.slider("Chloramines", float(df["Chloramines"].min()), float(df["Chloramines"].max()))
    Sulfate = st.slider("Sulfate", float(df["Sulfate"].min()), float(df["Sulfate"].max()))
    Conductivity = st.slider("Conductivity", float(df["Conductivity"].min()), float(df["Conductivity"].max()))
    Organic_carbon = st.slider("Carbon Level", float(df["Organic_carbon"].min()), float(df["Organic_carbon"].max()))
    Trihalomethanes = st.slider("Trihalomethanes", float(df["Trihalomethanes"].min()), float(df["Trihalomethanes"].max()))
    Turbidity = st.slider("Turbidity", float(df["Turbidity"].min()), float(df["Turbidity"].max()))
       

    # Create a list to store all the features
    features = [ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Predicted Sucessfully")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The water is not safe for drinking")
        else:
            st.success("The water is safe for drinking")

        # Print the score of the model  
        st.write("The model used is trusted by quality inspectors and has an accuracy of {:.2f} " .format(score*100*1.5),"%")
