import requests
import json
import os
import random
from requests_oauthlib import OAuth1Session

# Replace with your Twitter API keys

consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
#print(consumer_key)
# Replace with your Ollama API endpoint and API key if required
OLLAMA_API_URL = 'http://localhost:11434/api/generate'
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
    You are a content creator for Twitter.
    Generate engaging and concise Viral Twitter posts (within 280 characters) on the topic: "{topic}".
    Consider the user preferences: {user_preferences}.

    Create 1 unique tweet about this topic. The response which you give should be in the form of a tweet. 
    inlcude relevant 4-5 hashtags based on the topic.
    Do not include " at the starting and end of your in your response.
    """

    payload = {
        "model": "llama3.2:latest",  # Specify the Ollama model in the .env file
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

#Save the Ollama API response to a text file
def save_to_txt_file(filename, content):
    """
    Save the generated content to a text file.
    """
    with open(filename, "w") as file:
        file.write(content)
    print(f"Content saved to {filename}")

 #Parse the file written by the ollama   
def parse_tweet_file(filename):
        
    tweet_dict = {}
    with open(f"{filename}", "r") as file:
        lines = file.readlines()

    current_key = None
    current_value = []
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line.startswith("Tweet"):  # Identify a new tweet key
            if current_key:  # Save the previous tweet's content
                tweet_dict[current_key] = " ".join(current_value).strip()
            current_key = line  # Set the new key
            current_value = []  # Reset the value list
        elif current_key:  # Accumulate the value for the current key
            current_value.append(line)

    # Add the last tweet to the dictionary
    if current_key:
        tweet_dict[current_key] = " ".join(current_value).strip()

    return tweet_dict

#Calling the X API 
def twitter_API_call(payload):

    request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
    
    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError:
        print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
        )

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    # Get authorization
    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    print("Please go here and authorize: %s" % authorization_url)
    verifier = input("Paste the PIN here: ")

    # Get the access token
    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )
    oauth_tokens = oauth.fetch_access_token(access_token_url)

    access_token = oauth_tokens["oauth_token"]
    access_token_secret = oauth_tokens["oauth_token_secret"]

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))
    
if __name__ == "__main__":
    try:

        user_preferences = "Twitter user prefers latest news and engaging facts."
        # topic = input("Enter a topic you are intrested in:")

        # List of trending topics in India
        trending_topics_india = []

        # Assign a random value to the variable 'topic'
        topic = random.choice(trending_topics_india)

    # Print the randomly selected topic
        print(f"The randomly selected topic is: {topic}")

        print("Generating content for user preferences: ", user_preferences)
        print("Generating content using Ollama....")

        twitter_content = fetch_twitter_content(user_preferences, topic)
        #print(twitter_content)
        # Save the generated content to a .txt file
        filename = f"./text_files/{topic.replace(' ', '_')}_twitter_posts.txt"
        #save_to_txt_file(filename, twitter_content)
        tweet_payload = {"text": twitter_content}
            #tweeter_API_call
        print(tweet_payload)
        twitter_API_call(tweet_payload)

        print(f"Twitter content generated successfully! Check the file: {filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


    
