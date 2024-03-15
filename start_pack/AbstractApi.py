from abc import ABC, abstractmethod

class AbstractApi(ABC):
    @abstractmethod
    def get_employers_api(self, link):
        pass