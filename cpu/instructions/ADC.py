from .misc import check_halfcarry, check_carry

def _0x88(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["B"]
    carry = CPU.flags["C"]
    val, cflag = check_carry(val1, (val2+carry), "8")
    hcflag = check_halfcarry(val1, (val2+carry), "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADC A,B"
    CPU.cycles = 4

def _0x89(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["C"]
    carry = CPU.flags["C"]
    val, cflag = check_carry(val1, (val2+carry), "8")
    hcflag = check_halfcarry(val1, (val2+carry), "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADC A,C"
    CPU.cycles = 4

def _0x8A(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["D"]
    carry = CPU.flags["C"]
    val, cflag = check_carry(val1, (val2+carry), "8")
    hcflag = check_halfcarry(val1, (val2+carry), "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADC A,D"
    CPU.cycles = 4

def _0x8B(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["E"]
    carry = CPU.flags["C"]
    val, cflag = check_carry(val1, (val2+carry), "8")
    hcflag = check_halfcarry(val1, (val2+carry), "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADC A,E"
    CPU.cycles = 4

def _0x8C(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["H"]
    carry = CPU.flags["C"]
    val, cflag = check_carry(val1, (val2+carry), "8")
    hcflag = check_halfcarry(val1, (val2+carry), "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADC A,H"
    CPU.cycles = 4

def _0x8D(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["L"]
    carry = CPU.flags["C"]
    val, cflag = check_carry(val1, (val2+carry), "8")
    hcflag = check_halfcarry(val1, (val2+carry), "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADC A,L"
    CPU.cycles = 4

def _0x8E(CPU):
    CPU.pc += 1
    addr = (CPU.registers['H'] << 8) | CPU.registers['L']
    val1 = CPU.registers["A"]
    val2 = CPU.memory[addr]
    carry = CPU.flags["C"]
    val, cflag = check_carry(val1, (val2+carry), "8")
    hcflag = check_halfcarry(val1, (val2+carry), "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADC A,(HL)"
    CPU.cycles = 8

def _0xCE(CPU):
    val1 = CPU.registers["A"]
    val2 = CPU.memory[CPU.pc + 1]
    CPU.pc += 2
    carry = CPU.flags["C"]
    val, cflag = check_carry(val1, (val2+carry), "8")
    hcflag = check_halfcarry(val1, (val2+carry), "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADC A,u8"
    CPU.cycles = 4

def _0x8F(CPU):
    CPU.pc += 2
    val1 = CPU.registers["A"]
    val2 = CPU.registers["A"]
    carry = CPU.flags["C"]
    val, cflag = check_carry(val1, (val2+carry), "8")
    hcflag = check_halfcarry(val1, (val2+carry), "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADC A,A"
    CPU.cycles = 4