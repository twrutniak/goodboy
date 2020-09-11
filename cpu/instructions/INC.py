from .misc import *

def _0x03(CPU):
    CPU.pc += 1
    msb = CPU.registers["B"]
    lsb = CPU.registers["C"]

    val = (msb << 8) | lsb
    val += 1

    CPU.registers["B"] = val >> 8
    CPU.registers["C"] = val & 0xff

    CPU.mnemonic = "INC BC"

def _0x13(CPU):
    CPU.pc += 1
    msb = CPU.registers["D"]
    lsb = CPU.registers["E"]

    val = (msb << 8) | lsb
    val += 1

    CPU.registers["D"] = val >> 8
    CPU.registers["E"] = val & 0xff

    CPU.mnemonic = "INC DE"

def _0x23(CPU):
    CPU.pc += 1
    msb = CPU.registers["H"]
    lsb = CPU.registers["L"]

    val = (msb << 8) | lsb
    val += 1

    CPU.registers["H"] = val >> 8
    CPU.registers["L"] = val & 0xff

    CPU.mnemonic = "INC HL"

def _0x33(CPU):
    CPU.pc += 1
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()

    val = (msb << 8) | lsb
    val += 1

    CPU.stack.append(val & 0xff)
    CPU.stack.append(val >> 8)

    CPU.mnemonic = "INC SP"

def _0x04(CPU):
    CPU.pc += 1
    hcflag = check_halfcarry(CPU.registers["B"], 1, "8")
    CPU.registers["B"] += 1

    CPU.flags["HC"] = hcflag
    if CPU.registers["B"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 0
    CPU.mnemonic = "INC B"
    CPU.cycles = 4

def _0x14(CPU):
    CPU.pc += 1
    hcflag = check_halfcarry(CPU.registers["D"], 1, "8")
    CPU.registers["D"] += 1

    CPU.flags["HC"] = hcflag
    if CPU.registers["D"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 0
    CPU.mnemonic = "INC D"
    CPU.cycles = 4

def _0x24(CPU):
    CPU.pc += 1
    hcflag = check_halfcarry(CPU.registers["H"], 1, "8")
    CPU.registers["H"] += 1

    CPU.flags["HC"] = hcflag
    if CPU.registers["H"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 0
    CPU.mnemonic = "INC H"
    CPU.cycles = 4


def _0x34(CPU):
    CPU.pc += 1
    msb = CPU.registers["H"]
    lsb = CPU.registers["L"]
    addr = (msb << 8) | lsb

    hcflag = check_halfcarry(CPU.memory[addr], 1, "8")
    CPU.memory[addr] += 1
    CPU.flags["HC"] = hcflag
    if (CPU.memory[addr] + 1) == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 0
    CPU.mnemonic = "INC (HL)"
    CPU.cycles = 12
