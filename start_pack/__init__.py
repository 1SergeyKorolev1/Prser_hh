import pathlib
from src.app_operation import *
from src.functions import *
from src.Api import Api
from src.WorkWithDb import WorkWithDb

work_with_db = WorkWithDb()
api = Api()
link_hh_employers = 'http://api.hh.ru/employers'
link_hh_vacancies = 'http://api.hh.ru/vacancies'
name_db = 'db_hh'
name_table_employers = 'employers'
command_employers = 'employer_id int UNIQUE primary key, employer_name text, employer_url text, open_vacancies int'
command_insert_employers = '(employer_id, employer_name, employer_url, open_vacancies) values (%s, %s, %s, %s)'
# project_path = pathlib.Path(__file__).parent.parent
# path = pathlib.Path(project_path, '', '')


