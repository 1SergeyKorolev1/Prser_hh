import pathlib
from start_pack.app_operation import app_operation
from src.Api import Api


api = Api()
link_hh_employers = 'http://api.hh.ru/employers'
link_hh_vacancies = 'http://api.hh.ru/vacancies'
project_path = pathlib.Path(__file__).parent.parent
# path = pathlib.Path(project_path, '', '')


