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

    def get_vacancies_from_company_api(self, id_, link):
        params = {
            "per_page": 100,
            "employer_id": id_,
            'area': 113
        }
        response = requests.get(link, params)
        res = json.loads(response.text)['items']
        res_list = []
        try:
            for i in res:
                salary = self.get_salary(i)
                description = self.description(i)
                res_list.append(
                    [i['id'], i['name'], salary, i['alternate_url'], i['employer']['id'], i['employer']['name'],
                     description])
            return res_list
        except (Exception, requests.exceptions.ConnectionError) as error:
            print(error)
            return 0

    def get_salary(self, item):
        if item['salary'] != None:
            if item['salary']['from']:
                salary = item['salary']['from']
                return salary
            else:
                salary = item['salary']['to']
                return salary
        else:
            return 0

    def description(self, item):
        """"""
        if item['snippet']['requirement']:
            res = item['snippet']['requirement']
        else:
            res = ''
        if item['snippet']['responsibility']:
            res_ = item['snippet']['responsibility']
        else:
            res_ = ''
        return res + ' ' + res_
