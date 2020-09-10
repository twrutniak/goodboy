def _0xC2(CPU):
    if CPU.flags["Z"] == 0:
        CPU.cycles = 16
        msb = CPU.memory[CPU.pc + 2]
        lsb = CPU.memory[CPU + 1]
        CPU.pc = (msb << 8) | lsb
    else:
        CPU.cycles = 12
    CPU.pc += 3
    CPU.mnemonic = "JP NZ, u16"

def _0xD2(CPU):
    if CPU.flags["C"] == 0:
        CPU.cycles = 16
        msb = CPU.memory[CPU.pc + 2]
        lsb = CPU.memory[CPU + 1]
        CPU.pc = (msb << 8) | lsb
    else:
        CPU.cycles = 12
    CPU.pc += 3
    CPU.mnemonic = "JP NC, u16"

def _0xC3(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    CPU.pc = (msb << 8) | lsb

    CPU.mnemonic = "JP u16"
    CPU.cycles = 16
    CPU.pc += 3