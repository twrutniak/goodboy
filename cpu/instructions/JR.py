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

def _0x30(CPU):
    val = convert_signed(CPU.memory[CPU.pc + 1])
    if CPU.flags["C"] == 0:
        CPU.write_log("JR NC,i8 " + format((CPU.pc + 2 + val), "x"))
        CPU.cycles = 12
        CPU.pc += 2
        CPU.pc = CPU.pc + val
    else:
        CPU.write_log("JR NC,i8 " + format((CPU.pc + 2 + val), "x"))
        CPU.pc += 2
        CPU.cycles = 8

def _0x18(CPU):
    val = convert_signed(CPU.memory[CPU.pc + 1])
    CPU.write_log("JR i8 " + format((CPU.pc + 2 + val), "x"))
    CPU.cycles = 12
    CPU.pc += 2
    CPU.pc = CPU.pc + val

def _0x28(CPU):
    val = convert_signed(CPU.memory[CPU.pc + 1])
    if CPU.flags["Z"] == 1:
        CPU.write_log("JR Z,i8 " + format((CPU.pc + 2 + val), "x"))
        CPU.cycles = 12
        CPU.pc += 2
        CPU.pc = CPU.pc + val
    else:
        CPU.write_log("JR Z,i8 " + format((CPU.pc + 2 + val), "x"))
        CPU.pc += 2
        CPU.cycles = 8