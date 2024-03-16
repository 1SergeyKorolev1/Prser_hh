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
        return cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
