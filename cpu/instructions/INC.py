def _0x03(CPU):
    msb = CPU.registers["B"]
    lsb = CPU.registers["C"]

    val = (msb << 8) | lsb
    val += 1

    CPU.registers["B"] = val >> 8
    CPU.registers["C"] = val & 0xff

    CPU.mnemonic = "INC BC"

def _0x13(CPU):
    msb = CPU.registers["D"]
    lsb = CPU.registers["E"]

    val = (msb << 8) | lsb
    val += 1

    CPU.registers["D"] = val >> 8
    CPU.registers["E"] = val & 0xff

    CPU.mnemonic = "INC DE"

def _0x23(CPU):
    msb = CPU.registers["H"]
    lsb = CPU.registers["L"]

    val = (msb << 8) | lsb
    val += 1

    CPU.registers["H"] = val >> 8
    CPU.registers["L"] = val & 0xff

    CPU.mnemonic = "INC HL"

def _0x33(CPU):
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()

    val = (msb << 8) | lsb
    val += 1

    CPU.stack.append(val & 0xff)
    CPU.stack.append(val >> 8)

    CPU.mnemonic = "INC SP"