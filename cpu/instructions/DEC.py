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
