"""
Session 10 - Error Handling + First API Request

Goal: send a GET request, check the status code, parse JSON,
transform the response, and write a small output file.

Endpoint:
https://jsonplaceholder.typicode.com/users

Output file:
session-10-users.json
"""

import json
import requests

URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_PATH = "session-10-users.json"


def main():
    summaries = []

    try:
        response = requests.get(URL, timeout=10)
        print(response.status_code)

        if response.status_code != 200:
            print(f"request failed: {response.status_code}")
            return summaries

        users = response.json()
        print(len(users))

        summaries = [
            {
                "name": user["name"],
                "email": user["email"],
                "city": user["address"]["city"],
                "company": user["company"]["name"],
            }
            for user in users
        ]

        with open(OUTPUT_PATH, "w") as f:
            json.dump(summaries, f, indent=2)

        return summaries
    except requests.RequestException as e:
        print(f"request failed: {e}")
        return summaries
    finally:
        print("Session 10 API intro finished.")


if __name__ == "__main__":
    main()
