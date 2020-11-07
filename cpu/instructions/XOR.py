def _0xA9(CPU):
    CPU.registers["A"] = CPU.registers["A"] ^ CPU.registers["C"]
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.write_log("XOR A,C " + format(CPU.registers["A"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0xAE(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["A"] = CPU.registers["A"] ^ val
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.write_log("XOR A,(HL) " + format(CPU.registers["A"], 'x'))
    CPU.cycles = 8
    CPU.pc += 1