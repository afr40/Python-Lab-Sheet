import pandas as pd


def drop_tables(cursor):
    query = "DROP TABLE IF EXISTS FlightInfo"
    cursor.execute(query)
    query = "DROP TABLE IF EXISTS Destination"
    cursor.execute(query)
    query = "DROP TABLE IF EXISTS Pilot"
    cursor.execute(query)


def create_tables(cursor):
    query = '''CREATE TABLE IF NOT EXISTS FlightInfo (
        FlightID INTEGER PRIMARY KEY,
        Origin TEXT NOT NULL,
        Destination TEXT NOT NULL,
        PilotID INTEGER NOT NULL,
        Status TEXT,
        Schedule_time TIME NOT NULL,
        Departure_date DATE NOT NULL,
        CHECK (Origin <> Destination), 
        CHECK (Schedule_time IS strftime('%H:%M', Schedule_time)),
        CHECK (Departure_date IS strftime('%Y-%m-%d', Departure_date)),
        FOREIGN KEY(Origin) REFERENCES Destination(DestinationID),
        FOREIGN KEY(Destination) REFERENCES Destination(DestinationID),
        FOREIGN KEY(PILOTID) REFERENCES Pilot(PilotID)
    )'''
    cursor.execute(query)

    query = '''CREATE TABLE IF NOT EXISTS Destination (
        DestinationID TEXT PRIMARY KEY,
        City TEXT NOT NULL,
        Country TEXT NOT NULL,
        AirportID TEXT NOT NULL
    )'''
    cursor.execute(query)

    query = '''CREATE TABLE IF NOT EXISTS Pilot (
        PilotID TEXT PRIMARY KEY NOT NULL,
        Name TEXT NOT NULL,
        Status TEXT,
        Schedule TEXT
    )'''
    cursor.execute(query)
    cursor.execute('''PRAGMA foreign_keys = ON''')


def insert_sample_data(cursor):
    cursor.execute('''INSERT INTO Pilot VALUES (1, 'John Smith', 'Available', '08:00 - 16:00')''')
    cursor.execute('''INSERT INTO Pilot VALUES (2, 'Emma Johnson', '', '14:00 - 22:00')''')
    cursor.execute('''INSERT INTO Pilot VALUES (3, 'Michael Brown', 'On Leave', '')''')
    cursor.execute('''INSERT INTO Pilot VALUES (4, 'Sophia Davis', 'Available', '06:00 - 14:00')''')
    cursor.execute('''INSERT INTO Pilot VALUES (5, 'Daniel Wilson', '', '12:00 - 20:00')''')
    cursor.execute('''INSERT INTO Pilot VALUES (6, 'Olivia Martinez', 'On Duty', '10:00 - 18:00')''')
    cursor.execute('''INSERT INTO Pilot VALUES (7, 'William Anderson', 'Available', '')''')

    cursor.execute('''INSERT INTO Destination VALUES ('London-LHR', 'London', 'United Kingdom', 'LHR')''')
    cursor.execute('''INSERT INTO Destination VALUES ('New York-JFK', 'New York', 'United States', 'JFK')''')
    cursor.execute('''INSERT INTO Destination VALUES ('Tokyo-HND', 'Tokyo', 'Japan', 'HND')''')
    cursor.execute('''INSERT INTO Destination VALUES ('Berlin-TXL', 'Berlin', 'Germany', 'TXL')''')
    cursor.execute('''INSERT INTO Destination VALUES ('Sydney-SYD', 'Sydney', 'Australia', 'SYD')''')
    cursor.execute('''INSERT INTO Destination VALUES ('Toronto-YYZ', 'Toronto', 'Canada', 'YYZ')''')
    cursor.execute('''INSERT INTO Destination VALUES ('Dubai-DXB', 'Dubai', 'United Arab Emirates', 'DXB')''')
    cursor.execute('''INSERT INTO Destination VALUES ('Madrid-MAD', 'Madrid', 'Spain', 'MAD')''')
    cursor.execute('''INSERT INTO Destination VALUES ('Chicago-ORD', 'Chicago', 'United States', 'ORD')''')
    cursor.execute('''INSERT INTO Destination VALUES ('Hong Kong-HKG', 'Hong Kong', 'China (SAR)', 'HKG')''')

    cursor.execute('''INSERT INTO FlightInfo VALUES (1, 'London-LHR', 'New York-JFK', 3, '', '10:30', '2025-03-12')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (2, 'New York-JFK', 'Tokyo-HND', 6, 'Delayed', '14:45', '2025-03-15')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (3, 'Tokyo-HND', 'Berlin-TXL', 4, 'On Time', '08:15', '2025-04-01')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (4, 'Berlin-TXL', 'Sydney-SYD', 7, '', '12:00', '2025-05-05')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (5, 'Sydney-SYD', 'Toronto-YYZ', 2, 'Scheduled', '09:20', '2025-06-10')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (6, 'Toronto-YYZ', 'Dubai-DXB', 5, 'On Time', '18:30', '2025-07-22')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (7, 'Dubai-DXB', 'Madrid-MAD', 4, '', '23:45', '2025-08-19')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (8, 'Madrid-MAD', 'Chicago-ORD', 6, 'Delayed', '16:10', '2025-09-25')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (9, 'Chicago-ORD', 'Hong Kong-HKG', 3, 'On Time', '13:35', '2025-10-07')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (10, 'Hong Kong-HKG', 'London-LHR', 7, 'Scheduled', '07:55', '2025-11-13')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (11, 'New York-JFK', 'Dubai-DXB', 3, '', '11:25', '2025-12-01')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (12, 'Tokyo-HND', 'Madrid-MAD', 5, 'On Time', '17:50', '2025-01-18')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (13, 'Berlin-TXL', 'Chicago-ORD', 1, 'Delayed', '06:40', '2025-02-23')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (14, 'Sydney-SYD', 'Hong Kong-HKG', 4, 'Scheduled', '15:15', '2025-03-29')''')
    cursor.execute('''INSERT INTO FlightInfo VALUES (15, 'Toronto-YYZ', 'London-LHR', 3, '', '20:05', '2025-04-30')''')


def print_tables(cursor):
    query = "SELECT * FROM FlightInfo"
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [description[0] for description in cursor.description]

    # Print the FlightInfo in table format
    df = pd.DataFrame(result, columns=columns)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 300)
    print(df)


# print_tables()
