import os

mp3_folder = "C:/Users/baros/OneDrive/Masaüstü/Yeni klasör/arzu"
mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith(".mp3")]
for i, mp3_file in enumerate(mp3_files, start=1):
    new_name = f"{i:03d}.mp3"  # Örnek: 001.mp3, 002.mp3, ...
    old_path = os.path.join(mp3_folder, mp3_file)
    new_path = os.path.join(mp3_folder, new_name)
    os.rename(old_path, new_path)
