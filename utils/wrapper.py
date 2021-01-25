from prettytable import PrettyTable


class Wrapper:

    @staticmethod
    def print_credential_data(record):
        result_table = PrettyTable()
        result_table.field_names = ["No.", "username", "email", "site url", "site name"]

        for index, data in enumerate(record):
            result_table.add_row([index + 1, data[1], data[2], data[4], data[5]])

        print(result_table)
