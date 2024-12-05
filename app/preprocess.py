import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    # Encoding Education (BS=1, MS=2, PhD=3)
    education_mapping = {"BS": 1, "MS": 2, "PhD": 3, "None": 0}
    df['Education'] = df['Education'].map(education_mapping).fillna(0).astype(int)

    # Convert categorical variables into numeric values (if needed, like "Class A", "Class B", etc.)
    label_encoder = LabelEncoder()
    df['Category'] = label_encoder.fit_transform(df['Category'])  # Map 'Class A', 'Class B', etc. to 0, 1, 2

    # Ensure all columns are numeric
    df = df.apply(pd.to_numeric, errors='coerce')

    # Handle missing values if any
    df = df.fillna(0)

    return df
