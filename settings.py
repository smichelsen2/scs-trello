
from auth import API_KEY, API_TOKEN

API_ROOT = 'https://api.trello.com'

HEADERS = {
   "Accept": "application/json"
}

PARAMS = {
   'key': API_KEY,
   'token': API_TOKEN,
   'fields': 'name,url'
}