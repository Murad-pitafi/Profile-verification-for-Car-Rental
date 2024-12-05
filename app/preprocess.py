import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

# Define the path to your dataset
DATA_PATH = "data/linkedin_profiles_with_categories.csv"

# Load the dataset
def load_data(path):
    return pd.read_csv(path)

# Clean and preprocess the data
def preprocess_data(df):
    # Example column renaming, depending on your CSV structure
    df.columns = [
        "Name",
        "Education Level",
        "Experience (Years)",
        "Experience (Months)",
        "Connections",
        "Recent Post (Months Ago)",
        "Reactions",
        "Comments",
        "Reposts",
        "Class Type"
    ]
    
    # Fill missing values with 0 or appropriate value
    df.fillna(0, inplace=True)

    # Encode 'Education Level' if it's categorical (adjust based on dataset)
    education_mapping = {"PhD": 3, "MS": 2, "BS": 1, "None": 0}
    df["Education Level"] = df["Education Level"].map(education_mapping).fillna(0)

    # Convert data types to numeric
    for col in ["Connections", "Experience (Years)", "Experience (Months)", "Recent Post (Months Ago)", "Reactions", "Comments", "Reposts"]:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    return df

# Save preprocessed data
def save_preprocessed_data(df, train_path="data/train_data.pkl", test_path="data/test_data.pkl"):
    X = df.drop("Class Type", axis=1)
    y = df["Class Type"]
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Save to files
    joblib.dump((X_train, y_train), train_path)
    joblib.dump((X_test, y_test), test_path)
    print("Preprocessed data saved successfully!")

if __name__ == "__main__":
    # Load, preprocess, and save the data
    df = load_data(DATA_PATH)
    processed_df = preprocess_data(df)
    save_preprocessed_data(processed_df)
