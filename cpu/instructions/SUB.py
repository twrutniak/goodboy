from .misc import check_carry, check_halfcarry

def _0xD6(CPU):
    val = CPU.memory[CPU.pc + 1]
    if CPU.registers["A"] < val:
        CPU.flags["C"] = 1
    else:
        CPU.flags["C"] = 0
    if (CPU.registers["A"] & 0xF) < (val & 0xF):
        CPU.flags["HC"] = 1
    else:
        CPU.flags["HC"] = 0
    if (CPU.registers["A"] - val) == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.registers["A"] = CPU.registers["A"] - val
    if CPU.registers["A"] < 0:
        CPU.registers["A"] = 256 - abs(CPU.registers["A"])
    CPU.write_log("SUB A, u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2