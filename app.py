import os
import ctypes
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

# Directory to save wallpapers
WALLPAPER_DIR = "wallpapers"
if not os.path.exists(WALLPAPER_DIR):
    os.makedirs(WALLPAPER_DIR)

# URL of the webpage containing the wallpapers
URL = "https://www.wsupercars.com/ultrawide-wallpapers/"

# Function to download wallpaper images
def download_wallpapers():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    images = soup.find_all('img', class_='attachment-large')

    downloaded_files = []

    for img in images:
        img_url = img['src']
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        img_name = os.path.join(WALLPAPER_DIR, img_url.split('/')[-1])

        # Download and save the image
        img_data = requests.get(img_url).content
        with open(img_name, 'wb') as img_file:
            img_file.write(img_data)
            downloaded_files.append(img_name)
            print(f"Downloaded: {img_name}")
    
    return downloaded_files

# Function to set wallpaper on Windows
def set_wallpaper(image_path):
    abs_path = os.path.abspath(image_path)
    # Set wallpaper on Windows using ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 0)
    print(f"Wallpaper set to: {abs_path}")

# Main function
def main():
    wallpapers = download_wallpapers()
    
    if wallpapers:
        set_wallpaper(wallpapers[0])  # Set the first downloaded wallpaper as the desktop wallpaper
    else:
        print("No wallpapers downloaded.")

if __name__ == "__main__":
    main()
