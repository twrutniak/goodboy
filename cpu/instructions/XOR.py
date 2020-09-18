def _0xA8(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["B"]
    CPU.registers["A"] = val1 ^ val2
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.flags["C"] = 0
    CPU.mnemonic = "XOR A,B"
    CPU.cycles = 4