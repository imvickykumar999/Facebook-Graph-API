import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the access token from the environment variable
FB_ACCESS_TOKEN = os.getenv('FB_ACCESS_TOKEN')
VIDEO_ID = "757963361686491" # https://www.facebook.com/watch?v=757963361686491

def get_video_details(video_id):
    url = f'https://graph.facebook.com/v12.0/{video_id}'
    params = {
        'access_token': FB_ACCESS_TOKEN,
        'fields': 'id,title,description,source'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def main():
    try:
        video_details = get_video_details(VIDEO_ID)
        print("Video Details:")
        print(f"ID: {video_details['id']}")
        print(f"Title: {video_details.get('title')}")
        print(f"Description: {video_details.get('description')}")
        print(f"URL: {video_details.get('source')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
