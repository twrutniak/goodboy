from .misc import check_halfcarry

def _0x0D(CPU):
    if (CPU.registers["C"] & 0xF) < ((CPU.registers["C"] - 1) & 0xF):
        CPU.flags["HC"] = 1
    else:
        CPU.flags["HC"] = 0
    CPU.registers["C"] -= 1
    if CPU.registers["C"] < 0x00:
        CPU.registers["C"] = 0xFF
    if CPU.registers["C"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.write_log("DEC C " + format(CPU.registers["C"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0x05(CPU):
    if (CPU.registers["B"] & 0xF) < ((CPU.registers["B"] - 1) & 0xF):
        CPU.flags["HC"] = 1
    else:
        CPU.flags["HC"] = 0
    CPU.registers["B"] -= 1
    if CPU.registers["B"] < 0x00:
        CPU.registers["B"] = 0xFF
    if CPU.registers["B"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.write_log("DEC B " + format(CPU.registers["B"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0x2D(CPU):
    if (CPU.registers["L"] & 0xF) < ((CPU.registers["L"] - 1) & 0xF):
        CPU.flags["HC"] = 1
    else:
        CPU.flags["HC"] = 0
    CPU.registers["L"] -= 1
    if CPU.registers["L"] < 0x00:
        CPU.registers["L"] = 0xFF
    if CPU.registers["L"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.write_log("DEC L " + format(CPU.registers["B"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0x25(CPU):
    if (CPU.registers["H"] & 0xF) < ((CPU.registers["H"] - 1) & 0xF):
        CPU.flags["HC"] = 1
    else:
        CPU.flags["HC"] = 0
    CPU.registers["H"] -= 1
    if CPU.registers["H"] < 0x00:
        CPU.registers["H"] = 0xFF
    if CPU.registers["H"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.write_log("DEC H " + format(CPU.registers["H"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0x3D(CPU):
    if (CPU.registers["A"] & 0xF) < ((CPU.registers["A"] - 1) & 0xF):
        CPU.flags["HC"] = 1
    else:
        CPU.flags["HC"] = 0
    CPU.registers["A"] -= 1
    if CPU.registers["A"] < 0x00:
        CPU.registers["A"] = 0xFF
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.write_log("DEC A " + format(CPU.registers["A"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1


def _0x35(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    if (CPU.memory[addr] & 0xF) < ((CPU.memory[addr] - 1) & 0xF):
        CPU.flags["HC"] = 1
    else:
        CPU.flags["HC"] = 0
    CPU.memory[addr] -= 1
    if CPU.memory[addr] < 0x00:
        CPU.memory[addr] = 0xFF
    if CPU.memory[addr] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.write_log("DEC (HL) " + format(CPU.memory[addr], 'x'))
    CPU.cycles = 12
    CPU.pc += 1

def _0x1D(CPU):
    if (CPU.registers["E"] & 0xF) < ((CPU.registers["E"] - 1) & 0xF):
        CPU.flags["HC"] = 1
    else:
        CPU.flags["HC"] = 0
    CPU.registers["E"] -= 1
    if CPU.registers["E"] < 0x00:
        CPU.registers["E"] = 0xFF
    if CPU.registers["E"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.write_log("DEC E " + format(CPU.registers["E"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1
