from utils.wrapper import Wrapper
from mysql.connector import Error


class Query:

    @staticmethod
    def __get_table_name():
        return "tbl_passwords"

    @staticmethod
    def find_all_sites_connected_to_email(connection, email):
        try:
            table_name = Query.__get_table_name()
            query = f"""SELECT * FROM {table_name} WHERE email LIKE %s"""
            recent_connection, recent_cursor = connection.get_connection(prepared=True)
            recent_cursor.execute(query, (f"%{email}%",))
            result = recent_cursor.fetchall()

            return result
        except Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            connection.close_connection(recent_connection, recent_cursor)