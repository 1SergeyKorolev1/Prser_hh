import pathlib
from src.app_operation import *
from src.functions import *
from src.Api import Api


api = Api()
link_hh_employers = 'http://api.hh.ru/employers'
link_hh_vacancies = 'http://api.hh.ru/vacancies'
name_db = 'db_hh'
name_table_employers = 'employers'
command_employers = 'employer_id int UNIQUE primary key, employer_name text, employer_url text, open_vacancies int'
# project_path = pathlib.Path(__file__).parent.parent
# path = pathlib.Path(project_path, '', '')


