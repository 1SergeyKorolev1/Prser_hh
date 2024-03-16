import json
import requests
from start_pack.AbstractApi import AbstractApi


class Api(AbstractApi):
    def get_employers_api(self, link):
        params = {
            "per_page": 10,
            "sort_by": "by_vacancies_open"
        }
        try:
            response = requests.get(link, params)
            res = json.loads(response.text)['items']
            res_list = []
            for i in res:
                res_list.append([i['id'], i['name'], i['alternate_url'], i['open_vacancies']])
            return res_list
        except (Exception, requests.exceptions.ConnectionError) as error:
            print(error)
            return 0
