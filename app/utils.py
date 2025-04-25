import os
import csv
from datetime import datetime

def ensure_data_folder():
    if not os.path.exists('data'):
        os.makedirs('data')

def save_prediction_to_csv(emotion, file_path, output_file="data/history.csv"):
    ensure_data_folder()  # Assurer que data/ existe
    with open(output_file, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), emotion, file_path])
