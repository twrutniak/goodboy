def _0x90(CPU):
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
    CPU.pc += 1

def _0x91(CPU):
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
    CPU.pc += 1

def _0x92(CPU):
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
    CPU.pc += 1

    def _0x93(CPU):
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
    CPU.pc += 1
