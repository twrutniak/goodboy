def _0xF3(CPU):
    CPU.pc += 1
    CPU.mnemonic = "STOP"
    CPU.IME = 0
    CPU.cycles = 4
    # halts LCD and CPU, yet to be implemented