import joblib
import os
from dotenv import load_dotenv
from app.text_preprocessing import preprocess_text

load_dotenv()

# Load the model and vectorizer
MODEL_PATH = os.getenv("MODEL_PATH")
VECTORIZER_PATH = os.getenv("VECTORIZER_PATH")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def make_prediction(raw_text: str):
    
    clean_text = preprocess_text(raw_text)
    
    # Vectorize
    vectorized_input = vectorizer.transform([clean_text])
    
    # Predict
    prediction = model.predict(vectorized_input)[0]
    probabilities = model.predict_proba(vectorized_input)[0]
    
    
    label = "Fake" if prediction == 1 else "Real"
    confidence = float(max(probabilities))
    
    return label, confidence