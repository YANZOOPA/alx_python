"""2. POST an email #1"""
import requests
import sys

if __name__ == "__main__":
    """
    Check if the correct number of arguments is provided
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    """
    Get URL from command-line arguments
    """
    url = sys.argv[1]

    """
    Make a GET request to the URL
    """
    response = requests.get(url)

    """
    Display the body of the response
    """
    print(response.text)

    """
    Check if the status code is greater than or equal to 400
    """
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
