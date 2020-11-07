def _0xE6(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.registers["A"] = CPU.registers["A"] & val
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 1
    CPU.flags["C"] = 0
    CPU.write_log("AND A, u8" + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2