import requests
import json
import os
from pathlib import Path

# Replace with your Unsplash API access key
ACCESS_KEY = "your_unsplash_api_access_key"

# Unsplash API endpoint for searching photos
SEARCH_ENDPOINT = "https://api.unsplash.com/search/photos"

# Directory to save the images
SAVE_DIR = "south_africa_segregation_images"
Path(SAVE_DIR).mkdir(parents=True, exist_ok=True)

def fetch_images(query, per_page=10, page=1):
    headers = {
        "Accept-Version": "v1",
        "Authorization": f"Client-ID {ACCESS_KEY}"
    }

    params = {
        "query": query,
        "per_page": per_page,
        "page": page
    }

    response = requests.get(SEARCH_ENDPOINT, headers=headers, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data['results']
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
    else:
        print(f"Error {response.status_code}: {response.text}")

# Fetch images related to South African segregation
search_query = "south africa segregation"
images = fetch_images(search_query)

if images:
    for image in images:
        image_url = image['urls']['regular']
        image_id = image['id']
        save_path = os.path.join(SAVE_DIR, f"{image_id}.jpg")
        download_image(image_url, save_path)
        print(f"Downloaded image {image_id} to {save_path}")
else:
    print("No images found.")
