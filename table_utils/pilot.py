class Pilot:

    def __init__(self):
        self.pilot_id = ''
        self.name = ''
        self.status = ''
        self.schedule = ''

    def set_pilot_id(self, pilot_id):
        self.pilot_id = pilot_id

    def set_name(self, name):
        self.name = name

    def set_status(self, status):
        self.status = status

    def set_schedule(self, schedule):
        self.schedule = schedule

    def get_pilot_id(self):
        return self.pilot_id

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

    def get_schedule(self):
        return self.schedule

    def __str__(self):
        return (
                self.pilot_id + "\n" + self.name + "\n" + self.status + "\n" + self.schedule
        )
