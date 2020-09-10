def _0xA0(CPU):
    val1 = CPU.registers["A"]
    val2 = CPU.registers["B"]
    val = val1 & val2

    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 1
    CPU.flags["S"] = 0
    CPU.flags["C"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "AND A,B"
    CPU.cycles = 4
    CPU.pc += 1

def _0xA1(CPU):
    val1 = CPU.registers["A"]
    val2 = CPU.registers["C"]
    val = val1 & val2

    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 1
    CPU.flags["S"] = 0
    CPU.flags["C"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "AND A,C"
    CPU.cycles = 4
    CPU.pc += 1

def _0xA2(CPU):
    val1 = CPU.registers["A"]
    val2 = CPU.registers["D"]
    val = val1 & val2

    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 1
    CPU.flags["S"] = 0
    CPU.flags["C"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "AND A,D"
    CPU.cycles = 4
    CPU.pc += 1

def _0xA3(CPU):
    val1 = CPU.registers["A"]
    val2 = CPU.registers["E"]
    val = val1 & val2

    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 1
    CPU.flags["S"] = 0
    CPU.flags["C"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "AND A,E"
    CPU.cycles = 4
    CPU.pc += 1

