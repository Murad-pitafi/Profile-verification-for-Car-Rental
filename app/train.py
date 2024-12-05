import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Define paths to preprocessed data
TRAIN_DATA_PATH = "data/train_data.pkl"
TEST_DATA_PATH = "data/test_data.pkl"
MODEL_SAVE_PATH = "Model/profile_verification_synthetic_model.pkl"

# Load preprocessed data
def load_data(train_path, test_path):
    X_train, y_train = joblib.load(train_path)
    X_test, y_test = joblib.load(test_path)
    return X_train, y_train, X_test, y_test

# Train the model using Logistic Regression
def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

# Save the trained model
def save_model(model, path):
    joblib.dump(model, path)
    print(f"Model saved to {path}")

if __name__ == "__main__":
    # Load data
    X_train, y_train, X_test, y_test = load_data(TRAIN_DATA_PATH, TEST_DATA_PATH)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    evaluate_model(model, X_test, y_test)

    # Save the trained model
    save_model(model, MODEL_SAVE_PATH)
