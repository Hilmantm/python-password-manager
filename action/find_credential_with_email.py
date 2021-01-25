from service.query import Query
from utils.wrapper import Wrapper
import pyperclip


class FindCredentialWithEmail:
    ACTION_COPY_PASSWORD = 1
    ACTION_SHOW_PASSWORD = 2

    ACTION_QUIT = "q"

    def __init__(self, connection):
        self.connection = connection


    def __showActionForCredential(self):
        print("Choose action :")
        print("1. copy password")
        print("2. show password")
        print("Q. exit")

    def execute(self):
        email = input("Please insert email to find credential: ")

        # get all record according to the email you are looking for
        find_email_result = Query.find_all_sites_connected_to_email(connection=self.connection, email=email)

        select_credential = ""
        while select_credential != self.ACTION_QUIT:
            # show all record result
            Wrapper.print_credential_data(find_email_result)

            select_credential = input("Choose number of credential or (q) for back: ").lower()

            if select_credential != self.ACTION_QUIT:
                Wrapper.print_credential_data([find_email_result[int(select_credential) - 1]])

                copy_credential = ""
                while copy_credential != self.ACTION_QUIT:
                    self.__showActionForCredential()
                    copy_credential = input("selected action: ").lower()

                    if copy_credential != self.ACTION_QUIT:
                        self.__run_user_choice(int(copy_credential))

    def __run_user_choice(self, user_choice):
        if user_choice == self.ACTION_COPY_PASSWORD:
            pyperclip.copy('ini password saya')
            print("password success to copy")
        elif user_choice == self.ACTION_SHOW_PASSWORD:
            print("dummy password")