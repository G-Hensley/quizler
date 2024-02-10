import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

q_response = requests.get(url="https://opentdb.com/api.php", params=parameters)

question_data = q_response.json()["results"]
