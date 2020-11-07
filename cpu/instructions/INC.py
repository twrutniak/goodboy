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

def _0x23(CPU):
    val = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val += 1
    if val > 0xFFFF:
        val = 0x0000
    CPU.registers["H"] = (val >> 8)
    CPU.registers["L"] = val & 0xFF
    CPU.write_log("INC HL " + format(CPU.registers["H"], 'x') + ' ' + format(CPU.registers["L"]))
    CPU.cycles = 8
    CPU.pc += 1

def _0x03(CPU):
    val = (CPU.registers["B"] << 8) | CPU.registers["C"]
    val += 1
    if val > 0xFFFF:
        val = 0x0000
    CPU.registers["B"] = (val >> 8)
    CPU.registers["C"] = val & 0xFF
    CPU.write_log("INC BC " + format(CPU.registers["B"], 'x') + ' ' + format(CPU.registers["C"], 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x2C(CPU):
    hcflag = check_halfcarry(CPU.registers["L"], 1, '8')
    CPU.flags["HC"] = hcflag
    CPU.registers["L"] += 1
    if CPU.registers["L"] > 0xFF:
        CPU.registers["L"] = 0
    if CPU.registers["L"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.write_log("INC L " + format(CPU.registers["L"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0x24(CPU):
    hcflag = check_halfcarry(CPU.registers["H"], 1, '8')
    CPU.flags["HC"] = hcflag
    CPU.registers["H"] += 1
    if CPU.registers["H"] > 0xFF:
        CPU.registers["H"] = 0
    if CPU.registers["H"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.write_log("INC H " + format(CPU.registers["H"], 'x'))
    CPU.cycles = 4
    CPU.pc += 1

def _0x13(CPU):
    val = (CPU.registers["D"] << 8) | CPU.registers["E"]
    val += 1
    if val > 0xFFFF:
        val = 0x0000
    CPU.registers["D"] = (val >> 8)
    CPU.registers["E"] = val & 0xFF
    CPU.write_log("INC DE " + format(CPU.registers["D"], 'x') + ' ' + format(CPU.registers["E"], 'x'))
    CPU.cycles = 8
    CPU.pc += 1