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