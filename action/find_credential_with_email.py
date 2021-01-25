from service.query import Query
from utils.wrapper import Wrapper
import pyperclip


class FindCredentialWithEmail:
    ACTION_COPY_PASSWORD = 1
    ACTION_SHOW_PASSWORD = 2

    def __init__(self, connection, strings):
        self.connection = connection
        self.strings = strings

    def __showActionForCredential(self):
        print(self.strings.choose_action)
        print(f"{self.ACTION_COPY_PASSWORD}. copy password")
        print(f"{self.ACTION_SHOW_PASSWORD}. show password")
        print(f"{self.strings.ACTION_QUIT.upper()}. exit")

    def execute(self):
        email = input(self.strings.ask_email)

        # get all record according to the email you are looking for
        find_email_result = Query.find_all_sites_connected_to_email(connection=self.connection, email=email)

        select_credential = self.strings.empty_string
        while select_credential != self.strings.ACTION_QUIT:
            # show all record result
            Wrapper.print_credential_data(find_email_result)

            select_credential = input(self.strings.ask_to_choose_credential).lower()

            if select_credential != self.strings.ACTION_QUIT:
                copy_credential = self.strings.empty_string

                while copy_credential != self.strings.ACTION_QUIT:
                    Wrapper.print_credential_data([find_email_result[int(select_credential) - 1]])
                    self.__showActionForCredential()
                    copy_credential = input(self.strings.ask_select_action).lower()

                    if copy_credential != self.strings.ACTION_QUIT:
                        self.__run_user_choice(int(copy_credential))

    def __run_user_choice(self, user_choice):
        if user_choice == self.ACTION_COPY_PASSWORD:
            pyperclip.copy('ini password saya')
            print(self.strings.success_message_password_copied)
        elif user_choice == self.ACTION_SHOW_PASSWORD:
            print("DUMMY PASSWORD")
