import sqlite3 as sql


class DatabaseSetup:

    def __init__(self):
        self.db = sql.connect('test.db')
        self.cursor = self.db.cursor()

    def drop_tables(self):
        query = "DROP TABLE IF EXISTS FlightInfo"
        self.cursor.execute(query)
        query = "DROP TABLE IF EXISTS Destination"
        self.cursor.execute(query)
        query = "DROP TABLE IF EXISTS Pilot"
        self.cursor.execute(query)

    def create_tables(self):
        query = '''CREATE TABLE IF NOT EXISTS FlightInfo (
            FlightID TEXT PRIMARY KEY,
            Origin TEXT NOT NULL,
            Destination TEXT,
            PilotID INTEGER,
            Status TEXT,
            Schedule_time TIME NOT NULL,
            Departure_date DATE NOT NULL,
            CHECK (Origin <> Destination), 
            CHECK (Schedule_time IS strftime('%H:%M', Schedule_time)),
            CHECK (Departure_date IS strftime('%Y-%m-%d', Departure_date))
        )'''
        self.cursor.execute(query)

        query = '''CREATE TABLE IF NOT EXISTS Destination (
            DestinationID Text PRIMARY KEY,
            City Text NOT NULL,
            Country Text NOT NULL,
            AirportID Text NOT NULL
        )'''
        self.cursor.execute(query)

        query = '''CREATE TABLE IF NOT EXISTS Pilot (
            PilotID TEXT PRIMARY KEY,
            FlightID TEXT,
            Name TEXT NOT NULL,
            Status TEXT,
            FOREIGN KEY (FlightID) REFERENCES FlightInfo (FlightID)
        )'''
        self.cursor.execute(query)

        self.cursor.execute('''PRAGMA foreign_keys = ON''')

    def insert_sample_data(self):
        self.cursor.execute(
            '''INSERT INTO FlightInfo VALUES ('AV01', 'London', 'Edinburgh', '001', '', '10:30', '2025-03-12')''')
        self.cursor.execute('''INSERT INTO Destination VALUES ('London-HR', 'London', 'UK', 'HR')''')
        self.cursor.execute('''INSERT INTO Pilot VALUES ('001', 'AV01', 'Josh', '')''')

    def commit_database(self):
        self.db.commit()

    def print_tables(self):
        query = "SELECT * FROM ((FlightInfo NATURAL JOIN DESTINATION) NATURAL JOIN Pilot)"
        self.cursor.execute(query)
        sample_data = self.cursor.fetchall()
        print(sample_data)

DatabaseSetup().print_tables()