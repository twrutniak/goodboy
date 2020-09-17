def _0x27(CPU):
    CPU.pc += 1
    if CPU.flags["N"] == 0:
        if (CPU.flags["C"] == 1) or (CPU.registers["A"] > 0x99):
            CPU.registers["A"] += 0x60
            if CPU.registers["A"] > 0xff:
                CPU.registers["A"] -= 0xff
            CPU.registers["C"] = 1
    else:
        if CPU.flags["C"] == 1:
            CPU.registers["A"] -= 0x60
            if CPU.registers["A"] < 0:
                CPU.registers["A"] += 0xff
        if CPU.flags["HC"] == 1:
            CPU.registers["A"] -= 0x6
            if CPU.registers["A"] < 0:
                CPU.registers["A"] += 0xff
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    CPU.flags["HC"] = 0
    CPU.mnemonic = "DAA"
    CPU.cycles = 4