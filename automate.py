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

def fetch_twitter_content(user_preferences, topic):
    """
    Use Ollama to generate content for Twitter posts based on the user preferences and topic.
    """
    headers = {
        "Content-Type": "application/json",
    }

    # Customize this prompt based on how Ollama handles inputs
    prompt = f"""
    You are a content creator for Twitter. Generate engaging and concise Twitter posts (within 280 characters) on the topic: "{topic}".
    Consider the user preferences: {user_preferences}.
    Create 1 unique tweet about this topic. The response which you give should be in the form of a tweet. With each tweet after a Tweet: write the content of the tweet.
    """

    payload = {
        "model": os.getenv('model'),  # Specify the Ollama model in the .env file
        "prompt": prompt,
        "stream": False,  # Set to True for streaming completion
    }

    response = requests.post(OLLAMA_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        print(response.status_code)
        #print(response.json()['response'])
        return response.json()['response']
        #return response.json().get("content", "").split("\n")
    else:
        raise Exception(f"Error with Ollama API: {response.status_code} - {response.text}")

if __name__ == "__main__":
    try:

        user_preferences = "Tech-Savvy, prefers trending technology news and engaging facts."
        topic = input("Enter a topic you are intrested in:")

        print("Generating content for user preferences: ", user_preferences)
        print("Generating content using Ollama....")

        content = fetch_twitter_content(user_preferences, topic)
        print(content)

    except Exception as e:
        print("An error occurred: ", e)


    
