def _0xC9(CPU):
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()
    addr = (msb << 8) | lsb
    CPU.write_log("RET " + format(addr, 'x'))
    CPU.pc = addr
    CPU.cycles = 16
