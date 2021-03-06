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

def _0xB7(CPU):
    CPU.registers["A"] = CPU.registers["A"] | CPU.registers["A"]
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.write_log("OR A,A " + format(CPU.registers["A"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0xB0(CPU):
    CPU.registers["A"] = CPU.registers["A"] | CPU.registers["B"]
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.write_log("OR A,B " + format(CPU.registers["A"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0xB6(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.registers["A"] = CPU.registers["A"] | CPU.memory[addr]
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.write_log("OR A,(HL) " + format(CPU.registers["A"], 'x'))
    CPU.cycles = 8
    CPU.pc += 1