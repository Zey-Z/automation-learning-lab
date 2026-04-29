# API Basics Drill — Week 2

**Topic:** HTTP methods, status codes, `requests`, `.json()`, headers, params
**Format:** 10 questions — 5 basic (Q1–Q5) + 5 variants (Q6–Q10)
**Rule:** Write your answer directly under each question.

---

## Q1 — HTTP method
You want to fetch a list of users from `/users`. Which HTTP method should you use?

Your answer:
```python
GET
```

---

## Q2 — Status code meaning
In one sentence, what does status code `404` mean?

Your answer:
```python
the requested resource was not found 
```

---

## Q3 — Import `requests`
Write the import statement for the `requests` library.

Your answer:
```python
import requests
```

---

## Q4 — First GET request
Write one line that sends a GET request to:
`https://jsonplaceholder.typicode.com/users`

Store the result in a variable called `response`.

Your answer:
```python
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
```

---

## Q5 — Status check + parse JSON
Assume `response` already exists. Write code that:
- checks if `response.status_code == 200`
- if yes, stores parsed JSON in `data`
- if not, sets `data = []`

Your answer:
```python
if response.status_code == 200:
    data = response.json()
else:
    data =[]
```

---

## Q6 — Query parameters
Write a GET request to:
`https://jsonplaceholder.typicode.com/todos`

Pass query params so the request asks for:
- `userId = 1`
- `_limit = 3`

Store the result in `response`.

Your answer:
```python
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos", params= {"userId":1,"_limit" : 3})

```

---

## Q7 — Headers
Write a GET request to:
`https://api.example.com/orders`

Include these headers:
- `Authorization: Bearer TOKEN123`
- `Accept: application/json`

Store the result in `response`.

Your answer:
```python
import requests
response = requests.get("https://api.example.com/orders", headers={"Authorization": "Bearer TOKEN123", "Accept": "application/json"})
```

---

## Q8 — Non-200 handling
Write code that prints:
- `"success"` if `response.status_code == 200`
- otherwise prints `f"request failed: {response.status_code}"`

Your answer:
```python
if response.status_code == 200:
    print("success")
else:
    print(f"request failed: {response.status_code}")
```

---

## Q9 — Request exception handling
Write code that:
1. Sends a GET request to `https://jsonplaceholder.typicode.com/posts`
2. Uses `timeout=10`
3. Catches `requests.RequestException`
4. Prints `"network error"` if the request fails

Your answer:
```python
import requests
try:
    requests.get("https://jsonplaceholder.typicode.com/posts", timeout= 10)
except requests.RequestException:
    print("network error")

```

---

## Q10 — Full mini function
Write a function `fetch_user_names()` that:
1. Sends a GET request to `https://jsonplaceholder.typicode.com/users`
2. Uses `timeout=10`
3. Returns a list of names if the status code is `200`
4. Returns an empty list if the status is not `200`
5. Returns an empty list if a `requests.RequestException` happens

Your answer:
```python
import requests
def fetch_user_names():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users", timeout= 10)
        if response.status_code == 200:
            users = response.json()
            names = []
            for user in users:
                names.append(user["name"])
            return names
        else:
            return []    
    except requests.RequestException:
        return []

```
