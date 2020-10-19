def _0xCD(CPU):
    addr = (CPU.memory[CPU.pc + 2] << 8) | CPU.memory[CPU.pc + 1]
    CPU.write_log("CALL u16 " + format(addr, "x"))
    CPU.pc += 3
    msb = CPU.pc >> 8
    lsb = CPU.pc & 0x00FF
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.cycles = 24
    CPU.pc = addr