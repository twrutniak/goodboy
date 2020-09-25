def _0xC2(CPU):
    if CPU.flags["Z"] == 0:
        CPU.cycles = 16
        msb = CPU.memory[CPU.pc + 2]
        lsb = CPU.memory[CPU.pc + 1]
        CPU.pc = (msb << 8) | lsb
    else:
        CPU.pc += 3
        CPU.cycles = 12
    CPU.mnemonic = "JP NZ, u16"

def _0xD2(CPU):
    if CPU.flags["C"] == 0:
        CPU.cycles = 16
        msb = CPU.memory[CPU.pc + 2]
        lsb = CPU.memory[CPU.pc + 1]
        CPU.pc = (msb << 8) | lsb
    else:
        CPU.pc += 3
        CPU.cycles = 12
    CPU.mnemonic = "JP NC, u16"

def _0xC3(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    CPU.pc = (msb << 8) | lsb

    CPU.mnemonic = "JP u16"
    CPU.cycles = 16

def _0xE9(CPU):
    CPU.pc += 1
    msb = CPU.registers['H']
    lsb = CPU.registers['L']
    val = (msb << 8) | lsb
    CPU.pc = val
    CPU.mnemonic = "JP HL"
    CPU.cycles = 4

def _0xCA(CPU):
    if CPU.flags["Z"] == 1:
        CPU.cycles = 16
        msb = CPU.memory[CPU.pc + 2]
        lsb = CPU.memory[CPU.pc + 1]
        CPU.pc = (msb << 8) | lsb
    else:
        CPU.pc += 3
        CPU.cycles = 12
    CPU.mnemonic = "JP Z, u16"

def _0xDA(CPU):
    if CPU.flags["C"] == 1:
        CPU.cycles = 16
        msb = CPU.memory[CPU.pc + 2]
        lsb = CPU.memory[CPU.pc + 1]
        CPU.pc = (msb << 8) | lsb
    else:
        CPU.pc += 3
        CPU.cycles = 12
    CPU.mnemonic = "JP C, u16" 