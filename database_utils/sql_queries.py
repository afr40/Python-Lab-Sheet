class SQLQueries:
    """
    SQL Queries to interact with the database.

    Different queries: selection, update, delete and insertions are defined, as well as
    the primary keys and tables names for easy access in the whole application.
    """

    # sql_view_pilot_schedule = "SELECT Name, Schedule FROM Pilot WHERE PilotID = ?"
    search_flight_route = "SELECT * FROM FlightRoute WHERE FlightID = ?"
    search_flight_schedule = "SELECT * FROM FlightSchedule WHERE FlightID = ?"
    search_pilot_available = "SELECT * FROM Pilot WHERE Status = 'Available'"
    search_flight = '''
        SELECT FlightID, ScheduleID, Flight_number, Origin, o.City AS CityOrigin, Destination, d.City AS CityDestination,
            Departure_date, Departure_time, Status
        FROM (FlightRoute NATURAL JOIN FlightSchedule) 
        JOIN Airport AS o ON Origin = o.AirportID
        JOIN Airport AS d ON Destination = d.AirportID
        WHERE ScheduleID = ? 
        ORDER BY FlightID
    '''

    # Select all entries for the tables
    select_all_flight_routes = "SELECT * FROM FlightRoute"
    select_all_flight_schedule = "SELECT * FROM FlightSchedule"
    select_all_flights = '''
        SELECT FlightID, ScheduleID, Flight_number, Origin, o.City AS CityOrigin, Destination, d.City AS CityDestination,
            Departure_date, Departure_time, Status
        FROM (FlightRoute NATURAL JOIN FlightSchedule) 
        JOIN Airport AS o ON Origin = o.AirportID
        JOIN Airport AS d ON Destination = d.AirportID
        ORDER BY FlightID
    '''
    select_all_flights_columns = ['FlightID', 'ScheduleID', 'Flight Number', 'Origin', 'Origin City',
                                  'Destination', 'Destination City', 'Departure Date', 'Departure Time', 'Status']
    select_all_pilot_schedules = '''
        SELECT PilotID, FlightRoute.FlightID, Name, Role, Origin, Destination, Flight_number
        FROM PilotSchedule NATURAL JOIN Pilot
        JOIN FlightSchedule ON FlightSchedule.ScheduleID = PilotSchedule.ScheduleID
        JOIN FlightRoute ON FlightRoute.FlightID = FlightSchedule.FlightID
    '''
    select_all_airports = "SELECT * FROM Airport"
    select_all_pilots = "SELECT * FROM Pilot"
    select_pilot_list = "SELECT PilotID, Name FROM Pilot"

    # Insert queries
    insert_flight_route = "INSERT INTO FlightRoute VALUES (?, ?, ?, ?)"
    insert_flight_schedule = "INSERT INTO FlightSchedule VALUES (?, ?, ?, ?, ?)"
    insert_airport = "INSERT INTO Airport VALUES (?, ?, ?, ?)"
    insert_pilot = "INSERT INTO Pilot VALUES (?, ?, ?, ?)"

    # Delete queries
    delete_flight_route = "DELETE FROM FlightRoute WHERE FlightID = ?"
    delete_flight_schedule = "DELETE FROM FlightSchedule WHERE ScheduleID = ?"
    delete_pilot = "DELETE FROM Pilot WHERE PilotID = ?"
    delete_pilot_schedule = "DELETE FROM PilotSchedule WHERE PilotID = ?"
    delete_airport = "DELETE FROM Airport WHERE AirportID = ?"

    # Tables names
    flight_route_table = 'FlightRoute'
    flight_schedule_table = 'FlightSchedule'
    flight_records_table = 'FlightRecords'
    airport_table = 'Airport'
    pilot_table = 'Pilot'
    pilot_schedule_table = 'PilotSchedule'

    # Primary keys
    flight_route_pk = 'FlightID'
    flight_schedule_pk = 'ScheduleID'
    airport_pk = 'AirportID'
    pilot_pk = 'PilotID'

