import psycopg2


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


def create_table(name_db, name_table, command, work_with_db, password_db):
    cur, conn = work_with_db.connect_database(name_db, password_db)
    try:
        cur.execute(f"CREATE TABLE {name_table} ({command})")
        print(f"Таблица {name_table} успешно создана")
        cur.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        cur.close()
        conn.close()
        print(error)


def write_data_in_db(employers, name_db, work_with_db, name_table, command, name_for_print, password_db):
    cur, conn = work_with_db.connect_database(name_db, password_db)
    for i in employers:
        try:
            cur.execute(
                f"insert into {name_table} {command}",
                i)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    print(f"Таблица {name_table} успешно наполнена данными {name_for_print}")
    cur.close()
    conn.close()

