"""
controller.py
by Matthew McClelland
Various functions for dealing with API calls and 
data functionality
"""

# imports
import requests as re

def get_api_data(endpoint: str, query=""):
    domain = "https://swapi.py4e.com/api/"
    url = domain + endpoint + "/" + query + "/"
    response = re.get(url)

    if response.ok:
        results = response.text
    else:
        results = "Error!"
    return results

if __name__ == "__main__":
    call = get_api_data("planets", "1")
    print(call)