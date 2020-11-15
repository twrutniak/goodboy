def _0xC9(CPU):
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()
    addr = (msb << 8) | lsb
    CPU.write_log("RET " + format(addr, 'x'))
    CPU.pc = addr
    CPU.cycles = 16

def _0xD0(CPU):
    if CPU.flags["C"] == 0:
        msb = CPU.stack.pop()
        lsb = CPU.stack.pop()
        addr = (msb << 8) | lsb
        CPU.write_log("RET NC " + format(addr, "x"))
        CPU.pc = addr
        CPU.cycles = 20
    else:
        CPU.write_log("RET NC")
        CPU.pc += 1
        CPU.cycles = 8

def _0xD8(CPU):
    if CPU.flags["C"] == 1:
        msb = CPU.stack.pop()
        lsb = CPU.stack.pop()
        addr = (msb << 8) | lsb
        CPU.write_log("RET C " + format(addr, "x"))
        CPU.pc = addr
        CPU.cycles = 20
    else:
        CPU.write_log("RET C")
        CPU.pc += 1
        CPU.cycles = 8

def _0xC8(CPU):
    if CPU.flags["Z"] == 1:
        msb = CPU.stack.pop()
        lsb = CPU.stack.pop()
        addr = (msb << 8) | lsb
        CPU.write_log("RET Z " + format(addr, "x"))
        CPU.pc = addr
        CPU.cycles = 20
    else:
        CPU.write_log("RET Z")
        CPU.pc += 1
        CPU.cycles = 8