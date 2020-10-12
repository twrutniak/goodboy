from .misc import flip_bits

def _0x2F(CPU):
    CPU.pc += 1
    CPU.registers['A'] = flip_bits(CPU.registers['A'])
    CPU.mnemonic = "CPL"
    CPU.cycles = 4