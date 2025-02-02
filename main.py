import sqlite3
import pandas as pd
from database_setup import DatabaseSetup
from table_utils.flight_info import FlightInfo

# Define DBOperation class to manage all data into the database.


class DBOperations:
  # sql_create_table_firsttime = "create table if not exists "

  # sql_create_table = "create table TableName"

  sql_insert = "INSERT INTO FlightInfo VALUES (?, ?, ?, ?, ?, ?, ?)"
  sql_select_all = "SELECT * FROM FlightInfo"
  sql_search = "SELECT * FROM FlightInfo WHERE FlightID = ?"
  # sql_alter_data = "ALTER TABLE FlightInfo ADD COLUMN FlightID INTEGER"
  # sql_update_data = f"UPDATE FlightInfo SET {__update_choice} = ? WHERE FlightID = ?"
  sql_delete_data = "DELETE FROM FlightInfo WHERE FlightID = ?"
  # sql_drop_table = ""

  def __init__(self):
    try:
      self.database_setup = DatabaseSetup()
      # self.database_setup.drop_tables()
      # self.database_setup.create_tables()
      # self.database_setup.insert_sample_data()
      # self.database_setup.commit_database()

      self.conn = sqlite3.connect("test.db")
      self.cur = self.conn.cursor()
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def get_connection(self):
    self.conn = sqlite3.connect("test.db")
    self.cur = self.conn.cursor()

  # def create_table(self):
  #   try:
  #     self.get_connection()
  #     self.cur.execute(self.sql_create_table)
  #     self.conn.commit()
  #     print("Table created successfully")
  #   except Exception as e:
  #     print(e)
  #   finally:
  #     self.conn.close()

  def insert_data(self):
    try:
      self.get_connection()
      flight = FlightInfo()

      flight.set_flight_id(int(input("Enter FlightID: ")))
      flight.set_flight_origin(str(input("Enter Flight Origin: ")))
      flight.set_flight_destination(str(input("Enter Flight Destination: ")))
      flight.set_pilot_id(int(input("Enter Pilot ID: ")))
      flight.set_status(str(input("Enter Flight Status: ")))
      flight.set_schedule_time(str(input("Enter Flight Schedule Time: ")))
      flight.set_departure_date(str(input("Enter Departure Date: ")))

      self.cur.execute(self.sql_insert, tuple(str(flight).split("\n")))
      self.conn.commit()
      print("Inserted data successfully")
    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def select_all(self):
    try:
      self.get_connection()
      self.cur.execute(self.sql_select_all)
      result = self.cur.fetchall()

      # Find columns from FlightInfo table
      self.cur.execute("SELECT * FROM FlightInfo LIMIT 0")
      columns = [description[0] for description in self.cur.description]

      # Print the FlightInfo in table format
      df = pd.DataFrame(result, columns=columns)
      pd.set_option('display.max_columns', None)
      pd.set_option('display.width', 300)
      print(df)
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

  def update_data(self):
    try:
      self.get_connection()
      self.cur.execute("SELECT * FROM FlightInfo LIMIT 0")
      columns = [description[0] for description in self.cur.description]

      flight_id = int(input("Enter Flight ID: "))
      print("Choose Information to Update")
      print("---------------")
      print("Flight ID: " + str(flight_id))
      for index, column in enumerate(columns, start=1):
        print(f"{index}. Update {column}")

      print("\n")
      update_choice = int(input("Enter Update Index: "))
      update_information = str(input("Enter Update: "))
      sql_update_data = f"UPDATE FlightInfo SET {columns[update_choice - 1]} = ? WHERE FlightID = ?"
      self.cur.execute(sql_update_data, (update_information, flight_id))

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



# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

while True:
  print("\n Menu:")
  print("**********")
  print(" 1. Show all Flights Records")
  print(" 2. Search Flights Records")
  print(" 3. Add Flight Record")
  print(" 4. Update Flight Information")
  print(" 5. Delete Flight Record")
  print(" 6. Assign Pilot to a Flight")
  print(" 7. View Pilot Schedule")
  print(" 8. View Destination Information")
  print(" 9. Update Destination Information")
  print(" 10. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    db_ops.select_all()
  elif __choose_menu == 2:
    db_ops.search_data()
  elif __choose_menu == 3:
    db_ops.insert_data()
  elif __choose_menu == 4:
    db_ops.update_data()
  elif __choose_menu == 5:
    db_ops.delete_data()
  elif __choose_menu == 6:
    db_ops.search_data()
  elif __choose_menu == 7:
    db_ops.select_all()
  elif __choose_menu == 8:
    db_ops.delete_data()
  elif __choose_menu == 9:
    db_ops.select_all()
  elif __choose_menu == 10:
    exit(0)
  else:
    print("Invalid Choice")
