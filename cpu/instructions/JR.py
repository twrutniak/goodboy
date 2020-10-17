from .misc import convert_signed

def _0x20(CPU):
    val = convert_signed(CPU.memory[CPU.pc + 1])
    if CPU.flags["Z"] == 0:
        CPU.write_log("JR NZ,i8 " + format((CPU.pc + 2 + val), "x"))
        CPU.cycles = 12
        CPU.pc += 2
        CPU.pc = CPU.pc + val
    else:
        CPU.write_log("JR NZ,i8 " + format((CPU.pc + 2 + val), "x"))
        CPU.pc += 2
        CPU.cycles = 8
