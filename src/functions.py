import psycopg2


def create_database(name_db):
    try:
        conn = psycopg2.connect(database="postgres",
                                user="postgres",
                                password="1234",
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


def connect_database(name_db):
    try:
        conn = psycopg2.connect(database=name_db,
                                user="postgres",
                                password="1234",
                                host="localhost")

        cursor = conn.cursor()
        conn.autocommit = True
        return cursor, conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def create_table(name_db, name_table, command):
    cur, conn = connect_database(name_db)
    try:
        cur.execute(f"CREATE TABLE {name_table} ({command})")
        print(f"Таблица {name_table} успешно создана")
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        cur.close()
        conn.close()
        print(error)


def write_employers_in_db(employers, name_db):
    cur, conn = connect_database(name_db)
    for i in employers:
        cur.execute(
            "insert into employers (employer_id, employer_name, employer_url, open_vacancies) values (%s, %s, %s, %s)",
            i)

