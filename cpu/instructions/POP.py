def _0xC1(CPU):
    CPU.pc += 1
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()

    CPU.registers["C"] = lsb
    CPU.registers["B"] = msb

    CPU.mnemonic = "POP BC {}{}".format(str(hex(msb)), str(hex(lsb)))
    CPU.cycles = 12

def _0xD1(CPU):
    CPU.pc += 1
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()

    CPU.registers["E"] = lsb
    CPU.registers["D"] = msb

    CPU.mnemonic = "POP DE {}{}".format(str(hex(msb)), str(hex(lsb)))
    CPU.cycles = 12

def _0xE1(CPU):
    CPU.pc += 1
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()

    CPU.registers["L"] = lsb
    CPU.registers["H"] = msb

    CPU.mnemonic = "POP HL {}{}".format(str(hex(msb)), str(hex(lsb)))
    CPU.cycles = 12

def _0xF1(CPU):
    CPU.pc += 1
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()

    CPU.registers["F"] = lsb
    CPU.registers["A"] = msb

    flags = (msb >> 4)
    CPU.flags["Z"] = (flags & 0x8) >> 3
    CPU.flags["S"] = (flags & 0x4) >> 2
    CPU.flags["HC"] = (flags & 0x2) >> 1 
    CPU.flags["C"] = flags & 0x1

    CPU.mnemonic = "POP AF {}{}".format(str(hex(msb)), str(hex(lsb)))
    CPU.cycles = 12