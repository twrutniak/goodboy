def _0x38(CPU):
    CPU.flags["C"] = CPU.registers["B"] & 1
    CPU.registers["B"] = CPU.registers["B"] >> 1
    if CPU.registers["B"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.write_log("SRL B " + format(CPU.registers["B"], 'x'))
    CPU.cycles = 8
    CPU.pc += 2