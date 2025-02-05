class Pilot:
    """
    Pilot class that holds information about pilots airport base, name and status
    """

    def __init__(self):
        self.pilot_id = ''
        self.airport_base = ''
        self.name = ''
        self.status = ''

    def set_pilot_id(self, pilot_id):
        self.pilot_id = pilot_id

    def set_airport_base(self, airport_base):
        self.airport_base = airport_base

    def set_name(self, name):
        self.name = name

    def set_status(self, status):
        self.status = status

    def get_pilot_id(self):
        return self.pilot_id

    def get_airport_base(self):
        return self.airport_base

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

    def __str__(self):
        return self.pilot_id + "\n" + self.airport_base + "\n" + self.name + "\n" + self.status
