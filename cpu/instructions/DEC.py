from .misc import check_halfcarry

def _0x0D(CPU):
    hcflag = check_halfcarry(CPU.registers["C"], 1, '8')
    CPU.flags["HC"] = hcflag
    CPU.registers["C"] -= 1
    if CPU.registers["C"] < 0x00:
        CPU.registers["C"] = 0xFF
    if CPU.registers["C"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.write_log("DEC C " + format(CPU.registers["C"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0x05(CPU):
    hcflag = check_halfcarry(CPU.registers["B"], 1, '8')
    CPU.flags["HC"] = hcflag
    CPU.registers["B"] -= 1
    if CPU.registers["B"] < 0x00:
        CPU.registers["B"] = 0xFF
    if CPU.registers["B"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 1
    CPU.write_log("DEC B " + format(CPU.registers["B"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1