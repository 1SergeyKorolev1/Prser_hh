from src.Api import Api
from src.WorkWithDb import WorkWithDb
from src.app_operation import *
from src.functions import *

work_with_db = WorkWithDb()
api = Api()
link_hh_employers = 'http://api.hh.ru/employers'
link_hh_vacancies = 'http://api.hh.ru/vacancies'
name_db = 'db_hh'
name_table_employers = 'employers'
name_table_vacancies = 'vacancies'
name_for_print_employers = 'работодателей'
name_for_print_vacancies = 'вакансий'
command_employers = 'employer_id int UNIQUE primary key, employer_name text, employer_url text, open_vacancies int'
command_vacancies = 'vacancy_id int UNIQUE primary key, vacancy_name text, salary int, vacancy_url text, employer_id int, employer_name text, description text, constraint fk_vacancies_eployers foreign key(employer_id) references employers(employer_id)'
command_insert_employers = '(employer_id, employer_name, employer_url, open_vacancies) values (%s, %s, %s, %s)'
command_insert_vacancies = '(vacancy_id, vacancy_name, salary, vacancy_url, employer_id, employer_name, description) values (%s, %s, %s, %s, %s, %s, %s)'
# project_path = pathlib.Path(__file__).parent.parent
# path = pathlib.Path(project_path, '', '')
