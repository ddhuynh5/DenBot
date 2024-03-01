import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("YT_KEY")

youtube = build('youtube', 'v3', developerKey=api_key)

channel_name = input("Enter the channel name: ")

# Step 1: Search for channels by name
channel_request = youtube.search().list(
    q=channel_name,
    part='snippet',
    type='channel',
    maxResults=1
)
channel_response = channel_request.execute()

# Step 2: Extract channel ID from search results
if channel_response['items']:
    channel_id = channel_response['items'][0]['id']['channelId']
    print(f"Channel ID: {channel_id}")
else:
    print("No channel found with the provided name.")
    exit()

# Step 3: Search for videos uploaded by the channel
request = youtube.search().list(
    part="snippet",
    order="date",  # Sort by date in descending order
    channelId=channel_id,
    type="video",
    maxResults=10
)

response = request.execute()

# Process the search results
for item in response['items']:
    video_title = item['snippet']['title']
    video_id = item['id']['videoId']
    video_link = f"https://www.youtube.com/watch?v={video_id}"
    print('Video Title:', video_title)
    print('Video Link:', video_link)
    print('--------------------')

