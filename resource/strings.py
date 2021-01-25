class Strings:

    def __init__(self, config):
        self.app_name = config.app_name
        self.empty_string = ""
        self.ask_select_action = "selected action: "
        self.ACTION_QUIT = "q"

        self.ask_email = "Please insert email to find credential: "
        self.ask_to_choose_credential = "Choose number of credential or (q) for back: "
        self.success_message_password_copied = "PASSWORD SUCCESS COPY TO CLIPBOARD 📋"
