from resource.strings import Strings
from utils.config import Config
from utils.connection import Connection
from action.find_credential_with_email import FindCredentialWithEmail


class PasswordManager:
    ACTION_CREATE_PASSWORD = 1
    ACTION_FIND_WITH_EMAIL = 2
    ACTION_FIND_PASSWORD_FOR_SITE = 3

    def __init__(self):
        self.config = Config()
        self.connection = Connection(self.config)
        self.strings = Strings(self.config)

    def __showMenus(self):
        print(self.strings.choose_action)
        print(f"{self.ACTION_CREATE_PASSWORD}. create new password")
        print(f"{self.ACTION_FIND_WITH_EMAIL}. find all sites and apps connected to an email")
        print(f"{self.ACTION_FIND_PASSWORD_FOR_SITE}. find a password for a site or app")
        print(f"{self.strings.ACTION_QUIT.upper()}. exit")

    def execute(self):
        print(self.strings.welcome)
        # looping the choose action until user choose exit option
        action_choose = self.strings.empty_string
        while action_choose != self.strings.ACTION_QUIT:
            self.__showMenus()
            action_choose = input(self.strings.ask_select_action).lower()
            if action_choose != self.strings.ACTION_QUIT:
                self.execute_action(action_choose)

    def execute_action(self, action_choose):
        action_choose_value = int(action_choose)
        if action_choose_value == self.ACTION_FIND_WITH_EMAIL:
            find_credential_with_email = FindCredentialWithEmail(self.connection, self.strings)
            find_credential_with_email.execute()