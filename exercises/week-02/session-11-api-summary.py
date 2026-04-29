"""
Session 11 - Applied API Summary Script

Goal: fetch todo items for one user from a public API, handle failures,
filter the response, and write a small summary JSON file.

Endpoint:
https://jsonplaceholder.typicode.com/todos

Output file:
session-11-todo-summary.json
"""

import json
import requests

URL = "https://jsonplaceholder.typicode.com/todos"
OUTPUT_PATH = "session-11-todo-summary.json"
USER_ID = 1


def main():
    output = {}

    try:
        response = requests.get(URL, params={"userId": USER_ID}, timeout=10)
        print(response.status_code)

        if response.status_code != 200:
            print(f"failed to fetch: {response.status_code}")
            return output

        todos = response.json()
        print(len(todos))

        completed = [
            {
                "id": todo["id"],
                "title": todo["title"],
                "completed": todo["completed"],
            }
            for todo in todos
            if todo["completed"]
        ]

        output = {
            "user_id": USER_ID,
            "total_received": len(todos),
            "completed_count": len(completed),
            "completed_titles": [todo["title"] for todo in completed],
        }

        with open(OUTPUT_PATH, "w") as f:
            json.dump(output, f, indent=2)

        return output
    except requests.RequestException as e:
        print(f"request failed: {e}")
        return output
    finally:
        print("Session 11 API summary finished.")


if __name__ == "__main__":
    main()
