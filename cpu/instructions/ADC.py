from .misc import *

def _0x88(CPU):
    CPU.pc += 1
    val1 = CPU.registers["A"]
    val2 = CPU.registers["B"]
    carry = CPU.flags["C"]
    val, cflag = check_carry(val1, (val2+carry), "8")
    hcflag = check_halfcarry(val1, (val2+carry), "8")

    CPU.flags["C"] = cflag
    CPU.flags["HC"] = hcflag
    CPU.flags["S"] = 0
    if val == 0:
        CPU.flags["Z"] = 1
    else:
        CPU.flags["Z"] = 0
    CPU.registers["A"] = val
    CPU.mnemonic = "ADC A,B"
    CPU.cycles = 4