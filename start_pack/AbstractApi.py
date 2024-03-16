from abc import ABC, abstractmethod

class AbstractApi(ABC):
    @abstractmethod
    def get_employers_api(self, link):
        pass

    @abstractmethod
    def get_vacancies_from_company(self, id_, link):
        pass