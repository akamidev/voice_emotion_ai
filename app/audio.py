import sounddevice as sd
from scipy.io.wavfile import write
def record_audio(duration=10, filename="data/voice_input.wav"):
    fs = 44100  # 44.1 kHz
    print("🎙️ Enregistrement en cours... Parle maintenant !")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print(f"✅ Enregistrement terminé : {filename}")
