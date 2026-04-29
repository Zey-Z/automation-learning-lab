const fs = require("fs")
const { STATUS_CODES } = require("http")
const { title } = require("process")

const URL = "https://jsonplaceholder.typicode.com/todos"
const OUTPUT_PATH = "exercises/week-02/session-13-fetch-output.json"
const USER_ID = 1

async function fetchCompletedTitles() {
    /*
    Goal:
    1. Build a URL that includes userId=USER_ID as a query param
    2. Send a GET request with an Accept: application/json header
    3. If the status is not OK, return []
    4. Parse the JSON body
    5. Return only the titles of completed todos
    */

    // Your code here
    const url = `https://jsonplaceholder.typicode.com/todos?userId=${USER_ID}`
    const response = await fetch(url, {
        headers:{"Accept": "application/json"}
    })

    if (response.status !== 200){
        return []
    }
    const todos = await response.json()

    return todos.filter(todo => todo.completed === true).map(todo => todo.title) 

}

async function main() {
    const completedTitles = await fetchCompletedTitles()

    const output = {
        userId: USER_ID,
        completedCount: completedTitles.length,
        completedTitles: completedTitles,
    }

    fs.writeFileSync(OUTPUT_PATH, JSON.stringify(output, null, 2))
    console.log(output)
}

main().catch((error) => {
    console.error("session 13 fetch drill failed:", error.message)
})
