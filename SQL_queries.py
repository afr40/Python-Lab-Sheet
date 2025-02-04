import sqlite3
import pandas as pd


# All SQL Queries will be collected here since DBOperations handles queries differently
# NOTE: This queries are not commited to the database so any changes will not be reflected


db = sqlite3.connect('flightsDB.db')
cursor = db.cursor()

def create_table_flight(result, table = 'Flights'):
    try:
        cursor.execute(f"SELECT * FROM {table} LIMIT 0")
        columns = [description[0] for description in cursor.description]
        df = pd.DataFrame(result, columns=columns)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 300)
        print("\n")
        print(df)
        print('\n----------')
    except Exception as e:
        print(e)


# 1. Flight retrieval based on multiple criteria, such as destination, status or date
print("\nFlight Retrival: Destination is Manchester")
flights_query = '''
    CREATE VIEW IF NOT EXISTS Flights AS
    SELECT FlightID, ScheduleID, Flight_number, Origin, o.City AS CityOrigin, Destination, d.City AS CityDestination,
        Departure_date, Departure_time, Status
    FROM (FlightRoute NATURAL JOIN FlightSchedule)
    JOIN Airport AS o ON Origin = o.AirportID
    JOIN Airport AS d ON Destination = d.AirportID
    ORDER BY FlightID
'''
cursor.execute(flights_query)
cursor.fetchall()
db.commit()
cursor.execute("SELECT * FROM Flights WHERE CityDestination = 'Manchester' ")
destination_results = cursor.fetchall()
create_table_flight(destination_results, 'Flights')

print("\nFlight Retrival: Delayed Flights")
status_query = "SELECT * FROM Flights WHERE Status = 'Delayed'"
cursor.execute(status_query)
status_results = cursor.fetchall()
create_table_flight(status_results, 'Flights')

print("\nFlight Retrival: Flights Between February and April")
months_query = "SELECT * FROM Flights WHERE Departure_date > '2025-02-01' AND Departure_date < '2025-04-30'"
cursor.execute(months_query)
months_result = cursor.fetchall()
create_table_flight(months_result)


# 2. Update Flight Schedules (Departure time and Status)
print("\n")
print("Update Flight Schedules: Time")
time_query = "UPDATE FlightSchedule SET Departure_time = '11:15' WHERE ScheduleID = 3"
cursor.execute(time_query)
status_query = "UPDATE FlightSchedule SET Status = 'Delayed' WHERE ScheduleID = 3"
cursor.execute(status_query)
updated_query = "SELECT * FROM FlightSchedule WHERE ScheduleID = 3"
cursor.execute(updated_query)
updated_result = cursor.fetchall()
create_table_flight(updated_result, 'FlightSchedule')


# 3. Pilot Assigment and Schedule
print("\n")
print("Pilot Assigment and Pilot Schedule")
assigment_query = "UPDATE PilotSchedule SET PilotID = 4 WHERE ScheduleID = 1"
cursor.execute(assigment_query)
cursor.execute("SELECT * FROM PilotSchedule WHERE ScheduleID = 1")
assigment_result = cursor.fetchall()
create_table_flight(assigment_result, 'PilotSchedule')

schedule_query = "SELECT * FROM Pilot WHERE PilotID = 4"
cursor.execute(schedule_query)
cursor.execute('''
    SELECT Name, Departure_date, Departure_time, Origin, Destination 
    FROM PilotSchedule NATURAL JOIN Pilot
    JOIN FlightSchedule ON FlightSchedule.ScheduleID = PilotSchedule.ScheduleID = FlightSchedule.ScheduleID
    JOIN FlightRoute ON FlightRoute.FlightID = FlightSchedule.FlightID
    WHERE PilotID = 4
''')
schedule_result = cursor.fetchall()
print(pd.DataFrame(schedule_result, columns=['Name', 'Departure_date', 'Departure Time','Origin', 'Destination']))


# 4. Destination Management: View / Update Destination
print("\n")
view_query = "SELECT FlightID, Origin, Destination FROM FlightRoute WHERE FlightID = 404"
cursor.execute(view_query)
view_results = cursor.fetchall()
print(pd.DataFrame(view_results, columns=['FlightID', 'Origin', 'Destination']))
print("\n")

update_destination = "UPDATE FlightRoute SET Destination = 'Singapore' WHERE FlightID = 404"
cursor.execute(update_destination)
view_query = "SELECT FlightID, Origin, Destination FROM FlightRoute WHERE FlightID = 404"
cursor.execute(view_query)
view_results = cursor.fetchall()
print(pd.DataFrame(view_results, columns=['FlightID', 'Origin', 'Destination']))
print("--------")


# 5. Additional Queries
# 5.1 Number of Flights Assign to Each Pilot

query = '''
    SELECT Name, PilotSchedule.ScheduleID, COUNT(*)
    FROM PilotSchedule Natural JOIN Pilot
    GROUP BY PilotSchedule.PilotID HAVING COUNT(*) > 1
    ORDER BY COUNT(*) DESC
    '''

cursor.execute(query)
result = cursor.fetchall()
print(pd.DataFrame(result, columns=['Name', 'PilotID', 'Pilot Count']))

# 5.2 Most Popular Destinations and Countries
print("\n")
query= '''
    SELECT Destination, City, Country, Count(*)
    FROM FlightRoute JOIN Airport
    JOIN FlightSchedule ON FlightRoute.FlightID = FlightSchedule.FlightID
    WHERE FlightRoute.Destination = Airport.AirportID
    GROUP BY Destination HAVING COUNT(*) > 1
    ORDER BY Count(*) DESC
'''

cursor.execute(query)
result = cursor.fetchall()
print(pd.DataFrame(result, columns=['Airport', 'City', 'Country', 'No.Flights']))
