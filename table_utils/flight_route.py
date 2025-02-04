class FlightRoute:

    def __init__(self):
        self.flight_id = 0
        self.flight_origin = ''
        self.flight_destination = ''
        self.flight_number = ''

    # Set methods
    def set_flight_a_id(self, flight_id):
        self.flight_id = flight_id

    def set_flight_b_origin(self, flight_origin):
        self.flight_origin = flight_origin

    def set_flight_c_destination(self, flight_destination):
        self.flight_destination = flight_destination

    def set_flight_d_number(self, flight_number):
        self.flight_number = flight_number

    # Get methods
    def get_flight_id(self):
        return self.flight_id

    def get_flight_origin(self):
        return self.flight_origin

    def get_flight_destination(self):
        return self.flight_destination

    def get_flight_number(self):
        return self.flight_number

    def __str__(self):
        return str(self.flight_id) + "\n" + self.flight_origin + "\n" + self.flight_destination + "\n" + self.flight_number