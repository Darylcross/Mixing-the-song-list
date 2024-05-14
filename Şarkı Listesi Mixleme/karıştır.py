import os
import random
import shutil

# Rastgele sayı üretecinizi başlatın
random.seed(0)

mp3_folder = "C:/Users/baros/OneDrive/Masaüstü/Yeni klasör/arzu"
mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith(".mp3")]

# Dosyaları rastgele sırala
random.shuffle(mp3_files)

destination_folder = "C:/Users/baros/OneDrive/Masaüstü/Yeni klasör/new"

for mp3_file in mp3_files:
    source_path = os.path.join(mp3_folder, mp3_file)
    destination_path = os.path.join(destination_folder, mp3_file)
    shutil.move(source_path, destination_path)
