from .misc import *

# needs some tweaking with HC flag
def _0x05(CPU):
    CPU.pc += 1
    val = CPU.registers["B"]
    hcflag = check_halfcarry(val, 1, "8")
    CPU.registers["B"] -= 1
    if CPU.registers["B"] == 0:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1
    CPU.flags["HC"] = hcflag
    CPU.mnemonic = "DEC B"
    CPU.cycles = 4

def _0x15(CPU):
    CPU.pc += 1
    val = CPU.registers["D"]
    hcflag = check_halfcarry(val, 1, "8")
    CPU.registers["D"] -= 1
    if CPU.registers["D"] == 0:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1
    CPU.flags["HC"] = hcflag
    CPU.mnemonic = "DEC D"
    CPU.cycles = 4

def _0x25(CPU):
    CPU.pc += 1
    val = CPU.registers["H"]
    hcflag = check_halfcarry(val, 1, "8")
    CPU.registers["H"] -= 1
    if CPU.registers["H"] == 0:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1
    CPU.flags["HC"] = hcflag
    CPU.mnemonic = "DEC H"
    CPU.cycles = 4

def _0x35(CPU):
    CPU.pc += 1
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    hcflag = check_halfcarry(CPU.memory[addr], 1, "8")
    CPU.memory[addr] -= 1
    if CPU.memory[addr] == 0:
        CPU.flags["Z"] = 0
    CPU.flags["S"] = 1
    CPU.flags["HC"] = hcflag
    CPU.mnemonic = "DEC (HL)"
    CPU.cycles = 12

def _0x0B(CPU):
    CPU.pc += 1
    val = (CPU.registers["B"] << 8) | CPU.registers["C"]
    val -= 1
    CPU.registers["B"] = (val & 0xff00) >> 8
    CPU.registers["C"] = val & 0xff
    CPU.mnemonic = "DEC BC"
    CPU.cycles = 8

def _0x1B(CPU):
    CPU.pc += 1
    val = (CPU.registers["D"] << 8) | CPU.registers["E"]
    val -= 1
    CPU.registers["D"] = (val & 0xff00) >> 8
    CPU.registers["E"] = val & 0xff
    CPU.mnemonic = "DEC DE"
    CPU.cycles = 8

def _0x2B(CPU):
    CPU.pc += 1
    val = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val -= 1
    CPU.registers["H"] = (val & 0xff00) >> 8
    CPU.registers["L"] = val & 0xff
    CPU.mnemonic = "DEC HL"
    CPU.cycles = 8

def _0x3B(CPU):
    CPU.pc += 1
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()
    val = (msb << 8) | lsb
    val -= 1
    CPU.stack.append((val & 0xff00) >> 8)
    CPU.stack.append(val & 0xff)
    CPU.mnemonic = "DEC SP"
    CPU.cycles = 8