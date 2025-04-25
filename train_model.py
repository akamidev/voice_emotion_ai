import os
import numpy as np
import librosa
import joblib
from sklearn.ensemble import RandomForestClassifier

# Dictionnaire des 8 émotions du dataset RAVDESS
emotions = {
    '01': '😐 Neutre',
    '02': '😌 Calme',
    '03': '😊 Heureux',
    '04': '😢 Triste',
    '05': '😡 En colère',
    '06': '😱 Peur',
    '07': '🤢 Dégoûté',
    '08': '😮 Surpris'
}

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfcc.T, axis=0)

def load_data(dataset_path):
    X, y = [], []
    for file in os.listdir(dataset_path):
        if file.endswith('.wav'):
            emotion_code = file.split('-')[2]
            if emotion_code in emotions:
                features = extract_features(os.path.join(dataset_path, file))
                X.append(features)
                y.append(emotions[emotion_code])
    print(f"📊 Total fichiers utilisés : {len(X)}")
    return np.array(X), np.array(y)

if __name__ == "__main__":
    print("📁 Chargement des données...")
    X, y = load_data("ravdess")

    print("🧠 Entraînement du modèle...")
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X, y)

    joblib.dump(clf, "model/emotion_model.pkl")
    print("✅ Modèle enregistré dans model/emotion_model.pkl")
