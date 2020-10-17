from .misc import check_halfcarry

def _0x1C(CPU):
    hcflag = check_halfcarry(CPU.registers["E"], 1, '8')
    CPU.flags["HC"] = hcflag
    CPU.registers["E"] += 1
    if CPU.registers["E"] > 0xFF:
        CPU.registers["E"] = 0
    if CPU.registers["E"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.write_log("INC E " + format(CPU.registers["E"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0x14(CPU):
    hcflag = check_halfcarry(CPU.registers["D"], 1, '8')
    CPU.flags["HC"] = hcflag
    CPU.registers["D"] += 1
    if CPU.registers["D"] > 0xFF:
        CPU.registers["D"] = 0
    if CPU.registers["D"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.write_log("INC D " + format(CPU.registers["D"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0x04(CPU):
    hcflag = check_halfcarry(CPU.registers["B"], 1, '8')
    CPU.flags["HC"] = hcflag
    CPU.registers["B"] += 1
    if CPU.registers["B"] > 0xFF:
        CPU.registers["B"] = 0
    if CPU.registers["B"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.write_log("INC B " + format(CPU.registers["B"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1