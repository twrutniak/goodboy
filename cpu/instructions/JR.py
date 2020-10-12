from .misc import convert_signed

def _0x20(CPU):
    val = CPU.memory[CPU.pc + 1]
    if CPU.flags["Z"] == 0:
        val = convert_signed(val)
        CPU.pc = CPU.pc + val
        CPU.cycles = 12
    else:
        CPU.pc += 2
        CPU.cycles = 8
    CPU.mnemonic = "JR NZ i8"
    return

def _0x30(CPU):
    val = CPU.memory[CPU.pc + 1]
    if CPU.flags["C"] == 0:
        val = convert_signed(val)
        CPU.pc = CPU.pc + val
        CPU.cycles = 12
    else:
        CPU.pc += 2
        CPU.cycles = 8
    CPU.mnemonic = "JR NC i8"
    return

def _0x18(CPU):
    val = CPU.memory[CPU.pc + 1]
    val = convert_signed(val)
    CPU.pc = CPU.pc + val
    CPU.mnemonic = "JR i8"
    CPU.cycles = 12

def _0x28(CPU):
    val = CPU.memory[CPU.pc + 1]
    if CPU.flags["Z"] == 1:
        val = convert_signed(val)
        CPU.pc = CPU.pc + val
        CPU.cycles = 12
    else:
        CPU.pc += 2
        CPU.cycles = 8
    CPU.mnemonic = "JR Z i8"
    return

def _0x38(CPU):
    val = CPU.memory[CPU.pc + 1]
    if CPU.flags["C"] == 1:
        val = convert_signed(val)
        CPU.pc = CPU.pc + val
        CPU.cycles = 12
    else:
        CPU.pc += 2
        CPU.cycles = 8
    CPU.mnemonic = "JR C i8"
    return