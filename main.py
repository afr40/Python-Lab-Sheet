from database_utils.db_operations import DBOperations
from database_utils.sql_queries import SQLQueries
from table_utils.airport import Airport
from table_utils.flight_route import FlightRoute
from table_utils.flight_schedule import FlightSchedule
from table_utils.pilot import Pilot

"""
The Main Menu of the database:

1. The user will select a choice from the menu to interact with the database.
2. DBOperations will contain all the functions to create, delete, update, and insert data.
3. SQL Queries are declared on its own class. 
"""

while True:
    # Print menu
    print("\n Menu:")
    print("**********")
    print("1. Show Flight Information")
    print("2. Show Airport (Destinations)")
    print("3. Show Pilot Information")
    print("4. Manage Flights")
    print("5. Manage Airport (Destinations)")
    print("6. Manage Pilots")
    print("7. Search Functions")
    print("8. Admin Section")
    print("9. Show Help ")
    print("10. Exit\n")

    __choose_menu = int(input("Enter your choice: "))
    db_ops = DBOperations()
    sql = SQLQueries()

    # Menu Selection
    if __choose_menu == 1:
        print("1. Flights (Routes and Schedules)")
        print("2. Flight Routes")
        print("3. Flight Schedules")
        print("4. <- GO BACK")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            db_ops.select_all(sql.select_all_flights, None, sql.select_all_flights_columns)
        elif __choose_menu == 2:
            db_ops.select_all(sql.select_all_flight_routes, sql.flight_route_table)
        elif __choose_menu == 3:
            db_ops.select_all(sql.select_all_flight_schedule, sql.flight_schedule_table)
        elif __choose_menu == 4:
            print("")
        else:
            print("Invalid Choice")

    elif __choose_menu == 2:
        db_ops.select_all(sql.select_all_airports, sql.airport_table)

    elif __choose_menu == 3:
        print("1. Pilot's Information")
        print("2. Pilot's Schedules")
        print("3. Show Available Pilots")
        print("4. <- GO BACK")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            db_ops.select_all(sql.select_all_pilots, sql.pilot_table)
        elif __choose_menu == 2:
            db_ops.select_all(sql.select_all_pilot_schedules, None)
        elif __choose_menu == 3:
            db_ops.select_all(sql.search_pilot_available, sql.pilot_table)
        elif __choose_menu == 4:
            print("")
        else:
            print("Invalid Choice")

    elif __choose_menu == 4:
        print("1. Add Flight Route")
        print("2. Add Flight Schedule")
        print("3. Update Flight Route")
        print("4. Update Flight Schedule")
        print("5. Delete Flight Route")
        print("6. Delete Flight Schedule")
        print("7. <- GO BACK")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            flight_route = FlightRoute()
            db_ops.insert_data(flight_route, sql.flight_route_table, sql.insert_flight_route)
        elif __choose_menu == 2:
            flight_schedule = FlightSchedule()
            db_ops.insert_data(flight_schedule, sql.flight_schedule_table, sql.insert_flight_schedule)
        elif __choose_menu == 3:
            db_ops.update_data(sql.flight_route_table, sql.flight_route_pk)
        elif __choose_menu == 4:
            db_ops.update_data(sql.flight_schedule_table, sql.flight_schedule_pk)
        elif __choose_menu == 5:
            db_ops.delete_data(sql.flight_route_table, sql.flight_route_pk)
        elif __choose_menu == 6:
            db_ops.delete_data(sql.flight_schedule_table, sql.flight_schedule_pk)
        elif __choose_menu == 7:
            print("")
        else:
            print("Invalid Choice")

    elif __choose_menu == 5:
        print("1. Add Airport Record")
        print("2. Update Airport Record")
        print("3. Delete Airport Record")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            airport = Airport()
            db_ops.insert_data(airport, sql.airport_table, sql.insert_airport)
        elif __choose_menu == 2:
            db_ops.update_data(sql.airport_table, sql.airport_pk)
        elif __choose_menu == 3:
            db_ops.delete_data(sql.airport_table, sql.airport_pk)
        else:
            print("Invalid Choice")

    elif __choose_menu == 6:
        print("1. Add Pilots Record")
        print("2. Update Pilots Record")
        print("3. Delete Pilots Record")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            pilot = Pilot()
            db_ops.insert_data(pilot, sql.pilot_table, sql.insert_pilot)
        elif __choose_menu == 2:
            db_ops.update_data(sql.pilot_table, sql.pilot_pk)
        elif __choose_menu == 3:
            db_ops.delete_data(sql.pilot_table, sql.pilot_pk)
        else:
            print("Invalid Choice")

    elif __choose_menu == 7:
        print("1. Search Pilot Schedule")
        print("2. Search for Flight Routes Destination")
        print("3. Search for a Flight")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            db_ops.view_pilot_schedule()
        elif __choose_menu == 2:
            db_ops.view_destination()
        elif __choose_menu == 3:
            db_ops.search_data()
        else:
            print("Invalid Choice")

    elif __choose_menu == 8:
        print("1. Reset Database (Clear Current Database and add Sample Records)")
        print("2. Clear Database Records")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            __choose_menu = str(input("Confirm to reset Database (y/n): "))
            if __choose_menu == 'y':
               db_ops.create_table()
            elif __choose_menu == 'n':
                print("Going Back to Main Menu")
            else:
                print("Invalid Choice")
        elif __choose_menu == 2:
            __choose_menu = str(input("Confirm to Clear Database (y/n): "))
            if __choose_menu == 'y':
                db_ops.clear_database()
            elif __choose_menu == 'n':
                print("Going Back to Main Menu")
            else:
                print("Invalid Choice")

    elif __choose_menu == 9:
        print("Instructions on How to Use the Application")
        print("-------------------------------------------")
        print("1. SHOW DATABASE RECORDS (OPTIONS 1 TO 3)")
        print("You can view flight information, airport destinations, and pilot details.\n"
          "For pilots, you can also check their schedules and availability.")

        print("\n2. MANAGING DATA (OPTIONS 4 TO 6)")
        print("To add, update, or remove data, you can manage flights, airport records, and pilot details.\n"
          "Select which part of the database to modify and then the action.\n")

        print("\n3. SEARCHING FOR INFORMATION (OPTIONS 7)")
        print("The application allows you to search for specific pilots, flights, or destinations.\n"
          "Use the ID to use the search functionality to quickly find what you're looking for.")

        print("\n4. ADMINISTRATIVE TASKS (OPTIONS 8)")
        print("The application allows to reset the database and add sample data, or clear all records,\n")
        print("-------------------------------------------")
        __choose_menu = int(input("<- Go Back to Main Menu (Insert 0): "))
        print("-------------------------------------------")
        if __choose_menu == 1:
            print("")
        else:
            print("Invalid Choice")

    elif __choose_menu == 10:
        exit(0)
    else:
        print("Invalid Choice")
