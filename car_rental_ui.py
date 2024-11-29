import streamlit as st
import joblib

def load_model():
    return joblib.load("Model/profile_verification_synthetic_model.pkl")

model = load_model()

st.title("Profile Classification App")

# Form for Input Details
with st.form("car_rental_form"):
    st.subheader("User Profile Information")
    
    # Input Fields
    name = st.text_input("Name")
    education_level = st.number_input("Education Level", min_value=0, step=1)
    experience = st.number_input("Experience (Years)", min_value=0, step=1)
    experience_month = st.number_input("Experience (Months)", min_value=0, step=1)
    connections= st.number_input("Connections", min_value=0, step=1)
    recent_post = st.number_input("Recent Post(Months Ago)", min_value=0, step=1)
    reaction_recent_post = st.number_input("Reactions on Recent Post", min_value=0, step=1)
    comments = st.number_input("Comments on Recent Post", min_value=0, step=1)
    repost = st.number_input("Reposts on Recent Post", min_value=0, step=1)
    
    # Submit Button
    predict_button = st.form_submit_button("Predict")
    
    # Action on button click
    if predict_button:
        # Prepare data as required by the model
        input_data = [
            education_level,
            experience,
            experience_month,  
            connections,  
            recent_post, 
            reaction_recent_post, 
            comments, 
            repost,
        ]
        
        # Predict using the loaded model
        prediction = model.predict([input_data])

        # Map the prediction to a friendly label
        class_type_mapping = {2: "A Class Profile ", 1: "C Class Profile", 0: "B Class Profile"}
        verification_status = class_type_mapping.get(prediction[0], "Unknown")

        # Display the result using the mapped status
        st.success(f"Prediction for {name}: {verification_status}")

# Display any additional information as needed
st.write("Complete the form and click Predict to see the result.")
