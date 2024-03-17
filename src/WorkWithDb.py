import psycopg2

class WorkWithDb:
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

