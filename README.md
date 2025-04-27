# 🤖 Voice Emotion AI AKAMI

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![DeepFace](https://img.shields.io/badge/DeepFace-Facial_Recognition-00CED1?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-4.11.0-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-CustomTK-303030?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Graphiques-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)

---

## 🎯 Objectif

**Voice Emotion AI AKAMI** est une application de bureau qui détecte les émotions à partir :
- de la **voix** (enregistrement audio + classification émotionnelle),
- du **visage** (caméra en direct avec DeepFace).

L’objectif est d’expérimenter la détection multi-modale d’émotions dans un environnement interactif avec une interface moderne.

---

## 🖥️ Démonstration de l’application

<img src="./Emotion vocal et facial.png" alt="Détection Émotion Vocale et Faciale" width="500"/

---

## 🧠 Fonctionnalités

- 🎤 Détection vocale via micro
- 📸 Détection d’émotions faciales avec DeepFace
- 📊 Graphique matplotlib des probabilités
- ♻️ Bouton de réinitialisation du graphique
- 💾 Sauvegarde automatique des prédictions dans un fichier CSV

---

## 🚀 Technologies Utilisées

- **Python 3.12**
- **TensorFlow / DeepFace** : classification émotionnelle
- **OpenCV** : accès webcam
- **CustomTkinter** : interface stylée
- **Matplotlib** : rendu des graphiques
- **PIL / ImageTk** : intégration image live dans Tkinter

---

## 🛠️ Installation & Lancement

```bash
# 1. Cloner le dépôt
git clone https://github.com/votreNomUtilisateur/voice_emotion_ai.git
cd voice_emotion_ai

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'application
python -m app.ui

