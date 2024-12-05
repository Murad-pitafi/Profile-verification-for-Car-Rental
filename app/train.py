import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from preprocess import preprocess_data
import os
current_dir = os.path.dirname(os.path.realpath(__file__))

# Define the relative path to your dataset
data_file_path = os.path.join(current_dir, '..', 'data', 'linkedin_profiles_with_categories.csv')

# Load your dataset
def load_data():
    # Assuming you have the CSV file path
    df = pd.read_csv(data_file_path)

    # Preprocess the data
    df = preprocess_data(df)

    # Split into features and target variable
    X = df.drop('Category', axis=1)
    y = df['Category']
    
    return X, y

# Train the model
def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

# Save the trained model
def save_model(model):
    joblib.dump(model, 'profile_verification_synthetic_model.pkl')

# Main function to load data, train model, and save
if __name__ == "__main__":
    # Load the data
    X, y = load_data()

    # Split into training and testing datasets (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model on test data
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    # Save the trained model
    save_model(model)
