def drop_tables(cursor):
    query = "DROP VIEW IF EXISTS DestinationInfo"
    cursor.execute(query)
    query = "DROP TABLE IF EXISTS FlightRoute"
    cursor.execute(query)
    query = "DROP TABLE IF EXISTS FlightSchedule"
    cursor.execute(query)
    query = "DROP TABLE IF EXISTS Airport"
    cursor.execute(query)
    query = "DROP TABLE IF EXISTS Pilot"
    cursor.execute(query)
    query = "DROP TABLE IF EXISTS PilotSchedule"
    cursor.execute(query)


def create_tables(cursor):
    query = '''CREATE TABLE IF NOT EXISTS FlightRoute (
        FlightID INTEGER PRIMARY KEY,
        Origin TEXT NOT NULL,
        Destination TEXT NOT NULL,
        Flight_number TEXT NOT NULL,
        CHECK (Origin <> Destination), 
        FOREIGN KEY(Origin) REFERENCES Airport(AirportID) ON DELETE CASCADE,
        FOREIGN KEY(Destination) REFERENCES Airport(AirportID) ON DELETE CASCADE
    )'''
    cursor.execute(query)

    query = '''CREATE TABLE IF NOT EXISTS FlightSchedule (
        ScheduleID INTEGER PRIMARY KEY NOT NULL,
        FlightID INTEGER NOT NULL,
        Departure_time TIME NOT NULL,
        Departure_date DATE NOT NULL,
        Status TEXT CHECK (Status IN ('Scheduled', 'Delayed', 'Cancelled', 'Completed', 'On Route')),
        CHECK (Departure_time IS strftime('%H:%M', Departure_time)),
        CHECK (Departure_date IS strftime('%Y-%m-%d', Departure_date)),
        FOREIGN KEY(FlightID) REFERENCES FlightRoute(FlightID) ON DELETE CASCADE
    )'''
    cursor.execute(query)

    query = '''CREATE TABLE IF NOT EXISTS Airport (
        AirportID TEXT PRIMARY KEY NOT NULL,
        City TEXT NOT NULL,
        Country TEXT NOT NULL,
        ICAO TEXT
    )'''
    cursor.execute(query)

    query = '''CREATE TABLE IF NOT EXISTS Pilot (
        PilotID INTEGER PRIMARY KEY NOT NULL,
        Airport_base TEXT,
        Name TEXT NOT NULL,
        Status TEXT CHECK (Status IN ('Available', 'Unavailable', 'On Leave', 'Sick Leave', 'On Call', '')),
        FOREIGN KEY (Airport_base) REFERENCES Airport(AirportID)
    )'''
    cursor.execute(query)

    query = '''CREATE TABLE IF NOT EXISTS PilotSchedule (
        PilotID INTEGER NOT NULL,
        ScheduleID INTEGER NOT NULL,
        Role TEXT NOT NULL CHECK (Role IN ('Captain', 'Senior First Officer', 'First Officer', 'Second Officer')),
        PRIMARY KEY(PilotID, ScheduleID),
        FOREIGN KEY (PilotID) REFERENCES Pilot(PilotID) ON DELETE SET NULL,
        FOREIGN KEY (ScheduleID) REFERENCES FlightSchedule(ScheduleID)
    )'''
    cursor.execute(query)


