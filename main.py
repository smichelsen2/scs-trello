import requests
import json

from settings import API_ROOT, API_KEY, API_TOKEN, HEADERS, PARAMS

# set up base
boards_url = f"{API_ROOT}/1/members/me/boards"

boards = json.loads(requests.request(
   "GET",
   boards_url,
   headers=HEADERS,
   params=PARAMS
).text)

for board in boards:

    cards_url = f"{API_ROOT}/1/boards/{board['id']}/cards"
    cards = json.loads(
        requests.request(
            "GET",
            cards_url,
            headers=HEADERS,
            params=PARAMS
            ).text)

    for card in cards:

        attach_url = f"{API_ROOT}/1/cards/{card['id']}/attachments"
        attachments = json.loads(
            requests.request(
                "GET",
                attach_url,
                headers=HEADERS,
                params=PARAMS
                ).text)

        for attachment in attachments:

            delete_url = f"{API_ROOT}/1/cards/{card['id']}/attachments/{attachment['id']}"
            delete_response = requests.request(
                "DELETE",
                delete_url,
                headers=HEADERS,
                params=PARAMS
                ).text
                




