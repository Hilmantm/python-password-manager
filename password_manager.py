from resource.strings import Strings
from utils.config import Config
from utils.connection import Connection
from action.find_credential_with_email import FindCredentialWithEmail


class PasswordManager:
    ACTION_CREATE_PASSWORD = 1
    ACTION_FIND_WITH_EMAIL = 2
    ACTION_FIND_PASSWORD_FOR_SITE = 3

    ACTION_QUIT = "q"

    def __init__(self):
        self.config = Config()
        self.connection = Connection(self.config)
        self.strings = Strings(self.config)

    def __showMenus(self):
        print("Choose action :")
        print("1. create new password")
        print("2. find all sites and apps connected to an email")
        print("3. find a password for a site or app")
        print("Q. exit")

    def execute(self):
        print(f"Welcome in {self.strings.app_name}")
        # looping the choose action until user choose exit option
        action_choose = ""
        while action_choose != self.ACTION_QUIT:
            self.__showMenus()
            action_choose = input("selected action: ").lower()
            if action_choose != self.ACTION_QUIT:
                self.execute_action(action_choose)

    def execute_action(self, action_choose):
        action_choose_value = int(action_choose)
        if action_choose_value == self.ACTION_FIND_WITH_EMAIL:
            find_credential_with_email = FindCredentialWithEmail(self.connection)
            find_credential_with_email.execute()