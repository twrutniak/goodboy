def _0x10(CPU):
    CPU.mnemonic = "STOP"
    CPU.IME = 0
    CPU.cycles = 4
    CPU.pc += 1
    # halts LCD and CPU, yet to be implemented