import mysql.connector


class Connection:

    def __init__(self, config):
        self.config = config

    def get_connection(self, prepared):
        """
        Get new database connection and cursor from config
        database

        :return: connection
        :return: cursor
        """
        connection = mysql.connector.connect(
            host=self.config.database.host,
            user=self.config.database.user,
            password=self.config.database.password,
            database=self.config.database.database
        )
        cursor = connection.cursor(prepared=prepared)

        return connection, cursor

    def close_connection(self, connection, cursor):
        if connection.is_connected():
            connection.close()
            cursor.close()