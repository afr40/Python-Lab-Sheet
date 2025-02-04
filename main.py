from database_utils.db_operations import DBOperations
from database_utils.sql_queries import SQLQueries


# The main function will parse arguments.
# These argument will be defined by the users on the console.
# The user will select a choice from the menu to interact with the database.


while True:
    print("\n Menu:")
    print("**********")
    print(" 1. Show All Flight Records")
    print(" 2. Show All Destination Records")
    print(" 3. Show All Pilots Registered")
    print(" 4. Manage Flights")
    print(" 5. Manage Destinations")
    print(" 6. Manage Pilots")
    print(" 7. Search Functions")
    print(" 8. Admin Section")
    print(" 9. Exit\n")

    __choose_menu = int(input("Enter your choice: "))
    db_ops = DBOperations()
    sql = SQLQueries()

    if __choose_menu == 1:
        db_ops.select_all(sql.select_all_flight_routes, sql.flight_route_table)

    elif __choose_menu == 2:
        db_ops.select_all(sql.select_all_airports, sql.airport_table)

    elif __choose_menu == 3:
        db_ops.select_all(sql.select_all_pilots, sql.pilot_table)

    elif __choose_menu == 4:
        print("1. Add Flight Record")
        print("2. Update Flight Record")
        print("3. Delete Flight Record")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            db_ops.insert_flight_data()
        elif __choose_menu == 2:
            db_ops.update_data(sql.flight_route_table, sql.flight_route_pk)
        elif __choose_menu == 3:
            db_ops.delete_data(sql.flight_route_table, sql.flight_route_pk)

    elif __choose_menu == 5:
        print("1. Add Destination Record")
        print("2. Update Destination Record")
        print("3. Delete Destination Record")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            db_ops.insert_airport_data()
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
            db_ops.insert_pilot_data()
        elif __choose_menu == 2:
            db_ops.update_data(sql.pilot_table, sql.pilot_pk)
        elif __choose_menu == 3:
            db_ops.delete_data(sql.pilot_table, sql.pilot_pk)
        else:
            print("Invalid Choice")

    elif __choose_menu == 7:
        print("1. View Pilots Schedule")
        print("2. View Destinations")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            db_ops.view_pilot_schedule()
        elif __choose_menu == 2:
            db_ops.view_destination()

    elif __choose_menu == 8:
        print("1. Reset Database (Clear Current Database and add Sample Records)")
        print("2. Clear Database Records")
        admin_selection = int(input("Enter your choice: "))
        if admin_selection == 1:
            admin_ops = str(input("Confirm to reset Database (y/n): "))
            if admin_ops == 'y':
               db_ops.create_table()
            elif admin_ops == 'n':
                print("Going Back to Main Menu")
            else:
                print("Invalid Choice")
        elif admin_selection == 2:
            admin_ops = str(input("Confirm to Clear Database (y/n): "))
            if admin_ops == 'y':
                db_ops.clear_database()
            elif admin_ops == 'n':
                print("Going Back to Main Menu")
            else:
                print("Invalid Choice")

    elif __choose_menu == 9:
        exit(0)
    else:
        print("Invalid Choice")
