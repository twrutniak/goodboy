def _0x37(CPU):
    CPU.pc += 1
    CPU.flags["C"] = 1
    CPU.flags["S"] = 0
    CPU.flags["HC"] = 0
    CPU.mnemonic = "SCF"
    CPU.cycles = 4