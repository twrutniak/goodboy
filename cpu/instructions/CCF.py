def _0x3F(CPU):
    CPU.pc += 1
    CPU.flags["C"] = 0
    CPU.flags["S"] = 0
    CPU.flags["HC"] = 0
    CPU.mnemonic = "CCF"
    CPU.cycles = 4