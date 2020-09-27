def _0xFB(CPU):
    CPU.pc += 1
    CPU.enable_interrupts = True
    CPU.mnemonic = "EI"
    CPU.cycles = 4