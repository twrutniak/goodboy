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

def _0x85(CPU):
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
    CPU.flags["S"] = 0

    CPU.mnemonic = "ADD A,L"
    CPU.cycles = 4

def _0x86(CPU):
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
    CPU.flags["S"] = 0
    CPU.mnemonic = "ADD A,(HL)"
    CPU.cycles = 8

def _0xC6(CPU):
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
    CPU.flags["S"] = 0
    CPU.mnemonic = "ADD A, u8"
    CPU.cycles = 8

def _0x87(CPU):
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
    CPU.flags["S"] = 0

    CPU.mnemonic = "ADD A,A"
    CPU.cycles = 4

def _0xE8(CPU):
    val = convert_signed(CPU.memory[CPU.pc + 1])
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()
    addr = (msb << 8) | lsb
    hcflag = check_halfcarry(addr, val, "16")
    addr, cflag = check_carry(addr, val, "16")
    CPU.stack.append(addr & 0xff)
    CPU.stack.append((addr & 0xff00) >> 8)
    CPU.flags["Z"] = 0
    CPU.flags["S"] = 0
    CPU.flags["HC"] = hcflag
    CPU.flags["C"] = cflag
    CPU.pc += 2
    CPU.mnemonic = "ADD SP,i8"
    CPU.cycles = 16
