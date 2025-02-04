class PilotSchedule:

    def __init__(self):
        self.schedule_id = 0
        self.pilot_id = 0
        self.role = ''

    def set_schedule_id(self, schedule_id):
        self.schedule_id = schedule_id

    def set_pilot_id(self, pilot_id):
        self.pilot_id = pilot_id

    def set_role(self, role):
        self.role = role

    def get_pilot_id(self):
        return self.pilot_id

    def get_schedule_id(self):
        return self.schedule_id

    def get_role(self):
        return self.role

    def __str__(self):
        return str(self.schedule_id) + "\n" + str(self.pilot_id) + "\n" + self.role
