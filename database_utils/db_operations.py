import sqlite3
import pandas as pd
from database_utils.database_setup import *
from database_utils.sql_queries import SQLQueries
from table_utils.flight_route import FlightRoute
from table_utils.airport import Airport
from table_utils.pilot import Pilot



class DBOperations:

    def __init__(self):
        try:
            self.sql = SQLQueries()
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
            print("Tables FlightRoute, Destination and Pilot Created Successfully")
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


    def insert_data(self, table_instance, table, insert_query):
        try:
            self.get_connection()
            columns = self.find_columns(table)
            self.print_table(self.cur.execute(f"SELECT * FROM {table}"), table)

            print("")
            print(f"Add New Entry to {table} Records")
            print("---------------------------------")

            methods = dir(table_instance)
            i = 0
            for method in methods:
                if method.startswith("set_"):
                    method = getattr(table_instance, method)
                    if "ID" in columns[i]:
                        data_to_insert = input(f"Enter a {columns[i]} (Unique): ")
                    else:
                        data_to_insert = input(f"Enter {columns[i]}: ")
                    i = i + 1
                    method(data_to_insert)
                else:
                    pass
            print(str(table_instance))
            self.cur.execute(insert_query, tuple(str(table_instance).split("\n")))
            self.conn.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def insert_flight_data(self):
        try:
            self.get_connection()
            flight = FlightRoute()

            flight.set_flight_id(int(input("Enter FlightID (Unique): ")))
            print('')
            self.print_table(self.cur.execute("SELECT AirportID FROM Airport"), 'Destination', ['Locations Available'])
            print('')
            flight.set_flight_origin(str(input("Enter Flight Origin (Full Location Name): ")))
            flight.set_flight_destination(str(input("Enter Flight Destination (Full Location Name): ")))
            print('')
            self.print_table(self.cur.execute("SELECT PilotID, Name FROM Pilot"), 'Pilot', ['Pilot ID', 'Name'])
            print('')
            flight.flight_number = str(input("Enter Flight Number: "))

            self.cur.execute(self.sql.insert_airport, tuple(str(flight).split("\n")))
            self.conn.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def insert_airport_data(self):
        try:
            self.get_connection()
            airport = Airport()

            airport.set_airport_id(int(input("Enter Destination ID: ")))
            airport.set_city(str(input("Enter Destination City: ")))
            airport.set_country(str(input("Enter Destination Country: ")))
            # airport.set_airport_id(airport.get_airport_id().split("-")[1])

            self.cur.execute(self.sql.insert_airport, tuple(str(airport).split("\n")))
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
            pilot.set_airport_base(str(input("Enter Pilot Airport Base: ")))
            pilot.set_name(str(input("Enter Pilot Name: ")))
            pilot.set_status(str(input("Enter Pilot Status (Optional): ")))

            self.cur.execute(self.sql.insert_pilot, tuple(str(pilot).split("\n")))
            self.conn.commit()
            print("Inserted data successfully")
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
            self.print_table(self.cur.execute(f"SELECT * FROM {table}"), table, columns)
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
    def delete_data(self, table, primary_key):
        try:
            self.get_connection()
            print("")
            self.print_table(self.cur.execute(f"SELECT * FROM {table}"), table, None)
            delete_id = str(input(f"\nEnter {primary_key} Record to Delete: "))

            self.cur.execute(f"DELETE FROM {table} WHERE {primary_key} = ?", (delete_id,))

            if self.cur.rowcount != 0:
                print(str(self.cur.rowcount) + "Row(s) affected.")
                self.conn.commit()
            else:
                print("Cannot find this record in the database")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def select_all(self, sql_select_all, table, columns=None):
        try:
            self.get_connection()
            self.cur.execute(sql_select_all)
            result = self.cur.fetchall()
            self.print_table(result, table, columns)
        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def search_data(self):
        try:
            self.get_connection()
            flight_id = int(input("Enter FlightNo: "))
            self.cur.execute(self.sql.search_flight_route, (str(flight_id),))
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
                    else:
                        print("Departure Date: " + detail)
                        print("---------------")
            else:
                print("No Record")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def view_pilot_schedule(self):
        try:
            self.get_connection()
            print("View Pilot Schedule. List of Pilots: ")
            self.cur.execute(self.sql.select_pilot_list)
            result = self.cur.fetchall()
            self.print_table(result, 'Pilot', ['Pilot ID', 'Name'])
            print("")
            pilot_id = int(input("Enter Pilot ID: "))
            self.cur.execute(self.sql.select_all_pilots, str(pilot_id, ))
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
            self.cur.execute('''
                CREATE VIEW DestinationInfo AS
                SELECT FlightID, AirportID, City, Country 
                FROM FlightRoute JOIN Airport 
                WHERE FlightRoute.Destination = Airport.AirportID
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


    def print_table(self, result, table=None, columns=None):
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
        # finally:
        #     self.conn.close()
