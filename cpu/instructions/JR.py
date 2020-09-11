def _0x20(CPU):
    val = CPU.memory[CPU.pc + 1]
    if CPU.flags["Z"] == 0:
        if val > 0x7f:
            val = val - 0xff
        CPU.pc = CPU.pc + val
        CPU.cycles = 12
    else:
        CPU.pc += 2
        CPU.cycles = 8
    self.mnemonic = "JR NZ i8"
    return

def _0x30(CPU):
    val = CPU.memory[CPU.pc + 1]
    if CPU.flags["C"] == 0:
        if val > 0x7f:
            val = val - 0xff
        CPU.pc = CPU.pc + val
        CPU.cycles = 12
    else:
        CPU.pc += 2
        CPU.cycles = 8
    self.mnemonic = "JR NZ i8"
    return