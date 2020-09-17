def _0xC5(CPU):
    CPU.pc += 1
    CPU.stack.append(CPU.registers["C"])
    CPU.stack.append(CPU.registers["B"])
    CPU.mnemonic = "PUSH BC"
    CPU.cycles = 16

def _0xD5(CPU):
    CPU.pc += 1
    CPU.stack.append(CPU.registers["E"])
    CPU.stack.append(CPU.registers["D"])
    CPU.mnemonic = "PUSH DE"
    CPU.cycles = 16

def _0xE5(CPU):
    CPU.pc += 1
    CPU.stack.append(CPU.registers["L"])
    CPU.stack.append(CPU.registers["H"])
    CPU.mnemonic = "PUSH HL"
    CPU.cycles = 16

def _0xF5(CPU):
    CPU.pc += 1
    CPU.stack.append(CPU.registers["F"])
    CPU.stack.append(CPU.registers["A"])
    CPU.mnemonic = "PUSH AF"
    CPU.cycles = 16
    