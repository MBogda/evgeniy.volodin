import os
import sqlite3
from textwrap import indent, dedent
from datetime import datetime

from database import Database


def make_list(d):
    return '\n'.join('{}. {}'.format(key, value) for key, value in d.items())


def get_observation_details(db):
    print('Enter the observation details.')
    while True:
        time = input(
            'Enter date and time in format "YYYY-MM-DD HH:MM:SS" '
            'or empty string to get current date and time: '
        )
        try:
            if time:
                time = datetime.fromisoformat(time)
            else:
                time = datetime.now()
        except ValueError as e:
            print(e)
        else:
            break
    while True:
        cities = db.select_cities()
        print('List of the cities:')
        print(indent(make_list(cities), '  '))
        try:
            city = int(input('Enter the number of the city: '))
            assert city in cities
        except (ValueError, AssertionError):
            print('Please enter one of the number of the cities.')
        else:
            break
    while True:
        states = db.select_states()
        print('List of the weather states:')
        print(indent(make_list(states), '  '))
        try:
            state = int(input('Enter the number of the weather state: '))
            assert state in states
        except (ValueError, AssertionError):
            print('Please enter one of the number of the weather states.')
        else:
            break
    while True:
        try:
            temperature = float(input(
                'Enter the temperature (°C): '
            ))
        except ValueError as e:
            print(e)
        else:
            break
    while True:
        try:
            precipitation = float(input(
                'Enter the precipitation (mm): '
            ))
        except ValueError as e:
            print(e)
        else:
            break
    while True:
        try:
            pressure = float(input(
                'Enter the pressure (mm Hg): '
            ))
        except ValueError as e:
            print(e)
        else:
            break
    while True:
        directions = db.select_directions()
        print('List of the wind directions:')
        print(indent(make_list(directions), '  '))
        try:
            direction = int(input('Enter the number of the wind direction: '))
            assert direction in directions
        except (ValueError, AssertionError):
            print('Please enter one of the number of the wind directions.')
        else:
            break
    while True:
        try:
            wind_value = float(input(
                'Enter the wind speed (m/s): '
            ))
        except ValueError as e:
            print(e)
        else:
            break
    while True:
        ans = input('Add current observation? (y/n): ')
        if ans[0] == 'y':
            return {'time': time, 'city': city, 'state': state,
                    'temperature': temperature, 'precipitation': precipitation,
                    'pressure': pressure, 'wind_direction': direction,
                    'wind_value': wind_value}
        elif ans[0] == 'n':
            return {}


def db_dialog(db, filename):
    options_message = dedent('''\
        Opened database: {}.
        Please choose one of the following options:
        1. Show observations.
        2. Create observation.
        3. Delete observation.
        4. Show cities.
        5. Create city.
        6. Delete city.
        7. Show weather states.
        8. Show wind directions.
        0. Close database.
    '''.format(filename))
    incorrect_option_message = 'Please enter a digit from 0 to 8.'
    incorrect_id_message = 'Please enter the number.'

    while True:
        try:
            option = int(input(options_message))
            assert 0 <= option <= 8
        except (ValueError, AssertionError):
            print(incorrect_option_message)
        else:
            if option == 0:
                break
            elif option == 1:
                states = db.select_states()
                directions = db.select_directions()
                cities = db.select_cities()
                for id_, values in db.select_observations().items():
                    print(dedent('''\
                    Observation {}.
                      Date and time: {}
                      City: {}
                      Weather state: {}
                      Temperature: {} °C
                      Precipitation: {} mm
                      Pressure: {} mm Hg
                      Wind direction: {}
                      Wind speed: {} m/s'''.format(
                        id_, values[0], cities[values[1]], states[values[2]],
                        *values[3:6], directions[values[6]], values[7]
                    )))
            elif option == 2:
                values = get_observation_details(db)
                if values:
                    try:
                        observation_id = db.insert_observation(**values)
                    except sqlite3.IntegrityError as e:
                        print(e)
                    else:
                        print(
                            'New observation is added with '
                            'number {}.'.format(observation_id)
                        )
                else:
                    print('Observation is not added.')
            elif option == 3:
                try:
                    observation_id = int(input(
                        'Enter the number of the deleting observation '
                        'or 0 to cancel: '
                    ))
                except ValueError:
                    print(incorrect_id_message)
                else:
                    db.delete_observation(observation_id)
            elif option == 4:
                print('List of the cities:')
                print(indent(
                    make_list(db.select_cities()),
                    '  '
                ))
            elif option == 5:
                city_name = input('Enter the name of the new city: ')
                city_id = db.insert_city(city_name)
                print('New city {} added with number {}.'.format(
                    city_name, city_id))
            elif option == 6:
                try:
                    city_id = int(input(
                        'Enter the number of the deleting city '
                        'or 0 to cancel: '
                    ))
                    if city_id:
                        db.delete_city(city_id)
                except ValueError:
                    print(incorrect_id_message)
                except sqlite3.IntegrityError as e:
                    print(e)
            elif option == 7:
                print('List of the weather states:')
                print(indent(
                    make_list(db.select_states()),
                    '  '
                ))
            elif option == 8:
                print('List of the wind directions:')
                print(indent(
                    make_list(db.select_directions()),
                    '  '
                ))


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
                    db_dialog(db, database_filename)
                    db.close()
            elif option == 2:
                try:
                    db = Database(database_filename)
                    db.check_created()
                except sqlite3.OperationalError as e:
                    print(e)
                else:
                    db_dialog(db, database_filename)
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
