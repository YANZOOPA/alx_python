"""2. POST an email #1"""
import requests
import sys

def get_github_user_id(username, token):
    """
    Get the GitHub user id using Basic Authentication with a personal access token.
    """
    auth = (username, token)
    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()  # Raise an exception for bad responses

        data = response.json()
        return data.get("id")

    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors (e.g., wrong credentials)
        print(f"HTTP Error: {e}")
        return None

    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error decoding JSON: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    user_id = get_github_user_id(username, token)

    if user_id is not None:
        print("Your GitHub user id is:", user_id)
    else:
        print("Failed to retrieve GitHub user id.")
