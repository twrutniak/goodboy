def __0xC3(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    val = (msb << 8) | lsb
    CPU.write_log("JP u16 " + format(val, "x"))
    CPU.cycles = 16
    CPU.pc = val

