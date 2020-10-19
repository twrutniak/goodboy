def _0xE5(CPU):
    CPU.stack.append(CPU.registers["L"])
    CPU.stack.append(CPU.registers["H"])
    CPU.write_log("PUSH HL")
    CPU.cycles = 16
    CPU.pc += 1

def _0xF5(CPU):
    f = (CPU.flags["Z"] << 7) | (CPU.flags["N"] << 6) | (CPU.flags["HC"] << 5) | (CPU.flags["C"] << 4)
    CPU.stack.append(f)
    CPU.stack.append(CPU.registers["A"])
    CPU.write_log("PUSH AF")
    CPU.cycles = 16
    CPU.pc += 1

def _0xC5(CPU):
    CPU.stack.append(CPU.registers["C"])
    CPU.stack.append(CPU.registers["B"])
    CPU.write_log("PUSH BC")
    CPU.cycles = 16
    CPU.pc += 1