from db_operations import DBOperations


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

    if __choose_menu == 1:
        db_ops.select_all(db_ops.sql_select_all_flights, db_ops.sql_flight_table)

    elif __choose_menu == 2:
        db_ops.select_all(db_ops.sql_select_all_destinations, db_ops.sql_destination_table)

    elif __choose_menu == 3:
        db_ops.select_all(db_ops.sql_select_all_pilots, db_ops.sql_pilot_table)

    elif __choose_menu == 4:
        print("1. Add Flight Record")
        print("2. Update Flight Record")
        print("3. Delete Flight Record")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            db_ops.insert_flight_data()
        elif __choose_menu == 2:
            db_ops.update_data(db_ops.sql_flight_table, db_ops.sql_flight_primary_key)
        elif __choose_menu == 3:
            db_ops.delete_data(db_ops.sql_flight_table, db_ops.sql_flight_primary_key)

    elif __choose_menu == 5:
        print("1. Add Destination Record")
        print("2. Update Destination Record")
        print("3. Delete Destination Record")
        __choose_menu = int(input("Enter your choice: "))
        if __choose_menu == 1:
            db_ops.insert_destination_data()
        elif __choose_menu == 2:
            db_ops.update_data(db_ops.sql_destination_table, db_ops.sql_destination_primary_key)
        elif __choose_menu == 3:
            db_ops.delete_data(db_ops.sql_destination_table, db_ops.sql_destination_primary_key)
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
            db_ops.update_data(db_ops.sql_pilot_table, db_ops.sql_pilot_primary_key)
        elif __choose_menu == 3:
            db_ops.delete_data(db_ops.sql_pilot_table, db_ops.sql_pilot_primary_key)
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
            db_ops.create_table()
        elif admin_selection == 2:
            db_ops.clear_database()

    elif __choose_menu == 9:
        exit(0)
    else:
        print("Invalid Choice")
