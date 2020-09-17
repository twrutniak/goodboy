def _0xC4(CPU):
    if CPU.flags["Z"] == 0:
        lsb = CPU.memory[CPU.pc + 1]
        msb = CPU.memory[CPU.pc + 2]
        opaddr = CPU.pc + 3
        CPU.stack.append(opaddr & 0xff)
        CPU.stack.append((opaddr & 0xff00) >> 8)
        CPU.pc = (msb << 8) | lsb
        CPU.cycles = 24
    else:
        CPU.pc += 3
        CPU.cycles = 12
    CPU.mnemonic = "CALL NZ,u16"


def _0xD4(CPU):
    if CPU.flags["C"] == 0:
        lsb = CPU.memory[CPU.pc + 1]
        msb = CPU.memory[CPU.pc + 2]
        opaddr = CPU.pc + 3
        CPU.stack.append(opaddr & 0xff)
        CPU.stack.append((opaddr & 0xff00) >> 8)
        CPU.pc = (msb << 8) | lsb
        CPU.cycles = 24
    else:
        CPU.pc += 3
        CPU.cycles = 12
    CPU.mnemonic = "CALL NC,u16"