import sqlite3
import pandas as pd
from database_utils.database_setup import *
from database_utils.sql_queries import SQLQueries


class DBOperations:
    """
    Performs actions in the database.
    """

    def __init__(self):
        try:
            self.sql = SQLQueries()
            self.conn = sqlite3.connect("flightsDB.db")
            self.cur = self.conn.cursor()
            create_tables(self.cur)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def get_connection(self):
        self.conn = sqlite3.connect("flightsDB.db")
        self.cur = self.conn.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")


    def create_table(self):
        try:
            self.get_connection()
            drop_tables(self.cur)
            create_tables(self.cur)
            insert_sample_data(self.cur)
            self.conn.commit()
            print("Tables Created and Sample Data Added Successfully")
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
        """
        Inserts data into the table using a table instance the name of a table and the insert query.
        """
        try:
            self.get_connection()
            columns = self.find_columns(table)
            self.print_table(self.cur.execute(f"SELECT * FROM {table}"), table)

            print("")
            print(f"Add New Entry to {table} Records")
            print("---------------------------------")

            class_variables = table_instance.__dict__
            i = 0
            for class_variable in class_variables:
                method = "set_" + class_variable
                method = getattr(table_instance, method)
                if "ID" in columns[i]:
                    data_to_insert = input(f"Enter a {columns[i]} (Unique): ")
                else:
                    data_to_insert = input(f"Enter {columns[i]}: ")
                i = i + 1
                method(data_to_insert)

            self.cur.execute(insert_query, tuple(str(table_instance).split("\n")))
            self.conn.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def update_data(self, table, primary_key):
        """
        Updates data into the table using generic queries, and printing the tables before updating
        """
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

            self.cur.execute(sql_update_data, (update_information, table_id))
            if self.cur.rowcount != 0:
                print(str(self.cur.rowcount) + " Row(s) affected.")
                self.conn.commit()
            else:
                print("Cannot find this record in the database")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def delete_data(self, table, primary_key):
        """
        Deletes data from the table using generic queries.

        :param table: Targeted table to delete data from
        :param primary_key: Primary key to find the entry
        """
        try:
            self.get_connection()
            print("")
            self.print_table(self.cur.execute(f"SELECT * FROM {table}"), table, None)
            delete_id = str(input(f"\nEnter {primary_key} Record to Delete: "))

            self.cur.execute(f"DELETE FROM {table} WHERE {primary_key} = ?", (delete_id,))

            if self.cur.rowcount != 0:
                print(str(self.cur.rowcount) + " Row(s) affected.")
                self.conn.commit()
            else:
                print("Cannot find this record in the database")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def select_all(self, sql_select_all, table, columns=None):
        """
        Select all data from a particular table and prints its data
        """
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
        """
        Searches for a scheduled fligth ID and then prints its data
        """
        try:
            self.get_connection()
            schedule_id = int(input("Enter Scheduled Flight ID: "))
            self.cur.execute(self.sql.search_flight, (str(schedule_id),))
            result = self.cur.fetchone()
            if type(result) == type(tuple()):
                for index, detail in enumerate(result):
                    if index == 0:
                        print("---------------")
                        print("Flight ID: " + str(detail))
                    elif index == 1:
                        print("Schedule ID: " + str(detail))
                    elif index == 2:
                        print("Flight Number: " + detail)
                    elif index == 3:
                        print("Flight Origin: " + detail)
                    elif index == 4:
                        print("Flight City Origin: " + detail)
                    elif index == 5:
                        print("Flight Destination: " + detail)
                    elif index == 6:
                        print("Flight City Destination: " + detail)
                    elif index == 7:
                        print("Departure Date: " + detail)
                    elif index == 8:
                        print("Departure Time: " + detail)
                    else:
                        print("Status: " + detail)
                        print("---------------")
            else:
                print("No Record")

        except Exception as e:
            print(e)
        finally:
            self.conn.close()


    def view_pilot_schedule(self):
        """
        Searches for pilots schedule from a list of pilots
        """
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
        """
        Prints details of route destination from a Fligth Route ID
        """
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
        """
        Utility function for printing table

        :param result: Takes the result of the SQL query
        :param table: table name
        :param columns: Custom column names
        :return:
        """
        try:
            pd.set_option("display.max_columns", None)
            pd.set_option("display.width", 300)
            print("")
            if columns is not None:
                print(pd.DataFrame(result, columns=columns))
            elif columns is None:
                print(pd.DataFrame(result, columns=self.find_columns(table)))
            else:
                print("Cannot Find Results in the Database")
        except Exception as e:
            print(e)


    def find_columns(self, table):
        """
        Utility functino for finding columns names in a table
        """
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
