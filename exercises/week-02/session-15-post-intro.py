"""
Session 15 - Lightweight POST Exposure

Goal: compare GET vs POST in one small Python script.

Target endpoint:
https://jsonplaceholder.typicode.com/posts

Output file:
exercises/week-02/session-15-post-output.json
"""

import json
import requests

URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_PATH = "exercises/week-02/session-15-post-output.json"

PAYLOAD = {
    "title": "week-2-closeout",
    "body": "practicing python requests.post with a JSON body",
    "userId": 1,
}


def main():
    """
    Goal:
    1. send a POST request to URL
    2. send PAYLOAD as JSON body
    3. use timeout=10
    4. if status code is not 201, print a failure message and return {}
    5. parse response JSON
    6. write a small output JSON file with:
       - request_title
       - response_id
       - response_title
       - status_code
    7. print the output dict
    """

    output = {}

    response = requests.post(URL, json= PAYLOAD, timeout= 10)
    if response.status_code != 201:
        print(f"request failure, status code: {response.status_code}")
        return output
    data = response.json()
    output= {"request_title": PAYLOAD["title"], 
            "response_id":data["id"],
            "response_title":data["title"] , 
            "status_code":response.status_code,
            }
    print(output)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent= 2)



if __name__ == "__main__":
    main()
