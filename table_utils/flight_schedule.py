class FlightSchedule:

    def __init__(self):
        self.schedule_id = 0
        self.flight_id = 0
        self.departure_time = ''
        self.departure_date = ''
        self.status = ''

    # Set methods
    def set_schedule_id(self, schedule_id):
        self.schedule_id = schedule_id

    def set_flight_id(self, flight_id):
        self.flight_id = flight_id

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def set_departure_date(self, departure_date):
        self.departure_date = departure_date

    def set_status(self, status):
        self.status = status

    # Get methods
    def get_flight_id(self):
        return self.flight_id

    def get_departure_time(self):
        return self.departure_time

    def get_departure_date(self):
        return self.departure_date

    def get_status(self):
        return self.status

    def __str__(self):
        return (str(self.schedule_id) + "\n" +str(self.flight_id) + "\n" + self.departure_time + "\n" +
                self.departure_date + "\n" + self.status)
