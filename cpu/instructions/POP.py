def _0xE1(CPU):
    #msb = CPU.stack.pop()
    #lsb = CPU.stack.pop()
    msb = CPU.pop_stack()
    lsb = CPU.pop_stack()
    CPU.registers["H"] = msb
    CPU.registers["L"] = lsb
    CPU.write_log("POP HL")
    CPU.cycles = 12
    CPU.pc += 1

def _0xF1(CPU):
    #msb = CPU.stack.pop()
    #lsb = CPU.stack.pop()
    msb = CPU.pop_stack()
    lsb = CPU.pop_stack()
    CPU.registers["A"] = msb
    CPU.flags["Z"] = (lsb >> 7) & 0x1
    CPU.flags["N"] = (lsb >> 6) & 0x1
    CPU.flags["HC"] = (lsb >> 5) & 0x1
    CPU.flags["C"] = (lsb >> 4) & 0x1
    CPU.write_log("POP AF " + format(lsb, 'x'))
    CPU.cycles = 12
    CPU.pc += 1

def _0xC1(CPU):
    #msb = CPU.stack.pop()
    #lsb = CPU.stack.pop()
    msb = CPU.pop_stack()
    lsb = CPU.pop_stack()
    CPU.registers["B"] = msb
    CPU.registers["C"] = lsb
    CPU.write_log("POP BC")
    CPU.cycles = 12
    CPU.pc += 1

def _0xD1(CPU):
    #msb = CPU.stack.pop()
    #lsb = CPU.stack.pop()
    msb = CPU.pop_stack()
    lsb = CPU.pop_stack()
    CPU.registers["D"] = msb
    CPU.registers["E"] = lsb
    CPU.write_log("POP DE")
    CPU.cycles = 12
    CPU.pc += 1