# # import streamlit as st
# # import joblib

# # def load_model():
# #     return joblib.load("Model/profile_verification_synthetic_model.pkl")

# # model = load_model()

# # st.title("Profile Classification App")

# # # Form for Input Details
# # with st.form("car_rental_form"):
# #     st.subheader("User Profile Information")
    
# #     # Input Fields
# #     name = st.text_input("Name")
# #     education_level = st.number_input("Education Level", min_value=0, step=1)
# #     experience = st.number_input("Experience (Years)", min_value=0, step=1)
# #     experience_month = st.number_input("Experience (Months)", min_value=0, step=1)
# #     connections= st.number_input("Connections", min_value=0, step=1)
# #     recent_post = st.number_input("Recent Post(Months Ago)", min_value=0, step=1)
# #     reaction_recent_post = st.number_input("Reactions on Recent Post", min_value=0, step=1)
# #     comments = st.number_input("Comments on Recent Post", min_value=0, step=1)
# #     repost = st.number_input("Reposts on Recent Post", min_value=0, step=1)
    
# #     # Submit Button
# #     predict_button = st.form_submit_button("Predict")
    
# #     # Action on button click
# #     if predict_button:
# #         # Prepare data as required by the model
# #         input_data = [
# #             education_level,
# #             experience,
# #             experience_month,  
# #             connections,  
# #             recent_post, 
# #             reaction_recent_post, 
# #             comments, 
# #             repost,
# #         ]
        
# #         # Predict using the loaded model
# #         prediction = model.predict([input_data])

# #         # Map the prediction to a friendly label
# #         class_type_mapping = {2: "A Class Profile ", 1: "C Class Profile", 0: "B Class Profile"}
# #         verification_status = class_type_mapping.get(prediction[0], "Unknown")

# #         # Display the result using the mapped status
# #         st.success(f"Prediction for {name}: {verification_status}")

# # # Display any additional information as needed
# # st.write("Complete the form and click Predict to see the result.")
# # app.py
# # import streamlit as st
# # from pipeline import process_file

# # # Title for the app
# # st.title("Profile Classification App")

# # # Option 1: Manual input form
# # with st.expander("Enter Profile Details Manually"):
# #     st.subheader("User Profile Information")
    
# #     name = st.text_input("Name")
# #     education_level = st.number_input("Education Level", min_value=0, step=1)
# #     experience = st.number_input("Experience (Years)", min_value=0, step=1)
# #     experience_month = st.number_input("Experience (Months)", min_value=0, step=1)
# #     connections = st.number_input("Connections", min_value=0, step=1)
# #     recent_post = st.number_input("Recent Post(Months Ago)", min_value=0, step=1)
# #     reaction_recent_post = st.number_input("Reactions on Recent Post", min_value=0, step=1)
# #     comments = st.number_input("Comments on Recent Post", min_value=0, step=1)
# #     repost = st.number_input("Reposts on Recent Post", min_value=0, step=1)

# #     predict_button = st.form_submit_button("Predict")
    
# #     if predict_button:
# #         input_data = [
# #             education_level,  # Education
# #             experience,  # Experience (Years)
# #             experience_month,  # Experience (Months)
# #             connections,  # Connections
# #             recent_post,  # Recent Post
# #             reaction_recent_post,  # Reactions on Recent Post
# #             comments,  # Comments on Recent Post
# #             repost,  # Repost Count on Recent Post
# #         ]

# #         # Predict using the model
# #         verification_status = predict_profile_classification(input_data)

# #         st.success(f"Prediction for {name}: {verification_status}")

# # # Option 2: Paste LinkedIn Profile Data
# # with st.expander("Paste LinkedIn Profile Data"):
# #     st.subheader("Paste LinkedIn Profile Text Below")

# #     linkedin_data = st.text_area("Paste LinkedIn Profile", height=300)

# #     if linkedin_data:
# #         # Save the pasted LinkedIn data into a temporary text file
# #         with open("linkedin_profile.txt", "w") as file:
# #             file.write(linkedin_data)

# #         # Process the file to extract data
# #         results = process_file("linkedin_profile.txt")

# #         # Display extracted information
# #         st.write("Extracted Information:")
# #         st.write(results)

