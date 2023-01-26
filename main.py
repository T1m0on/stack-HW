import requests
from pprint import pprint


def get_python_posts():
    url = 'https://api.stackexchange.com/2.3/questions?fromdate=1674518400&order=desc&sort=activity&site=stackoverflow'
    response = requests.get(url).json()

    for i in response['items']:
        if 'python' in i['tags']:
            pprint(i['link'])


get_python_posts()

