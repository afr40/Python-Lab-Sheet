import sqlite3
import pandas as pd


# All SQL Queries will be collected here since DBOperations handles queries differently
# NOTE: This queries are not commited to the database so any changes will not be reflected


db = sqlite3.connect('test.db')
cursor = db.cursor()

def create_table_flight(result):
    cursor.execute("SELECT * FROM FlightRoute LIMIT 0")
    columns = [description[0] for description in cursor.description]
    df = pd.DataFrame(result, columns=columns)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 300)
    print(df)
    print('----------')
    # print("\n")


# 1. Flight retrieval based on multiple criteria, such as destination, status or date
print("\n")
print("Flight Retrival: Destination is Madrid-MAD")
destination_query = "SELECT * FROM FlightRoute WHERE Destination = 'Madrid-MAD'"
cursor.execute(destination_query)
destination_results = cursor.fetchall()
create_table_flight(destination_results)

print("Flight Retrival: Delayed Flights")
status_query = "SELECT * FROM FlightRoute WHERE Status = 'Delayed'"
cursor.execute(status_query)
status_results = cursor.fetchall()
create_table_flight(status_results)

print("Flight Retrival: Flights Between February and April")
months_query = "SELECT * FROM FlightRoute WHERE Departure_date > '2025-02-01' AND Departure_date < '2025-04-30'"
cursor.execute(months_query)
months_result = cursor.fetchall()
create_table_flight(months_result)

print("Flight Retrival: Flights Between February and April")
months_query = "SELECT * FROM FlightRoute WHERE Departure_date > '2025-02-01' AND Departure_date < '2025-04-30'"
cursor.execute(months_query)
months_result = cursor.fetchall()
create_table_flight(months_result)


# 2. Update Flight Schedules (Departure time and Status)
print("\n")
print("Update Flight Schedules: Time")
time_query = "UPDATE FlightRoute SET Schedule_time = '11:15' WHERE FlightID = 1"
cursor.execute(time_query)
status_query = "UPDATE FlightRoute SET Status = 'Delayed' WHERE FlightID = 1"
cursor.execute(status_query)
updated_query = "SELECT * FROM FlightRoute WHERE FlightID = 1"
cursor.execute(updated_query)
updated_result = cursor.fetchall()
create_table_flight(updated_result)


# 3. Pilot Assigment and Schedule
print("\n")
print("Pilot Assigment and Pilot Schedule")
assigment_query = "UPDATE FlightRoute SET PilotID = 4 WHERE FlightID = 1"
cursor.execute(assigment_query)
cursor.execute("SELECT * FROM FlightRoute WHERE FlightID = 1")
assigment_result = cursor.fetchall()
create_table_flight(assigment_result)

schedule_query = "SELECT * FROM Pilot WHERE PilotID = 4"
cursor.execute(schedule_query)
cursor.execute("SELECT Name, Schedule FROM Pilot WHERE PilotID = 4")
schedule_result = cursor.fetchall()
print(pd.DataFrame(schedule_result, columns=['Name', 'Schedule']))


# 4. Destination Management: View / Update Destination
print("\n")
view_query = "SELECT FlightID, Origin, Destination FROM FlightRoute WHERE FlightID = 4"
cursor.execute(view_query)
view_results = cursor.fetchall()
print(pd.DataFrame(view_results, columns=['FlightID', 'Origin', 'Destination']))
print("\n")

update_destination = "UPDATE FlightRoute SET Destination = 'Singapore' WHERE FlightID = 4"
cursor.execute(update_destination)
view_query = "SELECT FlightID, Origin, Destination FROM FlightRoute WHERE FlightID = 4"
cursor.execute(view_query)
view_results = cursor.fetchall()
print(pd.DataFrame(view_results, columns=['FlightID', 'Origin', 'Destination']))
print("--------")


# 5. Additional Queries
# 5.1 Number of Flights Assign to Each Pilot

query = '''
    SELECT Name, FlightRoute.PilotID, COUNT(*)
    FROM FlightRoute JOIN Pilot 
    WHERE FlightRoute.PilotID = Pilot.PilotID 
    GROUP BY FlightRoute.PilotID HAVING COUNT(*) > 1
    ORDER BY COUNT(*) DESC
    '''

cursor.execute(query)
result = cursor.fetchall()
print(pd.DataFrame(result, columns=['Name', 'PilotID', 'Pilot Count']))

# 5.2 Most Popular Destinations and Countries
print("\n")
query= '''
    SELECT Destination, Country, Count(*)
    FROM FlightRoute JOIN Destination 
    WHERE FlightRoute.Destination = Destination.DestinationID 
    GROUP BY Destination HAVING COUNT(*) > 1
    ORDER BY Count(*) DESC
'''

cursor.execute(query)
result = cursor.fetchall()
print(pd.DataFrame(result, columns=['Destination', 'Country', 'No.Flights']))
