import cv2
from deepface import DeepFace
from PIL import Image, ImageTk

def detect_emotion_live_tk(video_label):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Impossible d'ouvrir la caméra.")
        return

    print("📸 Caméra démarrée. Appuie sur 'q' pour quitter.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            result = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)
            emotion = result[0]["dominant_emotion"]

            # Traduction des émotions en français
            emotions_fr = {
                "neutral": "😐 Neutre",
                "happy": "😊 Heureux",
                "sad": "😢 Triste",
                "angry": "😠 En colère",
                "fear": "😨 Peur",
                "surprise": "😲 Surprise",
                "disgust": "🤢 Dégoût"
            }

            label = f"Émotion : {emotions_fr.get(emotion, emotion)}"
            cv2.putText(frame, label, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        except:
            cv2.putText(frame, "Pas de visage détecté", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Convertir l'image OpenCV en image Tkinter
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb_frame)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.configure(image=imgtk)
        video_label.image = imgtk

        # Pour éviter un freeze complet de l’UI
        video_label.update_idletasks()

        # Appuie sur Q pour quitter
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    video_label.configure(image="")
    print("🛑 Caméra arrêtée.")
