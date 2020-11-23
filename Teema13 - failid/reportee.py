class Reportee:
    def notify(self):
        print("Vaatleja sai alarmist teada")


class Police(Reportee):
    def notify(self):
        print("Politsei sai alarmist teada")


class G4S(Reportee):
    def notify(self):
        print("G4S sai alarmist teada")
