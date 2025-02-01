import sqlite3 as sql

db = sql.connect('test.db')
cursor = db.cursor()

query = "DROP TABLE IF EXISTS Flight"
cursor.execute(query)
query = "DROP TABLE IF EXISTS Destination"
cursor.execute(query)
query = "DROP TABLE IF EXISTS Pilot"
cursor.execute(query)

query = '''CREATE TABLE IF NOT EXISTS Flight (
    FlightID TEXT PRIMARY KEY,
    Origin TEXT NOT NULL,
    Destination TEXT,
    PilotID INTEGER,
    Status TEXT,
    Schedule_time TIME NOT NULL,
    Schedule_date DATE NOT NULL,
    CHECK (Origin <> Destination), 
    CHECK (Schedule_time IS strftime('%H:%M', Schedule_time)),
    CHECK (Schedule_date IS strftime('%Y-%m-%d', Schedule_date))
)'''
cursor.execute(query)

query = '''CREATE TABLE IF NOT EXISTS Destination (
    DestinationID Text PRIMARY KEY,
    City Text NOT NULL,
    Country Text NOT NULL,
    AirportID Text NOT NULL
)'''
cursor.execute(query)

query = '''CREATE TABLE IF NOT EXISTS Pilot (
    PilotID TEXT PRIMARY KEY,
    FlightID TEXT,
    Name TEXT NOT NULL,
    Status TEXT,
    FOREIGN KEY (FlightID) REFERENCES Flight (FlightID)
)'''
cursor.execute(query)

cursor.execute('''PRAGMA foreign_keys = ON''')

cursor.execute('''INSERT INTO Flight VALUES ('AV01', 'London', 'Edinburgh', '001', '', '10:30', '2025-03-12')''')
cursor.execute('''INSERT INTO Destination VALUES ('London-HR', 'London', 'UK', 'HR')''')
cursor.execute('''INSERT INTO Pilot VALUES ('001', 'AV01', 'Josh', '')''')

db.commit()

query = "SELECT * FROM ((Flight NATURAL JOIN DESTINATION) NATURAL JOIN Pilot)"
cursor.execute(query)
sampleData = cursor.fetchall()
print(sampleData)
