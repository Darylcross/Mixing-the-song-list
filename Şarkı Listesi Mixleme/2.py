import os
import random
import shutil

# Sıralı MP3 dosyalarının bulunduğu kaynak klasör yolu
kaynak_klasor = "C:/Users/baros/OneDrive/Masaüstü/Yeni klasör/new"  # Bu yolu kendi kaynak klasör yoluma değiştirin

# Hedef klasörünüzü belirleyin
hedef_klasor = "C:/Users/baros/OneDrive/Masaüstü/Yeni klasör/arzu"  # Bu yolu kendi hedef klasör yoluma değiştirin

mp3_dosyalari = [dosya for dosya in os.listdir(kaynak_klasor) if dosya.endswith('.mp3')]



# MP3 dosyalarını karışık bir şekilde sırala
random.shuffle(mp3_dosyalari)

# Hedef klasörü oluşturun (varsa geçersiz kılın)
if not os.path.exists(hedef_klasor):
    os.makedirs(hedef_klasor)

# MP3 dosyalarını hedef klasöre kopyala
for mp3_dosyasi in mp3_dosyalari:
    kaynak_mp3 = os.path.join(kaynak_klasor, mp3_dosyasi)
    hedef_mp3 = os.path.join(hedef_klasor, mp3_dosyasi)
    shutil.copy(kaynak_mp3, hedef_mp3)

print("MP3 dosyaları başarıyla kopyalandı.")
