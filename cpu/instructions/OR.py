def _0xB1(CPU):
    CPU.registers["A"] = CPU.registers["A"] | CPU.registers["C"]
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.write_log("OR A,C " + format(CPU.registers["A"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1