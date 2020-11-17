def _0x37(CPU):
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 1
    CPU.write_log("SCF")
    CPU.cycles = 4
    CPU.pc += 1