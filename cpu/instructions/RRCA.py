def _0x0F(CPU):
    CPU.pc += 1
    bit = CPU.registers['A'] & 0x1
    CPU.registers['A'] = (CPU.registers['A'] >> 1) | (CPU.flags['C'] << 7)
    CPU.registers['C'] = bit
    CPU.flags["S"] = 0
    CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.mnemonic = "RRCA"
    CPU.cycles = 4

def _0x1F(CPU):
    CPU.pc += 1
    bit = CPU.registers['A'] & 0x1
    CPU.registers['A'] = (CPU.registers['A'] >> 1) | (bit << 7)

    CPU.flags["S"] = 0
    CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.mnemonic = "RRA"
    CPU.cycles = 4

