import requests

# Set the search term and the number of images to download
search_term = 'apartheid south africa 1950s'
num_images = 1000

# Set the API key and the endpoint URL
# Read api key based on unsplash_key.txt 
# the format for the api key is changed to {[userName] [api_key]}
key_file = open("unsplash_key.txt", "r")
api_key = key_file.read()
endpoint_url = 'https://api.unsplash.com/search/photos'

# Make the request
response = requests.get(endpoint_url, params={'query': search_term, 'per_page': num_images}, headers={'Authorization': 'Client-ID '+api_key})

# Check the status code of the response
if response.status_code == 200:
    # Load the response data as a JSON object
    data = response.json()
    # Iterate through the list of images
    for image in data['results']:
        # Get the image URL and download the image
        image_url = image['urls']['full']
        response = requests.get(image_url)
        # Save the image to a file
        open(f'images/{image["id"]}.jpg', 'wb').write(response.content)
else:
    print('Error:', response.status_code)
