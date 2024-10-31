import streamlit as st

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
        # Here you could call your prediction model with the entered data
        st.success(f"Prediction in progress for user: {username}")

# Display the result or any additional information as needed
st.write("Complete the form and click Predict to see the result.")
