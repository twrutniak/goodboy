from .misc import *

def _0xB8(CPU):
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
    CPU.mnemonic = "CP A,B"
    CPU.cycles = 4

def _0xB9(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["C"]
    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1
    CPU.mnemonic = "CP A,C"
    CPU.cycles = 4

def _0xBA(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["D"]
    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1
    CPU.mnemonic = "CP A,D"
    CPU.cycles = 4