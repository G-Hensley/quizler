import requests

# Parameters for the quiz
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

# Get the questions from the API
q_response = requests.get(url="https://opentdb.com/api.php", params=parameters)

# Get the results from the API
question_data = q_response.json()["results"]
