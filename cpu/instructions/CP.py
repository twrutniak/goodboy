from .misc import check_carry, check_halfcarry

def _0xFE(CPU):
    val = CPU.memory[CPU.pc + 1]
    if CPU.registers["A"] < val:
        CPU.flags["C"] = 1
    else:
        CPU.flags["C"] = 0
    if (CPU.registers["A"] & 0xF) < (val & 0xF):
        CPU.registers["HC"] = 1
    else:
        CPU.flags["HC"] = 0
    if (CPU.registers["A"] - val) == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.write_log("CP A, u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2