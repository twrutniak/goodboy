from .misc import *

def _0x80(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["B"]
    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADD A,B"
    CPU.cycles = 4

def _0x81(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["B"]

    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADD A,B"
    CPU.cycles = 4


def _0x82(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["D"]

    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADD A,D"
    CPU.cycles = 4

def _0x83(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["E"]

    val, cflag = check_carry(val1, val2, "8")
    hcflag = check_halfcarry(val1, val2, "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADD A,E"
    CPU.cycles = 4


def _0x84(CPU):
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
    CPU.flags["S"] = 0

    CPU.mnemonic = "ADD A,H"
    CPU.cycles = 4
    