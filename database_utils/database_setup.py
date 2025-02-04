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
        Status TEXT CHECK (Status IN ('Available', 'On Duty', 'On Leave', 'Sick Leave', 'On Call', '')),
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
    cursor.execute("INSERT INTO Pilot VALUES (1, 'LHR', 'John Smith', 'On Duty')")
    cursor.execute("INSERT INTO Pilot VALUES (2, 'LGW', 'Alice Johnson', 'On Duty')")
    cursor.execute("INSERT INTO Pilot VALUES (3, 'MAN', 'Michael Brown', 'On Duty')")
    cursor.execute("INSERT INTO Pilot VALUES (4, 'BHX', 'Sarah Davis', 'On Duty')")
    cursor.execute("INSERT INTO Pilot VALUES (5, 'GLA', 'David Wilson', 'On Duty')")
    cursor.execute("INSERT INTO Pilot VALUES (6, 'EDI', 'James Martinez', 'On Duty')")
    cursor.execute("INSERT INTO Pilot VALUES (7, 'BRS', 'Mary Taylor', 'Available')")
    cursor.execute("INSERT INTO Pilot VALUES (8, 'NCL', 'Robert Anderson', 'Available')")
    cursor.execute("INSERT INTO Pilot VALUES (9, 'DUB', 'Patricia Thomas', 'Sick Leave')")
    cursor.execute("INSERT INTO Pilot VALUES (10, 'CDG', 'Linda White', 'On Leave')")

    # Insert airport sample data
    cursor.execute("INSERT INTO Airport VALUES ('LHR', 'London', 'UK', 'EGLL')")
    cursor.execute("INSERT INTO Airport VALUES ('LGW', 'London', 'UK', 'EGKK')")
    cursor.execute("INSERT INTO Airport VALUES ('MAN', 'Manchester', 'UK', 'EGCC')")
    cursor.execute("INSERT INTO Airport VALUES ('BHX', 'Birmingham', 'UK', 'EGBB')")
    cursor.execute("INSERT INTO Airport VALUES ('GLA', 'Glasgow', 'UK', 'EGPF')")
    cursor.execute("INSERT INTO Airport VALUES ('EDI', 'Edinburgh', 'UK', 'EGPH')")
    cursor.execute("INSERT INTO Airport VALUES ('BRS', 'Bristol', 'UK', 'EGGD')")
    cursor.execute("INSERT INTO Airport VALUES ('NCL', 'Newcastle', 'UK', 'EGNT')")
    cursor.execute("INSERT INTO Airport VALUES ('DUB', 'Dublin', 'Ireland', 'EIDW')")
    cursor.execute("INSERT INTO Airport VALUES ('CDG', 'Paris', 'France', 'LFPG')")

    # Insert flight routes (legs) sample data
    cursor.execute("INSERT INTO FlightRoute VALUES (101, 'LHR', 'EDI', 'BA101')")
    cursor.execute("INSERT INTO FlightRoute VALUES (202, 'LGW', 'MAN', 'BA202')")
    cursor.execute("INSERT INTO FlightRoute VALUES (303, 'BHX', 'GLA', 'BA303')")
    cursor.execute("INSERT INTO FlightRoute VALUES (404, 'BRS', 'NCL', 'BA404')")
    cursor.execute("INSERT INTO FlightRoute VALUES (505, 'DUB', 'CDG', 'BA505')")
    cursor.execute("INSERT INTO FlightRoute VALUES (606, 'EDI', 'LHR', 'BA606')")
    cursor.execute("INSERT INTO FlightRoute VALUES (707, 'GLA', 'BRS', 'BA707')")
    cursor.execute("INSERT INTO FlightRoute VALUES (808, 'LGW', 'BHX', 'BA808')")
    cursor.execute("INSERT INTO FlightRoute VALUES (909, 'NCL', 'DUB', 'BA909')")
    cursor.execute("INSERT INTO FlightRoute VALUES (1010, 'CDG', 'MAN', 'BA1010')")

    # Insert flight schedules sample data
    cursor.execute("INSERT INTO FlightSchedule VALUES (1, 505, '08:30', '2025-01-15', 'Scheduled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (2, 303, '10:15', '2025-02-20', 'Delayed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (3, 707, '12:00', '2025-03-10', 'Cancelled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (4, 1010, '14:45', '2025-04-25', 'Completed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (5, 202, '16:20', '2025-05-18', 'On Route')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (6, 808, '18:35', '2025-06-12', 'Scheduled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (7, 404, '20:10', '2025-07-07', 'Scheduled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (8, 606, '22:25', '2025-08-29', 'Delayed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (9, 909, '06:00', '2025-09-03', 'Cancelled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (10, 101, '07:45', '2025-10-11', 'Completed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (11, 1010, '09:30', '2025-11-05', 'On Route')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (12, 505, '11:15', '2025-12-21', 'Scheduled')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (13, 303, '13:00', '2025-07-15', 'Delayed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (14, 707, '15:45', '2025-03-28', 'Completed')")
    cursor.execute("INSERT INTO FlightSchedule VALUES (15, 202, '17:20', '2025-10-09', 'On Route')")

    # Insert pilot schedule data
    cursor.execute("INSERT INTO PilotSchedule VALUES (1, 1, 'Captain')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (1, 4, 'Captain')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (4, 2, 'First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (3, 2, 'Captain')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (5, 3, 'Captain')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (2, 1, 'First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (2, 4, 'First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (3, 5, 'Captain')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (2, 7, 'First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (5, 6, 'Captain')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (4, 5, 'First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (6, 3, 'First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (6, 6, 'First Officer')")
    cursor.execute("INSERT INTO PilotSchedule VALUES (1, 7, 'Captain')")

    cursor.execute('''PRAGMA foreign_keys = ON''')

