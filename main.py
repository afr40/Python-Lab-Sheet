import sqlite3
import pandas as pd
from database_setup import drop_tables, create_tables, insert_sample_data
from table_utils.flight_info import FlightInfo
from table_utils.destination import Destination
from table_utils.pilot import Pilot


# Define DBOperation class to manage all data into the database.


class DBOperations:

  sql_insert_flight = "INSERT INTO FlightInfo VALUES (?, ?, ?, ?, ?, ?, ?)"
  sql_insert_destination = "INSERT INTO Destination VALUES (?, ?, ?, ?)"
  sql_insert_pilot = "INSERT INTO Pilot VALUES (?, ?, ?, ?)"
  sql_select_all_flights = "SELECT * FROM FlightInfo"
  sql_select_all_destinations = "SELECT * FROM Destination"
  sql_select_all_pilots = "SELECT * FROM Pilot"
  sql_select_pilot_list = "SELECT PilotID, Name FROM Pilot"
  sql_search = "SELECT * FROM FlightInfo WHERE FlightID = ?"
  sql_delete_data = "DELETE FROM FlightInfo WHERE FlightID = ?"
  sql_view_pilot_schedule = "SELECT Name, Schedule FROM Pilot WHERE PilotID = ?"
  sql_flight_table = 'FlightInfo'
  sql_destination_table = 'Destination'
  sql_pilot_table = 'Pilot'
  sql_flight_primary_key = 'FlightID'
  sql_destination_primary_key = 'DestinationID'
  sql_pilot_primary_key = 'PilotID'

  def __init__(self):
    try:
      self.conn = sqlite3.connect("test.db")
      self.cur = self.conn.cursor()
      create_tables(self.cur)
      self.conn.commit()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()


  def get_connection(self):
    self.conn = sqlite3.connect("test.db")
    self.cur = self.conn.cursor()


  def create_table(self):
    try:
      self.get_connection()
      drop_tables(self.cur)
      create_tables(self.cur)
      insert_sample_data(self.cur)
      self.conn.commit()
      print("Tables FlightInfo, Destination and Pilot Created Successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()


  def clear_database(self):
    try:
      self.get_connection()
      drop_tables(self.cur)
      create_tables(self.cur)
      self.conn.commit()
      print("Database Cleared")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()


  def insert_flight_data(self):
    try:
      self.get_connection()
      flight = FlightInfo()

      flight.set_flight_id(int(input("Enter FlightID (Unique): ")))
      print('')
      self.print_table(self.cur.execute("SELECT DestinationID FROM Destination"), 'Destination', ['Locations Available'])
      print('')
      flight.set_flight_origin(str(input("Enter Flight Origin (Full Location Name): ")))
      flight.set_flight_destination(str(input("Enter Flight Destination (Full Location Name): ")))
      print('')
      self.print_table(self.cur.execute("SELECT PilotID, Name FROM Pilot"), 'Pilot', ['Pilot ID', 'Name'])
      print('')
      flight.set_pilot_id(int(input("Assign Pilot ID: ")))
      flight.set_status(str(input("Enter Flight Status (Optional): ")))
      flight.set_schedule_time(str(input("Flight Schedule Time (HH:MM): ")))
      flight.set_departure_date(str(input("Departure Date (YYYY-MM-DD): ")))

      self.cur.execute(self.sql_insert_flight, tuple(str(flight).split("\n")))
      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()


  def insert_destination_data(self):
    try:
      self.get_connection()
      destination = Destination()

      destination.set_destination_id(int(input("Enter Destination ID: ")))
      destination.set_city(str(input("Enter Destination City: ")))
      destination.set_country(str(input("Enter Destination Country: ")))
      destination.set_airport_id(destination.get_airport_id().split("-")[1])

      self.cur.execute(self.sql_insert_destination, tuple(str(destination).split("\n")))
      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def insert_pilot_data(self):
    try:
      self.get_connection()
      pilot = Pilot()

      pilot.set_pilot_id(int(input("Enter Pilot ID: ")))
      pilot.set_name(str(input("Enter Pilot Name: ")))
      pilot.set_status(str(input("Enter Pilot Status (Optional): ")))
      pilot.set_schedule(str(input("Enter Pilot Schedule Time (HH:MM - HH:MM): ")))

      self.cur.execute(self.sql_insert_pilot, tuple(str(pilot).split("\n")))
      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()


  def select_all(self, sql_select_all, table):
    try:
      self.get_connection()
      self.cur.execute(sql_select_all)
      result = self.cur.fetchall()
      self.print_table(result, table, None)
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def search_data(self):
    try:
      self.get_connection()
      flight_id = int(input("Enter FlightNo: "))
      self.cur.execute(self.sql_search, (str(flight_id),))
      result = self.cur.fetchone()
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("---------------")
            print("Flight ID: " + str(detail))
          elif index == 1:
            print("Flight Origin: " + detail)
          elif index == 2:
            print("Flight Destination: " + detail)
          elif index == 3:
            print("Pilot ID: " + str(detail))
          elif index == 4:
            print("Status: " + detail)
          elif index == 5:
            print("Schedule Time: " + detail)
          else :
            print("Departure Date: " + detail)
            print("---------------")
      else:
        print("No Record")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


  def update_data(self, table, primary_key):
    try:
      self.get_connection()
      self.cur.execute("PRAGMA foreign_keys = ON")
      self.cur.execute(f"SELECT * FROM {table} LIMIT 0")
      columns = [description[0] for description in self.cur.description]

      table_id = input(f"Enter {table} ID: ")
      print("Choose Information to Update")
      print("---------------")
      print("Flight ID: " + str(table_id))
      for index, column in enumerate(columns, start=1):
        print(f"{index}. Update {column}")

      print("")
      update_choice = int(input("Enter Update Index: "))
      update_information = str(input("Enter Update: "))
      sql_update_data = f"UPDATE {table} SET {columns[update_choice - 1]} = ? WHERE {primary_key} = ?"
      print(sql_update_data)
      self.cur.execute(sql_update_data, (update_information, table_id))

      if self.cur.rowcount != 0:
        print(str(self.cur.rowcount) + "Row(s) affected.")
        self.conn.commit()
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


  # Define Delete_data method to delete data from the table.
  # The user will need to input the flight id to delete the corresponding record.
  def delete_data(self):
    try:
      self.get_connection()
      flight_id = str(input("Enter Flight ID Record to Delete: "))

      self.cur.execute(self.sql_delete_data, (flight_id,))
      # result = self.cur.fetchall()

      if self.cur.rowcount != 0:
        print(str(self.cur.rowcount) + "Row(s) affected.")
        self.conn.commit()
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def view_pilot_schedule(self):
      try:
        self.get_connection()
        print("View Pilot Schedule. List of Pilots: ")
        self.cur.execute(self.sql_select_pilot_list)
        result = self.cur.fetchall()
        self.print_table(result, 'Pilot', ['Pilot ID', 'Name'])
        print("")
        pilot_id = int(input("Enter Pilot ID: "))
        self.cur.execute(self.sql_view_pilot_schedule, str(pilot_id,))
        result = self.cur.fetchall()

        if result:
          self.print_table(result, 'Pilot', ['Name', 'Schedule'])
        else:
          print("Cannot Find Pilot in the Database")

      except Exception as e:
        print(e)
      finally:
        self.conn.close()


  def view_destination(self):
    try:
      self.get_connection()
      print("Select Flight ID")
      self.cur.execute("DROP VIEW IF EXISTS DestinationInfo")
      self.cur.execute(f'''
        CREATE VIEW DestinationInfo AS
        SELECT FlightID, DestinationID, City, Country 
        FROM FlightInfo JOIN Destination 
        WHERE FlightInfo.Destination = Destination.DestinationID
      ''')
      flight_id = int(input("Enter Flight ID: "))
      self.cur.execute(f"SELECT * FROM DestinationInfo WHERE FlightID = {flight_id}")
      result = self.cur.fetchall()
      if result:
        self.print_table(result, 'DestinationInfo', None)
      else:
        print("Cannot Find Flight in the Database")
    except Exception as e:
      print(e)
    finally:
      self.conn.commit()
      self.conn.close()


  def select_all_pilots(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all_pilots)
      result = self.cur.fetchall()
      self.print_table(result, 'Pilot')
    except Exception as e:
      print(e)
    finally:
      self.conn.close()


  def print_table(self, result, table, columns=None):
    try:
      pd.set_option("display.max_columns", None)
      pd.set_option("display.width", 300)
      if columns is not None:
        print(pd.DataFrame(result, columns=columns))
      elif columns is None:
        print(pd.DataFrame(result, columns=self.find_columns(table)))
      else:
        print("Cannot Find Results in the Database")
    except Exception as e:
      print(e)


  def find_columns(self, table):
    try:
      self.get_connection()
      self.cur.execute(f"SELECT * FROM {table} LIMIT 0")
      columns = [description[0] for description in self.cur.description]
      if columns:
        return columns
      else:
        print(f"Cannot Find the Table '{table}' in the Database")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()


# The main function will parse arguments.
# These argument will be definded by the users on the console.
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
      db_ops.delete_data()
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
      db_ops.delete_data()
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
      db_ops.delete_data()
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
