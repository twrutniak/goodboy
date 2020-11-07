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
    CPU.write_log("ADD A,u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2