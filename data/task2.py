import kagglehub
import shutil
import os

# Download latest version
path = kagglehub.dataset_download("adrianmcmahon/imdb-india-movies")

destination_path = r"C:\Users\user\Desktop\ENCRYPTIX Data Science Internship\data"

# Buat folder tujuan jika belum adacreate destination folder if it's haven't
os.makedirs(destination_path, exist_ok=True)

# move the dataset to destination folder
for file_name in os.listdir(path):
    shutil.move(os.path.join(path, file_name), destination_path)

print("Dataset successfully moved to:", destination_path)