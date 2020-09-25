def _0xF3(CPU):
    CPU.pc += 1
    CPU.mnemonic = "STOP"
    CPU.enable_interrupts = False
    CPU.cycles = 4
    # halts LCD and CPU, yet to be implemented