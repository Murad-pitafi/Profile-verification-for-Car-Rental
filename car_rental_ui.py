import streamlit as st
import joblib

def load_model():
    return joblib.load("Model/profile_verification_model.pkl")

model = load_model()

st.title("Car Rental Prediction System")

# Form for Input Details
with st.form("car_rental_form"):
    st.subheader("User Profile Information")
    
    # Input Fields
    username = st.text_input("Username")
    headline = st.text_input("Headline")
    no_of_license_certificates = st.number_input("Number of Licenses and Certificates", min_value=0, step=1)
    job_title = st.text_input("Job Title")
    company_verified = st.selectbox("Company Verified", options=["Yes", "No"])
    no_of_companies_worked = st.number_input("Number of Companies Worked", min_value=0, step=1)
    followers = st.number_input("Followers", min_value=0, step=1)
    
    # Submit Button
    predict_button = st.form_submit_button("Predict")
    
    # Action on button click
    if predict_button:
        # Convert "Yes"/"No" to binary as required by the model
        company_verified_binary = 1 if company_verified == "Yes" else 0

        # Prepare data as required by the model
        input_data = [
            headline, 
            no_of_license_certificates, 
            job_title, 
            company_verified_binary, 
            no_of_companies_worked, 
            followers, 
        ]
        
        # Predict using the loaded model
        prediction = model.predict([input_data])

        # Map the prediction to a friendly label
        if prediction[0] == 1:
            verification_status = "Verified"
            
        else: 
            verification_status= "Not Verified"

        # Display the result using the mapped status
        st.success(f"Prediction for {username}: {verification_status}")

# Display the result or any additional information as needed
st.write("Complete the form and click Predict to see the result.")
