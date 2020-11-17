def _0xCD(CPU):
    addr = (CPU.memory[CPU.pc + 2] << 8) | CPU.memory[CPU.pc + 1]
    CPU.write_log("CALL u16 " + format(addr, "x"))
    CPU.pc += 3
    msb = CPU.pc >> 8
    lsb = CPU.pc & 0x00FF
    #CPU.stack.append(lsb)
    #CPU.stack.append(msb)
    CPU.push_stack(lsb)
    CPU.push_stack(msb)
    CPU.cycles = 24
    CPU.pc = addr

def _0xC4(CPU):
    addr = (CPU.memory[CPU.pc + 2] << 8) | CPU.memory[CPU.pc + 1]
    if CPU.flags["Z"] == 0:
        CPU.write_log("CALL NZ, u16 " + format(addr, "x"))
        CPU.pc += 3
        msb = CPU.pc >> 8
        lsb = CPU.pc & 0x00FF
        #CPU.stack.append(lsb)
        #CPU.stack.append(msb)
        CPU.push_stack(lsb)
        CPU.push_stack(msb)
        CPU.cycles = 24
        CPU.pc = addr
    else:
        CPU.write_log("CALL NZ, u16 " + format(addr, "x"))
        CPU.pc += 3
        CPU.cycles = 12
