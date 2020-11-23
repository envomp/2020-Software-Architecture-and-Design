from gate import Gate
from reportee import Police, G4S

if __name__ == '__main__':
    gate = Gate()
    gate.add_reportee(G4S())
    gate.add_reportee(Police())
    gate.pass_gate()
    # alarm
    gate.insert_coin()
    # avaneb
    gate.insert_coin()
    # tänab
    gate.pass_gate()
    # sulgub
