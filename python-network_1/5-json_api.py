"""2. POST an email #1"""
import requests
import sys

if __name__ == "__main__":
    """
    Check if the correct number of arguments is provided
    """
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    """
    Make a POST request to the search_user endpoint
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": q}
    response = requests.post(url, data=payload)

    try:
        """
        Try to parse the response JSON
        """
        data = response.json()

        if data:
            """
            Display id and name if JSON is properly formatted and not empty
            """
            print(f"[{data['id']}] {data['name']}")
        else:
            """
            Display No result if JSON is empty
            """
            print("No result")

    except ValueError:
        """
        Display Not a valid JSON if the JSON is invalid
        """
        print("Not a valid JSON")
