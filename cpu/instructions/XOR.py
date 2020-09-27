def _0xA8(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["B"]
    CPU.registers["A"] = val1 ^ val2
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.mnemonic = "XOR A,B"
    CPU.cycles = 4

def _0xA9(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["C"]
    CPU.registers["A"] = val1 ^ val2
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.mnemonic = "XOR A,C"
    CPU.cycles = 4

def _0xAA(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["D"]
    CPU.registers["A"] = val1 ^ val2
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.mnemonic = "XOR A,D"
    CPU.cycles = 4

def _0xAB(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["E"]
    CPU.registers["A"] = val1 ^ val2
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.mnemonic = "XOR A,E"
    CPU.cycles = 4