def __0xC3(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    val = (msb << 8) | lsb
    CPU.write_log("JP u16 " + format(val, "x"))
    CPU.cycles = 16
    CPU.pc = val

def __0xE9(CPU):
    val = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.write_log("JP HL " + format(val, "x"))
    CPU.cycles = 4
    CPU.pc = val

def _0xC2(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    addr = (msb << 8) | lsb
    if CPU.flags["Z"] == 0:
        CPU.write_log("JP NZ,u16 " + format(addr, "x"))
        CPU.cycles = 16
        CPU.pc = addr
    else:
        CPU.write_log("JP NZ,u16 " + format(addr, "x"))
        CPU.pc += 3
        CPU.cycles = 12