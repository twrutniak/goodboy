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

def _0xAC(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["H"]
    CPU.registers["A"] = val1 ^ val2
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.mnemonic = "XOR A,H"
    CPU.cycles = 4

def _0xAD(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["L"]
    CPU.registers["A"] = val1 ^ val2
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.mnemonic = "XOR A,L"
    CPU.cycles = 4

def _0xAE(CPU):
    CPU.pc += 1
    addr = (CPU.registers['H'] << 8) | CPU.registers['L']
    val1 = CPU.registers["A"]
    val2 = CPU.memory[addr]
    CPU.registers["A"] = val1 ^ val2
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.mnemonic = "XOR A,(HL)"
    CPU.cycles = 8

def _0xEE(CPU):
    val1 = CPU.registers["A"]
    val2 = CPU.memory[CPU.pc + 1]
    CPU.pc += 2
    CPU.registers["A"] = val1 ^ val2
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.mnemonic = "XOR A,u8"
    CPU.cycles = 8

def _0xAF(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["A"]
    CPU.registers["A"] = val1 ^ val2
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.mnemonic = "XOR A,A"
    CPU.cycles = 4