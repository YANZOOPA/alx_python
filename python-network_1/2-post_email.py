"""2. POST an email #1"""
import requests
import sys

if __name__ == "__main__":
    """Check if the correct number of arguments is provided """
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    """Get URL and email from command-line arguments """
    url = sys.argv[1]
    email = sys.argv[2]

    """Make a POST request with the email as a parameter """
    payload = {'email': email}
    response = requests.post(url, data=payload)

    """Display the body of the response """
    print(response.text)