# #         # Prepare the input data for prediction
# #         input_data = [
# #             results.get("Education", 1),  # Education (default to 1 if not available)
# #             results.get("Experience (Years)", 1),  # Experience (Years)
# #             results.get("Experience (Months)", 1),  # Experience (Months)
# #             results.get("Connections", 1),  # Connections
# #             results.get("Recent Post", 1),  # Recent Post
# #             results.get("Reactions on Recent Post", 1),  # Reactions on Recent Post
# #             results.get("Comments on Recent Post", 1),  # Comments on Recent Post
# #             results.get("Repost Count on Recent Post", 1),  # Repost Count on Recent Post
# #         ]

# #         # Predict using the model
# #         verification_status = predict_profile_classification(input_data)

# #         st.success(f"Prediction for LinkedIn Profile: {verification_status}")

# # app.py
# import streamlit as st
# from pipeline import process_file

# # Title for the app
# st.title("Profile Classification App")

# # Option 1: Manual input form
# with st.expander("Enter Profile Details Manually"):
#     st.subheader("User Profile Information")
    
#     # Wrap manual input fields inside a form
#     with st.form(key="manual_form"):
#         name = st.text_input("Name")
#         education_level = st.number_input("Education Level", min_value=0, step=1)
#         experience = st.number_input("Experience (Years)", min_value=0, step=1)
#         experience_month = st.number_input("Experience (Months)", min_value=0, step=1)
#         connections = st.number_input("Connections", min_value=0, step=1)
#         recent_post = st.number_input("Recent Post(Months Ago)", min_value=0, step=1)
#         reaction_recent_post = st.number_input("Reactions on Recent Post", min_value=0, step=1)
#         comments = st.number_input("Comments on Recent Post", min_value=0, step=1)
#         repost = st.number_input("Reposts on Recent Post", min_value=0, step=1)

#         # Submit button for the form
#         predict_button = st.form_submit_button("Predict")
        
#         if predict_button:
#             input_data = [
#                 education_level,  # Education
#                 experience,  # Experience (Years)
#                 experience_month,  # Experience (Months)
#                 connections,  # Connections
#                 recent_post,  # Recent Post
#                 reaction_recent_post,  # Reactions on Recent Post
#                 comments,  # Comments on Recent Post
#                 repost,  # Repost Count on Recent Post
#             ]

#             # Predict using the model
#             verification_status = predict_profile_classification(input_data)

#             st.success(f"Prediction for {name}: {verification_status}")

# # Option 2: Paste LinkedIn Profile Data
# with st.expander("Paste LinkedIn Profile Data"):
#     st.subheader("Paste LinkedIn Profile Text Below")

#     linkedin_data = st.text_area("Paste LinkedIn Profile", height=300)

#     if linkedin_data:
#         # Save the pasted LinkedIn data into a temporary text file
#         with open("linkedin_profile.txt", "w") as file:
#             file.write(linkedin_data)

#         # Process the file to extract data
#         results = process_file("linkedin_profile.txt")

#         # Display extracted information
#         st.write("Extracted Information:")
#         st.write(results)

#         # Prepare the input data for prediction
#         input_data = [
#             results.get("Education", 1),  # Education (default to 1 if not available)
#             results.get("Experience (Years)", 1),  # Experience (Years)
#             results.get("Experience (Months)", 1),  # Experience (Months)
#             results.get("Connections", 1),  # Connections
#             results.get("Recent Post", 1),  # Recent Post
#             results.get("Reactions on Recent Post", 1),  # Reactions on Recent Post
#             results.get("Comments on Recent Post", 1),  # Comments on Recent Post
#             results.get("Repost Count on Recent Post", 1),  # Repost Count on Recent Post
#         ]

#         # Predict using the model
#         verification_status = predict_profile_classification(input_data)

#         st.success(f"Prediction for LinkedIn Profile: {verification_status}")

import streamlit as st
from pipeline import process_file
import re
import joblib

# Load the model
def load_model():
    return joblib.load("Model/profile_verification_synthetic_model.pkl")

