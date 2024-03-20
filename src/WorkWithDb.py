import psycopg2


class WorkWithDb:
    @staticmethod
    def create_database(name_db, password_db):
        try:
            conn = psycopg2.connect(database="postgres",
                                    user="postgres",
                                    password=password_db,
                                    host="localhost")

            cursor = conn.cursor()
            conn.autocommit = True
            sql_db_create = f"CREATE DATABASE {name_db}"

            cursor.execute(sql_db_create)
            print(f"База данных {name_db} успешно создана")
            cursor.close()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def connect_database(name_db, password_db):
        try:
            conn = psycopg2.connect(database=name_db,
                                    user="postgres",
                                    password=password_db,
                                    host="localhost")

            cursor = conn.cursor()
            conn.autocommit = True
            return cursor, conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def get_companies_and_vacancies_count(work_with_db, name_db, password_db):
        cur, conn = work_with_db.connect_database(name_db, password_db)
        cur.execute(f"select employer_name, open_vacancies from employers")
        data = cur.fetchall()
        print('\nполучаем список всех компаний и количество вакансий у каждой компании..:')
        for i in data:
            print(f'Название - {i[0]} | кол-во открытых вакансий - {i[1]}')
        cur.close()
        conn.close()

    @staticmethod
    def get_all_vacancies(work_with_db, name_db, password_db):
        cur, conn = work_with_db.connect_database(name_db, password_db)
        cur.execute(f"select employer_name, vacancy_name, salary, vacancy_url from vacancies")
        data = cur.fetchall()
        print(
            '\nполучаем список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию..:')
        for i in data:
            print(
                f'Название компании - {i[0]} | название вакансии - {i[1]} | зарплата - {i[2]} | ссылка на вакансию - {i[3]}')
        cur.close()
        conn.close()

    @staticmethod
    def get_avg_salary(work_with_db, name_db, password_db):
        cur, conn = work_with_db.connect_database(name_db, password_db)
        cur.execute(f"select employer_name, avg(salary) from vacancies group by employer_name")
        data = cur.fetchall()
        print('\nполучаем среднюю зарплату по вакансиям..:')
        for i in data:
            print(f'Название компании - {i[0]} | средняя зарплата по вакансиям - {int(i[1])}')
        cur.close()
        conn.close()

    @staticmethod
    def get_vacancies_with_higher_salary(work_with_db, name_db, password_db):
        cur, conn = work_with_db.connect_database(name_db, password_db)
        cur.execute(f"select vacancy_name, salary, vacancy_url from vacancies where salary > (select avg(salary) from vacancies)")
        data = cur.fetchall()
        print('\nполучаем список всех вакансий, у которых зарплата выше средней по всем вакансиям..:')
        for i in data:
            print(f'Название вакансии - {i[0]} | зарплата - {int(i[1])} | ссылка на вакансию - {int(i[1])}')
        cur.close()
        conn.close()

    @staticmethod
    def get_vacancies_with_keyword(work_with_db, name_db, password_db, keyword):
        cur, conn = work_with_db.connect_database(name_db, password_db)
        cur.execute(f"select vacancy_name, salary, vacancy_url from vacancies where vacancy_name like '%{keyword}%'")
        data = cur.fetchall()
        print('\nполучаем список всех вакансий, в названии которых содержатся переданные в метод слова..:')
        for i in data:
            print(f'Название вакансии - {i[0]} | зарплата - {int(i[1])} | ссылка на вакансию - {int(i[1])}')
        cur.close()
        conn.close()

    @staticmethod
    def get_vacancies_with_keyword_in_description(work_with_db, name_db, password_db, keyword):
        cur, conn = work_with_db.connect_database(name_db, password_db)
        cur.execute(f"select vacancy_name, salary, vacancy_url from vacancies where description like '%{keyword}%'")
        data = cur.fetchall()
        print('\nполучаем список всех вакансий, в описании которых содержатся переданные в метод слова..:')
        for i in data:
            print(f'Название вакансии - {i[0]} | зарплата - {int(i[1])} | ссылка на вакансию - {int(i[1])}')
        cur.close()
        conn.close()
