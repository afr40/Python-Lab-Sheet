class FlightInfo:

    def __init__(self):
        self.flight_id = 0
        self.flight_origin = ''
        self.flight_destination = ''
        self.pilot_id = 0
        self.status = ''
        self.schedule_time = ''
        self.departure_date = ''

    # Set methods
    def set_flight_id(self, flight_id):
        self.flight_id = flight_id

    def set_flight_origin(self, flight_origin):
        self.flight_origin = flight_origin

    def set_flight_destination(self, flight_destination):
        self.flight_destination = flight_destination

    def set_pilot_id(self, pilot_id):
        self.pilot_id = pilot_id

    def set_status(self, status):
        self.status = status

    def set_schedule_time(self, schedule_time):
        self.schedule_time = schedule_time

    def set_departure_date(self, departure_date):
        self.departure_date = departure_date

    # Get methods
    def get_flight_id(self):
        return self.flight_id

    def get_flight_origin(self):
        return self.flight_origin

    def get_flight_destination(self):
        return self.flight_destination

    def get_status(self):
        return self.status

    def get_pilot_id(self):
        return self.pilot_id

    def get_schedule_time(self):
        return self.schedule_time

    def get_departure_date(self):
        return self.departure_date

    def __str__(self):
        return str(
            self.flight_id
        ) + "\n" + self.flight_origin + "\n" + self.flight_destination + "\n" + str(self.pilot_id) + "\n" + str(
            self.status) + "\n" + str(self.schedule_time) + "\n" + str(self.departure_date)
