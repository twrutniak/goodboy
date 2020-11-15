from .misc import check_carry, check_halfcarry

def _0xCE(CPU):
    val = CPU.memory[CPU.pc + 1]
    num, cflag = check_carry(CPU.registers["A"], (val + CPU.flags["C"]), "8")
    hcflag = check_halfcarry(CPU.registers["A"], (val + CPU.flags["C"]), "8")
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
    CPU.write_log("ADC A,u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2