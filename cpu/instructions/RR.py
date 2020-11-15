def _0x19(CPU):
    CPU.registers["C"] = CPU.registers["C"] | (CPU.flags["C"] << 8)
    CPU.flags["C"] = CPU.registers["C"] & 1
    CPU.registers["C"] = CPU.registers["C"] >> 1
    if CPU.registers["C"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.write_log("RR C " + format(CPU.registers["C"], 'x'))
    CPU.cycles = 8
    CPU.pc += 2

def _0x1A(CPU):
    CPU.registers["D"] = CPU.registers["D"] | (CPU.flags["C"] << 8)
    CPU.flags["C"] = CPU.registers["D"] & 1
    CPU.registers["D"] = CPU.registers["D"] >> 1
    if CPU.registers["D"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.write_log("RR D " + format(CPU.registers["D"], 'x'))
    CPU.cycles = 8
    CPU.pc += 2

def _0x1B(CPU):
    CPU.registers["E"] = CPU.registers["E"] | (CPU.flags["C"] << 8)
    CPU.flags["C"] = CPU.registers["E"] & 1
    CPU.registers["E"] = CPU.registers["E"] >> 1
    if CPU.registers["E"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.write_log("RR E " + format(CPU.registers["E"], 'x'))
    CPU.cycles = 8
    CPU.pc += 2