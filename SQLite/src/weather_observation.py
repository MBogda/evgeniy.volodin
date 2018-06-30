import os
import sqlite3
from textwrap import dedent

from database import Database


def db_dialog(db):
    pass


def main():
    welcome_message = 'Welcome to weather observation.'
    cwd_message = \
        'Please run the program under the .../SQLite working directory.'
    options_message = dedent('''\
        Please choose one of the following options:
        1. Create database.
        2. Load database.
        3. Delete database.
        0. Exit.
    ''')
    incorrect_option_message = 'Please enter one of the digits: 1, 2, 3 or 0.'
    default_db_name = 'weather.sql'
    enter_filename_message = \
        'Enter the database filename ({}): '.format(default_db_name)
    file_already_exists_message = 'File {} already exists.'
    file_not_exists_message = 'File {} does not exist.'
    file_is_directory_message = 'File {} is a directory.'
    file_removed_message = 'File {} successfully removed.'
    exit_message = 'Good bye!'

    print(welcome_message)
    if os.path.basename(os.getcwd()) != 'SQLite':
        print(cwd_message)
        return

    while True:
        try:
            option = int(input(options_message))
            assert 0 <= option <= 3
        except (ValueError, AssertionError):
            print(incorrect_option_message)
        else:
            if option == 0:     # if not option:
                break

            database_filename = input(enter_filename_message)
            if not database_filename:
                database_filename = default_db_name

            if option == 1:
                if os.path.exists(database_filename):
                    print(file_already_exists_message.format(
                        database_filename
                    ))
                    continue
                try:
                    db = Database(database_filename)
                except sqlite3.OperationalError as e:
                    print(e)
                else:
                    db.create()
                    db_dialog(db)
                    db.close()
            elif option == 2:
                try:
                    db = Database(database_filename)
                    db.check_created()
                except sqlite3.OperationalError as e:
                    print(e)
                else:
                    db_dialog(db)
                    db.close()
            elif option == 3:
                try:
                    os.remove(database_filename)
                except FileNotFoundError:
                    print(file_not_exists_message.format(
                            database_filename
                    ))
                except IsADirectoryError:
                    print(file_is_directory_message.format(
                        database_filename
                    ))
                else:
                    print(file_removed_message.format(database_filename))
    print(exit_message)


if __name__ == '__main__':
    main()
