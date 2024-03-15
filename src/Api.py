import json
import requests
from start_pack.AbstractApi import AbstractApi


class Api(AbstractApi):
    def get_employers_api(self, link):
        params = {
            "per_page": 10,
            "sort_by": "by_vacancies_open"
        }

        response = requests.get(link, params)
        return json.loads(response.text)['items']
