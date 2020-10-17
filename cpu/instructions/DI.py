def _0xF3(CPU):
    CPU.enable_interrupts = False
    CPU.write_log("DI")
    CPU.cycles = 4
    CPU.pc += 1