def _0xC0(CPU):
    CPU.cycles = 8
    if CPU.flags["Z"] == 0:
        msb = CPU.stack.pop()
        lsb = CPU.stack.pop()
        CPU.pc = (msb << 8) | lsb
        CPU.cycles = 20
    else:
        CPU.pc += 1
        CPU.cycles = 8
    CPU.mnemonic = "RET NZ"

def _0xD0(CPU):
    CPU.cycles = 8
    if CPU.flags["C"] == 0:
        msb = CPU.stack.pop()
        lsb = CPU.stack.pop()
        CPU.pc = (msb << 8) | lsb
        CPU.cycles = 20
    else:
        CPU.pc += 1
        CPU.cycles = 8
    CPU.mnemonic = "RET NC"

def _0xC8(CPU):
    CPU.cycles = 8
    if CPU.flags["Z"] == 1:
        msb = CPU.stack.pop()
        lsb = CPU.stack.pop()
        CPU.pc = (msb << 8) | lsb
        CPU.cycles = 20
    else:
        CPU.pc += 1
        CPU.cycles = 8
    CPU.mnemonic = "RET Z"

def _0xD8(CPU):
    CPU.cycles = 8
    if CPU.flags["C"] == 1:
        msb = CPU.stack.pop()
        lsb = CPU.stack.pop()
        CPU.pc = (msb << 8) | lsb
        CPU.cycles = 20
    else:
        CPU.pc += 1
        CPU.cycles = 8
    CPU.mnemonic = "RET C"