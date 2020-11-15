from .misc import check_carry, check_halfcarry

def _0xC6(CPU):
    val = CPU.memory[CPU.pc + 1]
    num, cflag = check_carry(CPU.registers["A"], val, "8")
    hcflag = check_halfcarry(CPU.registers["A"], val, "8")
    CPU.registers["A"] = num
    if CPU.registers["A"] == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = hcflag
    CPU.flags["C"] = cflag
    if CPU.registers["A"] > 255:
        CPU.registers["A"] -= 256
    CPU.write_log("ADD A,u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2


# HC flag looking kinda sus
def _0x29(CPU):
    val = (CPU.registers["H"] << 8) | CPU.registers["L"]
    num, cflag = check_carry(val, val, "16")
    hcflag = check_halfcarry(val, val, "16")
    if num > 0xFFFF:
        num = num - 0x10000
    if num == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.flags["N"] = 0
    CPU.flags["HC"] = hcflag
    CPU.flags["C"] = cflag
    CPU.registers["H"] = num >> 8
    CPU.registers["L"] = num & 0xFF
    CPU.write_log("ADD HL,HL " + format(num, 'x'))
    CPU.cycles = 8
    CPU.pc += 1