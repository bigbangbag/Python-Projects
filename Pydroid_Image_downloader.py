import requests
import os

# URL of the image to download
image_url = "https://t4.ftcdn.net/jpg/04/49/63/29/360_F_449632947_2lGNlALitIkk8dUL8zY4a4OVDNS0dZQ8.webp"
save_path = "/storage/emulated/0/Download/example.webp"  # you can replace "example.webp"

# Download the image
response = requests.get(image_url)
if response.status_code == 200:
    with open(save_path, "wb") as file:
        file.write(response.content)
    print(f"Image successfully downloaded to: {save_path}")
else:
    print(f"Failed to download image. Status code: {response.status_code}")
