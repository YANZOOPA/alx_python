"""2. POST an email #1"""
import requests
import sys

if __name__ == "__main__":
    """
    Check if the correct number of arguments is provided
    """
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <personal_access_token>")
        sys.exit(1)

    """
    Retrieve username and personal access token from command line arguments
    """
    username = sys.argv[1]
    token = sys.argv[2]

    """
    Set up Basic Authentication with personal access token
    """
    auth = (username, token)

    """
    Make a GET request to the GitHub API to retrieve user information
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=auth)

    try:
        """
        Try to parse the response JSON
        """
        data = response.json()

        """
        Display the user id
        """
        print("Your GitHub user id is:", data["id"])

    except ValueError:
        """
        Display an error message if the JSON is invalid
        """
        print("Error: Unable to retrieve user id. Please check your credentials.")
