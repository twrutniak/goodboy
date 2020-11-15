def _0x1F(CPU):
    CPU.registers["A"] = CPU.registers["A"] | (CPU.flags["C"] << 8)
    CPU.flags["C"] = CPU.registers["A"] & 1
    CPU.registers["A"] = CPU.registers["A"] >> 1
    CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.write_log("RRA " + format(CPU.registers["A"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1