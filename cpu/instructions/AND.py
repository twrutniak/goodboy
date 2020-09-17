def _0xA0(CPU):
    CPU.pc += 1
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
    

def _0xA1(CPU):
    CPU.pc += 1
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

def _0xA2(CPU):
    CPU.pc += 1
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

def _0xA3(CPU):
    CPU.pc += 1
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

def _0xA4(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["H"]
    val = val1 & val2

    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 1
    CPU.flags["S"] = 0
    CPU.flags["C"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "AND A,H"
    CPU.cycles = 4

def _0xA5(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["L"]
    val = val1 & val2

    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 1
    CPU.flags["S"] = 0
    CPU.flags["C"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "AND A,L"
    CPU.cycles = 4

def _0xA6(CPU):
    CPU.pc += 1
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val1 = CPU.registers["A"]
    val2 = CPU.memory[addr]
    val = val1 & val2

    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 1
    CPU.flags["S"] = 0
    CPU.flags["C"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "AND A,(HL)"
    CPU.cycles = 8

def _0xE6(CPU):
    val1 = CPU.registers["A"]
    val2 = CPU.memory[CPU.pc + 1]    
    CPU.pc += 2
    val = val1 & val2

    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 1
    CPU.flags["S"] = 0
    CPU.flags["C"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "AND A, u8"
    CPU.cycles = 8

def _0xA7(CPU):
    CPU.pc += 1
    val = CPU.registers["A"] & CPU.registers["A"]

    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 1
    CPU.flags["S"] = 0
    CPU.flags["C"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "AND A,A"
    CPU.cycles = 4