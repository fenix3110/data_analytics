import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv("sample_data.csv")

# Create pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression(max_iter=1000))
])

# Train model
pipeline.fit(df["text"], df["category"])

# Save model
joblib.dump(pipeline, "classify_model.pkl")
print("✅ Model trained and saved as 'classify_model.pkl'")
