import requests

def summary_generator():

    url = "https://api.covid19api.com/summary"

    # Get response in terms of JSON of COVID-19 summary and saves Global
    response = requests.get(
        url,
        headers={
            "Accept": "application/json"}
    ).json()
    response = dict(response['Global'])

    return response