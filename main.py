import sqlite3
import pandas as pd
from database_setup import DatabaseSetup

# Define DBOperation class to manage all data into the database.
# Give a name of your choice to the database


class DBOperations:
  # sql_create_table_firsttime = "create table if not exists "

  # sql_create_table = "create table TableName"

  sql_insert = "INSERT INTO FlightInfo VALUES (?, ?, ?, ?, ?, ?, ?)"
  sql_select_all = "SELECT * FROM FlightInfo"
  sql_search = "SELECT * FROM FlightInfo WHERE FlightID = ?"
  sql_alter_data = ""
  sql_update_data = ""
  sql_delete_data = ""
  # sql_drop_table = ""

  def __init__(self):
    try:
      self.database_setup = DatabaseSetup()
      # self.database_setup.drop_tables()
      self.database_setup.create_tables()
      # self.database_setup.insert_sample_data()
      self.database_setup.commit_database()

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
      flight.set_flight_id(str(input("Enter FlightID: ")))
      flight.set_flight_origin(str(input("Enter Flight Origin: ")))
      flight.set_flight_destination(str(input("Enter Flight Destination: ")))
      flight.set_pilot_id(int(input("Enter Pilot ID: ")))
      flight.set_status(str(input("Enter Flight Status: ")))
      flight.set_schedule_time(str(input("Enter Flight Schedule Time: ")))
      flight.set_departure_date(str(input("Enter Departure Date: ")))

      # print(flight)
      print(tuple(str(flight).split("\n")))
      self.cur.execute(self.sql_insert, tuple(str(flight).split("\n")))
      # print(self.sql_insert)
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

      df = pd.DataFrame(result, columns=['Flight ID', 'Origin', 'Destination', 'Pilot ID', 'Status', 'Schedule Time', 'Departure Date'])
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
      self.cur.execute(self.sql_search, tuple(str(flight_id)))
      result = self.cur.fetchone()
      if type(result) == type(tuple()):
        for index, detail in enumerate(result):
          if index == 0:
            print("Flight ID: " + str(detail))
          elif index == 1:
            print("Flight Origin: " + detail)
          elif index == 2:
            print("Flight Destination: " + detail)
          else:
            print("Status: " + str(detail))
      else:
        print("No Record")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()

  def update_data(self):
    try:
      self.get_connection()

      # Update statement

      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


# Define Delete_data method to delete data from the table. The user will need to input the flight id to delete the corrosponding record.

  def delete_data(self):
    try:
      self.get_connection()

      if result.rowcount != 0:
        print(str(result.rowcount) + "Row(s) affected.")
      else:
        print("Cannot find this record in the database")

    except Exception as e:
      print(e)
    finally:
      self.conn.close()


class FlightInfo:

  def __init__(self):
    self.flight_id = 0
    self.flight_origin = ''
    self.flight_destination = ''
    self.pilot_id = 0
    self.status = ''
    self.schedule_time = ''
    self.departure_date = ''

  # Set methods
  def set_flight_id(self, flight_id):
    self.flight_id = flight_id

  def set_flight_origin(self, flight_origin):
    self.flight_origin = flight_origin

  def set_flight_destination(self, flight_destination):
    self.flight_destination = flight_destination

  def set_pilot_id(self, pilot_id):
    self.pilot_id = pilot_id

  def set_status(self, status):
    self.status = status

  def set_schedule_time(self, schedule_time):
    self.schedule_time = schedule_time

  def set_departure_date(self, departure_date):
    self.departure_date = departure_date

  # Get methods
  def get_flight_id(self):
    return self.flight_id

  def get_flight_origin(self):
    return self.flight_origin

  def get_flight_destination(self):
    return self.flight_destination

  def get_status(self):
    return self.status

  def get_pilot_id(self):
    return self.pilot_id

  def get_schedule_time(self):
    return self.schedule_time

  def get_departure_date(self):
    return self.departure_date

  def __str__(self):
    return str(
      self.flight_id
    ) + "\n" + self.flight_origin + "\n" + self.flight_destination + "\n" + str(self.pilot_id) + "\n" + str(
      self.status) + "\n" + str(self.schedule_time) + "\n" + str(self.departure_date)


# The main function will parse arguments.
# These argument will be definded by the users on the console.
# The user will select a choice from the menu to interact with the database.

while True:
  print("\n Menu:")
  print("**********")
  print(" 1. Create table FlightInfo")
  print(" 2. Insert data into FlightInfo")
  print(" 3. Select all data from FlightInfo")
  print(" 4. Search a flight")
  print(" 5. Update data some records")
  print(" 6. Delete data some records")
  print(" 7. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  db_ops = DBOperations()
  if __choose_menu == 1:
    db_ops.create_table()
  elif __choose_menu == 2:
    db_ops.insert_data()
  elif __choose_menu == 3:
    db_ops.select_all()
  elif __choose_menu == 4:
    db_ops.search_data()
  elif __choose_menu == 5:
    db_ops.update_data()
  elif __choose_menu == 6:
    db_ops.delete_data()
  elif __choose_menu == 7:
    exit(0)
  else:
    print("Invalid Choice")
