class Destination:

    def __init__(self):
        self.destination_id = ''
        self.city = ''
        self.country = ''
        self.airport_id = ''

    def set_destination_id(self, destination_id):
        self.destination_id = destination_id

    def set_city(self, city):
        self.city = city

    def set_country(self, country):
        self.country = country

    def set_airport_id(self, airport_id):
        self.airport_id = airport_id

    def get_destination_id(self):
        return self.destination_id

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    def get_airport_id(self):
        return self.airport_id

    def __str__(self):
        return (
            self.destination_id + "\n" + self.city + "\n" + self.country + "\n" + self.airport_id
        )