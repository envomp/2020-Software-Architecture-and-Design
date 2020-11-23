from gate_state import OpenedGateState, ClosedGateState


class Gate:
    def __init__(self):
        self.state = ClosedGateState()
        self.reportees = []

    def insert_coin(self):
        self.state.insert_coin(self)

    def pass_gate(self):
        self.state.pass_gate(self)

    def close(self):
        print("Värav läks kinni")

    def open(self):
        print("Värav avanes")

    def thank(self):
        print("Värav tänab")

    def alarm(self):
        print("Värava alarm läks tööle")
        self.notify_reportees()

    def set_open(self):
        self.state = OpenedGateState()

    def set_closed(self):
        self.state = ClosedGateState()

    def add_reportee(self, reportee):
        self.reportees.append(reportee)

    def remove_reportee(self, reportee):
        self.reportees.remove(reportee)

    def notify_reportees(self):
        for reportee in self.reportees:
            reportee.notify()
