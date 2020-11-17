def _0x37(CPU):
    CPU.registers["A"] = ((CPU.registers["A"] & 0xF0) >> 4) | ((CPU.registers["A"] & 0x0F) << 4)
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.write_log("SWAP A")
    CPU.cycles = 8
    CPU.pc += 2