from example_system.db_connection_wrapper import db_connection_wrapper


def process_data() -> None:
    pass


def process_data_with_error() -> None:
    raise Exception("Something went wrong")


def run_example() -> None:
    with db_connection_wrapper() as db_connection:
        db_connection.execute("SELECT * FROM USERS;")
        db_connection.execute("SELECT * FROM CUSTOMERS;")
        db_connection.execute("INSERT ...")
        process_data()

    with db_connection_wrapper() as db_connection:
        db_connection.execute("SELECT * FROM USERS;")
        db_connection.execute("SELECT * FROM CUSTOMERS;")
        db_connection.execute("INSERT ...")
        process_data_with_error()


if __name__ == "__main__":
    run_example()
