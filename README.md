# Twitter API and Ollama Integration

This project integrates the Twitter API with Ollama to post content generated based on user input directly to X (formally knows as Twitter). This README provides instructions on setting up the necessary components.


## Prerequisites

- **Python**: Ensure Python 3.8 or higher is installed.
- **Git**: Make sure Git is installed to clone the repository.
- **Twitter Developer Account**: Access to Twitter Developer Platform is required to create API keys. (https://developer.twitter.com/en/portal/dashboard)
- **Ollama Setup**: Ollama must be installed and configured on your system.

---

## Setting Up the Twitter API

1. **Create a Twitter Developer Account**:
   - Visit [Twitter Developer Platform](https://developer.twitter.com/).
   - Log in with your Twitter credentials.
   - Create a developer account if you don’t already have one.

2. **Create a New App**:
   - Navigate to the "Projects & Apps" section.
   - Click on "Create App" and fill out the required details (e.g., app name and description).

3. **Generate API Keys and Tokens**:
   - Once the app is created, go to the "Keys and Tokens" tab.
   - Generate the following:
     - API Key
     - API Secret Key
     - Access Token
     - Access Token Secret

4. **Set Up API Permissions**:
   - Under the "App Settings" section, select the required permissions (e.g., Read and Write).
   - Ensure these permissions allow posting tweets.

5. **Secure Your API Keys**:
   - Store your API keys and tokens securely. They will be needed to authenticate with the Twitter API.

---

## Setting Up Ollama

1. **Install Ollama**:
   - Follow the official instructions to install Ollama on your system. Visit [Ollama’s official website](https://ollama.com/) for detailed guidance.

2. **Configure Ollama**:
   - Ensure Ollama is accessible via your Python environment or command line.
   - Verify the setup by running a test query (e.g., `ollama --test`).

---
## Project Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Environment Variables**:
   - Create a `.env` file in the project root and add the following:
     ```env
     consumer_key=<your_api_key>
     consumer_secret=<your_api_secret_key>
     OLLAMA_API_URL="http://localhost:11434/api/generate" # if applicable
     ```

4. **Run the Application**:
   ```bash
   python automate.py
   ```

---
