from .misc import *

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