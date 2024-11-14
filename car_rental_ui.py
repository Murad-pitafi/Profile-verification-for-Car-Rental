import streamlit as st
import joblib

def load_model():
    return joblib.load("Model/profile_verification_model.pkl")

model = load_model()

st.title("Profile Classification App")

# Form for Input Details
with st.form("car_rental_form"):
    st.subheader("User Profile Information")
    
    # Input Fields
    name = st.text_input("Name")
    experience = st.number_input("Experience (Years)", min_value=0, step=1)
    education_level = st.number_input("Education Level", min_value=0, step=1)
    followers = st.number_input("Followers", min_value=0, step=1)
    skill_endorsements = st.number_input("Skill Endorsements", min_value=0, step=1)
    recommendations = st.number_input("Recommendations", min_value=0, step=1)
    activity = st.number_input("Activity", min_value=0, step=1)
    projects = st.number_input("Projects", min_value=0, step=1)
    certificates = st.number_input("Certificates", min_value=0, step=1)
    
    # Submit Button
    predict_button = st.form_submit_button("Predict")
    
    # Action on button click
    if predict_button:
        # Prepare data as required by the model
        input_data = [
            experience, 
            education_level, 
            followers, 
            skill_endorsements, 
            recommendations, 
            activity, 
            projects, 
            certificates,
        ]
        
        # Predict using the loaded model
        prediction = model.predict([input_data])

        # Map the prediction to a friendly label
        class_type_mapping = {2: "Type A", 1: "Type C", 0: "Type B"}
        verification_status = class_type_mapping.get(prediction[0], "Unknown")

        # Display the result using the mapped status
        st.success(f"Prediction for {name}: {verification_status}")

# Display any additional information as needed
st.write("Complete the form and click Predict to see the result.")
