import customtkinter as ctk
from app.audio import record_audio
from app.features import extract_features
from app.model import predict_emotion_with_proba
from app.utils import save_prediction_to_csv
from app.face_emotion import detect_emotion_live_tk
from PIL import Image, ImageTk
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class EmotionApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Voice Emotion AI AKAMI")
        self.geometry("500x650")

        self.label_title = ctk.CTkLabel(self, text="🎙️ Détection d’émotion vocale", font=("Arial", 20))
        self.label_title.pack(pady=10)

        self.btn_record = ctk.CTkButton(self, text="🎤 Parler", command=self.start_analysis_thread, width=200)
        self.btn_record.pack(pady=10)

        self.btn_face = ctk.CTkButton(self, text="📸 Détecter Visage", command=self.start_face_detection_thread, width=200)
        self.btn_face.pack(pady=10)

        self.btn_reset = ctk.CTkButton(self, text="♻️ Réinitialiser", command=self.reset_graph, width=200)
        self.btn_reset.pack(pady=5)

        self.label_status = ctk.CTkLabel(self, text="Aucune détection encore", font=("Arial", 14))
        self.label_status.pack(pady=10)

        self.plot_canvas = None

        self.video_label = ctk.CTkLabel(self, text="")
        self.video_label.pack(pady=10)

    def start_analysis_thread(self):
        thread = threading.Thread(target=self.analyze_voice)
        thread.start()

    def analyze_voice(self):
        self.label_status.configure(text="⏳ Enregistrement en cours... Parle maintenant !")
        record_audio()
        self.label_status.configure(text="⚙️ Analyse en cours...")

        features = extract_features("data/voice_input.wav")
        emotion, proba_dict = predict_emotion_with_proba(features)
        self.label_status.configure(text=f"🧠 Émotion détectée : {emotion}")

        save_prediction_to_csv(emotion, "data/voice_input.wav")
        self.after(0, lambda: self.plot_emotion_bar(proba_dict))

    def plot_emotion_bar(self, proba_dict):
        if self.plot_canvas:
            self.plot_canvas.get_tk_widget().destroy()

        fig, ax = plt.subplots(figsize=(6, 4))

        emotions = list(proba_dict.keys())
        scores = list(proba_dict.values())

        ax.bar(emotions, scores, color='skyblue')
        ax.set_ylim(0, 1)
        ax.set_ylabel("Probabilité", fontsize=12)
        ax.set_title("Prédiction des émotions", fontsize=14)
        ax.tick_params(axis='x', labelrotation=25, labelsize=10)
        ax.tick_params(axis='y', labelsize=10)
        fig.subplots_adjust(bottom=0.3)

        self.plot_canvas = FigureCanvasTkAgg(fig, master=self)
        self.plot_canvas.draw()
        self.plot_canvas.get_tk_widget().pack(pady=10)

    def reset_graph(self):
        if self.plot_canvas:
            self.plot_canvas.get_tk_widget().destroy()
            self.plot_canvas = None
        self.video_label.configure(image="")
        self.label_status.configure(text="📉 Graphique réinitialisé.")

    def start_face_detection_thread(self):
        thread = threading.Thread(target=lambda: detect_emotion_live_tk(self.video_label))
        thread.start()


if __name__ == "__main__":
    app = EmotionApp()
    app.mainloop()
