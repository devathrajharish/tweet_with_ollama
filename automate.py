import requests
import json
import os

from requests_oauthlib import OAuth1Session

# Replace with your Twitter API keys

consumer_key = os.getenv('TWITTER_API_KEY')
consumer_secret = os.getenv('TWITTER_API_SECRET')

# Replace with your Ollama API endpoint and API key if required
OLLAMA_API_URL = os.getenv('OLLAMA_API_URL')
# Update if hosted differently
    
if __name__ == "__main__":
    try:

        user_preferences = "Tech-Savvy, prefers trending technology news and engaging facts."
        topic = input("Enter a topic you are intrested in:")

        print("Generating content for user preferences: ", user_preferences)
        print("Generating content using Ollama....")

    except Exception as e:
        print("An error occurred: ", e)


    
