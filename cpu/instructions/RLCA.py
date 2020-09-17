def _0x07(CPU):
    CPU.pc += 1
    val = (CPU.registers["A"] << 1) | CPU.flags["C"]
    CPU.flags["C"] = (val & 0x100) >> 8
    if val > 0xff:
        val = val & 0xff
    CPU.flags["S"] = 0
    CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.mnemonic = "RLCA"
    CPU.cycles = 4

def _0x17(CPU):
    CPU.pc += 1
    val = (CPU.registers["A"] << 1)
    msb = (val & 0x100) >> 8
    val = (val & 0xff) | msb

    CPU.flags["S"] = 0
    CPU.flags["Z"] = 0
    CPU.flags["HC"] = 0
    CPU.mnemonic = "RLA"
    CPU.cycles = 4

