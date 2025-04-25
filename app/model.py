import joblib
import numpy as np

# Charger le vrai modèle IA préentraîné
model = joblib.load("model/emotion_model.pkl")

def predict_emotion_with_proba(features):
    features = np.array(features).reshape(1, -1)
    proba = model.predict_proba(features)[0]
    classes = model.classes_
    proba_dict = dict(zip(classes, proba))
    emotion = classes[np.argmax(proba)]
    return emotion, proba_dict
