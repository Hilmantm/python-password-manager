from entity.database import Database
import json


class Config:

    def __init__(self):

        # open config file in json format
        config_file = open('./config.json')
        config = json.load(config_file)

        # set configuration into property
        self.__set_config(config)

        # close the connection to config file
        config_file.close()

    def __set_config(self, config):
        database_config = config["database"]
        self.database = Database(
            host=database_config["host"],
            user=database_config["user"],
            password=database_config["password"],
            database=database_config["database"]
        )
        self.app_name = config["app_name"]