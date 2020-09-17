def _0x90(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["B"]
    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1
    CPU.registers["A"] = val
    CPU.mnemonic = "SUB A,B"
    CPU.cycles = 4

def _0x91(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["C"]

    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 1
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "SUB A,C"
    CPU.cycles = 4

def _0x92(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["D"]

    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 1
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "SUB A,D"
    CPU.cycles = 4

    def _0x93(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["E"]

    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 1
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "SUB A,E"
    CPU.cycles = 4

def _0x94(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["H"]
    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.registers["A"] = val

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1

    CPU.mnemonic = "SUB A,H"
    CPU.cycles = 4

def _0x95(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["L"]
    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.registers["A"] = val

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1

    CPU.mnemonic = "SUB A,L"
    CPU.cycles = 4

def _0x96(CPU):
    CPU.pc += 1
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    
    val, cflag = check_carry(CPU.registers["A"], CPU.memory[addr], "8")
    hcflag = check_halfcarry(CPU.registers["A"], CPU.memory[addr], "8")

    CPU.registers["A"] = val

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1
    CPU.mnemonic = "ADD A,(HL)"
    CPU.cycles = 8

def _0xD6(CPU):
    val1 = CPU.memory[CPU.pc + 1]
    val2 = CPU.registers["A"]
    CPU.pc += 2
    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.registers["A"] = val

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1
    CPU.mnemonic = "SUB A, u8"
    CPU.cycles = 8

def _0x97(CPU):
    CPU.pc += 1
    val, cflag = check_carry(CPU.registers["A"], CPU.registers["A"], "8")
    hcflag = check_halfcarry(CPU.registers["A"], CPU.registers["A"], "8")

    CPU.registers["A"] = val

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1

    CPU.mnemonic = "SUB A,A"
    CPU.cycles = 4