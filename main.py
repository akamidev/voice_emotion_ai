from app.audio import record_audio
from app.features import extract_features
from app.model import predict_emotion
from app.utils import ensure_data_folder

def main():
    ensure_data_folder()
    record_audio()
    features = extract_features("data/voice_input.wav")
    emotion = predict_emotion(features)
    print(f"🧠 Émotion détectée : {emotion}")

if __name__ == "__main__":
    main()
