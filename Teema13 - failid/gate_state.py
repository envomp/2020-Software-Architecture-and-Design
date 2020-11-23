class GateState:
    def insert_coin(self, gate):
        pass

    def pass_gate(self, gate):
        pass


class OpenedGateState(GateState):
    def insert_coin(self, gate):
        gate.thank()

    def pass_gate(self, gate):
        gate.close()
        gate.set_closed()


class ClosedGateState(GateState):
    def insert_coin(self, gate):
        gate.open()
        gate.set_open()

    def pass_gate(self, gate):
        gate.alarm()
