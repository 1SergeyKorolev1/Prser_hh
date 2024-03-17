from abc import ABC, abstractmethod


class AbstractApi(ABC):
    @abstractmethod
    def get_employers_api(self, link):
        pass

    @abstractmethod
    def get_vacancies_from_company_api(self, id_, link, count_vacancies):
        pass

    @abstractmethod
    def get_salary(self, item):
        pass

    @abstractmethod
    def description(self, item):
        pass