# Preprocess the input data
def preprocess_data(results):
    # 1. Convert Education (e.g., "MS", "PhD") to numerical values
    education_mapping = {"PhD": 3, "MS": 2, "BS": 1, "None": 0}
    education = education_mapping.get(results.get("Education", "None"), 0)

    # 2. Convert Connections (e.g., "500+") to a number
    connections = results.get("Connections", "0")
    if "+" in connections:
        connections = int(connections.split("+")[0])
    else:
        connections = int(connections)

    # 3. Convert Recent Post (e.g., "2 months", "1 year") to number of months
    recent_post = results.get("Recent Post", "0 months")
    months = 0
    if "mo" in recent_post:
        months = int(re.search(r"(\d+)\s*mo", recent_post).group(1))
    elif "yr" in recent_post:
        months = int(re.search(r"(\d+)\s*yr", recent_post).group(1)) * 12
    elif "d" in recent_post:
        months = 0  # You can choose to map days to a number if needed

    # 4. Convert Reactions, Comments, Reposts to numbers (default to 1 if missing)
    reactions = int(results.get("Reactions on Recent Post", 1))
    comments = int(results.get("Comments on Recent Post", 1))
    reposts = int(results.get("Repost Count on Recent Post", 1))

    # 5. Return preprocessed input data
    input_data = [
        education,  # Education level as number
        results.get("Experience (Years)", 0),  # Experience (Years)
        results.get("Experience (Months)", 0),  # Experience (Months)
        connections,  # Connections (as number)
        months,  # Recent Post (in months)
        reactions,  # Reactions
        comments,  # Comments
        reposts,  # Reposts
    ]
    
    return input_data

# Define the function for making predictions
def predict_profile_classification(input_data):
    model = load_model()
    prediction = model.predict([input_data])
    
    # Map prediction to profile status
    class_type_mapping = {2: "A Class Profile", 1: "C Class Profile", 0: "B Class Profile"}
    verification_status = class_type_mapping.get(prediction[0], "Unknown")
    
    return verification_status


# Title for the app
st.title("Profile Classification App")

# Option 1: Manual input form
with st.expander("Enter Profile Details Manually"):
    st.subheader("User Profile Information")
    
    # Wrap manual input fields inside a form
    with st.form(key="manual_form"):
        name = st.text_input("Name")
        education_level = st.number_input("Education Level", min_value=0, step=1)
        experience = st.number_input("Experience (Years)", min_value=0, step=1)
        experience_month = st.number_input("Experience (Months)", min_value=0, step=1)
        connections = st.number_input("Connections", min_value=0, step=1)
        recent_post = st.number_input("Recent Post(Months Ago)", min_value=0, step=1)
        reaction_recent_post = st.number_input("Reactions on Recent Post", min_value=0, step=1)
        comments = st.number_input("Comments on Recent Post", min_value=0, step=1)
        repost = st.number_input("Reposts on Recent Post", min_value=0, step=1)

        # Submit button for the form
        predict_button = st.form_submit_button("Predict")
        
        if predict_button:
            input_data = [
                education_level,  # Education
                experience,  # Experience (Years)
                experience_month,  # Experience (Months)
                connections,  # Connections
                recent_post,  # Recent Post
                reaction_recent_post,  # Reactions on Recent Post
                comments,  # Comments on Recent Post
                repost,  # Repost Count on Recent Post
            ]

            # Predict using the model
            verification_status = predict_profile_classification(input_data)

            st.success(f"Prediction for {name}: {verification_status}")

# Option 2: Paste LinkedIn Profile Data
with st.expander("Paste LinkedIn Profile Data"):
    st.subheader("Paste LinkedIn Profile Text Below")

    linkedin_data = st.text_area("Paste LinkedIn Profile", height=300)

    if linkedin_data:
        # Save the pasted LinkedIn data into a temporary text file
        with open("linkedin_profile.txt", "w",  encoding='utf-8') as file:
            file.write(linkedin_data)

        # Process the file to extract data
        results = process_file("linkedin_profile.txt")

        # Display extracted information
        # st.write("Extracted Information:")
        # st.write(results)

        # Preprocess the extracted data
        input_data = preprocess_data(results)

        # Predict using the model
        verification_status = predict_profile_classification(input_data)

        st.success(f"Prediction for LinkedIn Profile: {verification_status}")