def insert_sample_data(cursor):
    # Insert pilot sample data
    cursor.execute("INSERT INTO Pilot VALUES (1, 'JFK', 'John Smith', 'Available')")
    cursor.execute("INSERT INTO Pilot VALUES (2, 'LAX', 'Alice Johnson', 'Unavailable')")
    cursor.execute("INSERT INTO Pilot VALUES (3, 'ORD', 'Michael Brown', 'On Leave')")
    cursor.execute("INSERT INTO Pilot VALUES (4, 'MIA', 'Sarah Davis', 'Sick Leave')")
    cursor.execute("INSERT INTO Pilot VALUES (5, 'DFW', 'David Wilson', 'On Call')")
    cursor.execute("INSERT INTO Pilot VALUES (6, 'ATL', 'James Martinez', 'Available')")
    cursor.execute("INSERT INTO Pilot VALUES (7, 'SFO', 'Mary Taylor', 'Unavailable')")
    cursor.execute("INSERT INTO Pilot VALUES (8, 'SEA', 'Robert Anderson', 'On Leave')")
    cursor.execute("INSERT INTO Pilot VALUES (9, 'BOS', 'Patricia Thomas', 'Sick Leave')")
    cursor.execute("INSERT INTO Pilot VALUES (10, 'DEN', 'Linda White', 'On Call')")

    # Insert airport sample data
    cursor.execute("INSERT INTO Airport VALUES ('JFK', 'New York', 'USA', 'KJFK')")
    cursor.execute("INSERT INTO Airport VALUES ('LAX', 'Los Angeles', 'USA', 'KLAX')")
    cursor.execute("INSERT INTO Airport VALUES ('ORD', 'Chicago', 'USA', 'KORD')")
    cursor.execute("INSERT INTO Airport VALUES ('MIA', 'Miami', 'USA', 'KMIA')")
    cursor.execute("INSERT INTO Airport VALUES ('DFW', 'Dallas', 'USA', 'KDFW')")
    cursor.execute("INSERT INTO Airport VALUES ('ATL', 'Atlanta', 'USA', 'KATL')")
    cursor.execute("INSERT INTO Airport VALUES ('SFO', 'San Francisco', 'USA', 'KSFO')")
    cursor.execute("INSERT INTO Airport VALUES ('SEA', 'Seattle', 'USA', 'KSEA')")
    cursor.execute("INSERT INTO Airport VALUES ('BOS', 'Boston', 'USA', 'KBOS')")
    cursor.execute("INSERT INTO Airport VALUES ('DEN', 'Denver', 'USA', 'KDEN')")

    # Insert flight routes (legs) sample data
    cursor.execute("INSERT INTO FlightRoute VALUES (1, 'JFK', 'LAX', 'AA101')")
    cursor.execute("INSERT INTO FlightRoute VALUES (2, 'ORD', 'MIA', 'UA202')")
    cursor.execute("INSERT INTO FlightRoute VALUES (3, 'DFW', 'SFO', 'DL303')")
    cursor.execute("INSERT INTO FlightRoute VALUES (4, 'ATL', 'SEA', 'SW404')")
    cursor.execute("INSERT INTO FlightRoute VALUES (5, 'LAX', 'ORD', 'AA505')")
    cursor.execute("INSERT INTO FlightRoute VALUES (6, 'SFO', 'JFK', 'DL606')")
    cursor.execute("INSERT INTO FlightRoute VALUES (7, 'SEA', 'DFW', 'UA707')")
    cursor.execute("INSERT INTO FlightRoute VALUES (8, 'MIA', 'ATL', 'SW808')")
    cursor.execute("INSERT INTO FlightRoute VALUES (9, 'BOS', 'DEN', 'AA909')")
    cursor.execute("INSERT INTO FlightRoute VALUES (10, 'DEN', 'JFK', 'UA1010')")

    # Insert flight schedules sample data
    cursor.execute("INSERT INTO FlightSchedule VALUES (1, 5, '08:30', '2025-01-15', 'Scheduled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (2, 3, '10:15', '2025-02-20', 'Delayed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (3, 7, '12:00', '2025-03-10', 'Cancelled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (4, 10, '14:45', '2025-04-25', 'Completed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (5, 2, '16:20', '2025-05-18', 'On Route')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (6, 8, '18:35', '2025-06-12', 'Scheduled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (7, 4, '20:10', '2025-07-07', 'Scheduled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (8, 6, '22:25', '2025-08-29', 'Delayed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (9, 9, '06:00', '2025-09-03', 'Cancelled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (10, 1, '07:45', '2025-10-11', 'Completed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (11, 10, '09:30', '2025-11-05', 'On Route')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (12, 5, '11:15', '2025-12-21', 'Scheduled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (13, 3, '13:00', '2025-07-15', 'Delayed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (14, 7, '15:45', '2025-03-28', 'Completed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (15, 2, '17:20', '2025-10-09', 'On Route')")

    # Insert pilot schedule data
    cursor.execute("INSERT INTO PilotSchedule VALUES (3, 1, 'Captain')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (7, 2, 'Senior First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (2, 3, 'First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (9, 4, 'Second Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (5, 5, 'Captain')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (6, 6, 'Senior First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (10, 7, 'First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (8, 8, 'Second Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (1, 9, 'Captain')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (4, 10, 'Senior First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (5, 11, 'First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (3, 12, 'Second Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (2, 13, 'Captain')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (7, 14, 'Senior First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (9, 15, 'First Officer')")

    cursor.execute('''PRAGMA foreign_keys = ON''')

