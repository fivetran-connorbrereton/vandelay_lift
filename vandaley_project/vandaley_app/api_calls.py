import json
import requests

from vandaley_app.config import API_KEY, API_SECRET


def get_url(url):
    return requests.get(url, auth=(API_KEY, API_SECRET))


def post_url(url, values):
    return requests.post(url, auth=(API_KEY, API_SECRET), json=values)


def delete_url(url, values):
    return requests.delete(url, auth=(API_KEY, API_SECRET), json=values)


def dump(response):
    print(json.dumps(response.json()))


