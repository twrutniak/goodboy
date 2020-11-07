def _0x21(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    CPU.registers["H"] = msb
    CPU.registers["L"] = lsb
    CPU.write_log("LD HL, u16 " + format(msb, 'x') + format(lsb, 'x'))
    CPU.cycles = 12
    CPU.pc += 3

def _0x47(CPU):
    CPU.registers["B"] = CPU.registers["A"]
    CPU.write_log("LD B, A")
    CPU.cycles = 4
    CPU.pc += 1

def _0x11(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    CPU.registers["D"] = msb
    CPU.registers["E"] = lsb
    CPU.write_log("LD DE, u16 " + format(msb, 'x') + format(lsb, 'x'))
    CPU.cycles = 12
    CPU.pc += 3

def _0x0E(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.registers["C"] = val
    CPU.write_log("LD C, u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2

def _0x2A(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["A"] = val
    addr += 1
    if addr > 0xFFFF:
        addr = 0
    CPU.registers["H"] = (addr >> 8)
    CPU.registers["L"] = (addr & 0x00ff)
    CPU.write_log("LD A, (HL+) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x12(CPU):
    addr = (CPU.registers["D"] << 8) | CPU.registers['E']
    CPU.memory[addr] = CPU.registers['A']
    CPU.write_log("LD (DE), A " + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x78(CPU):
    CPU.registers["A"] = CPU.registers["B"]
    CPU.write_log("LD A, B")
    CPU.cycles = 4
    CPU.pc += 1

def _0x01(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    CPU.registers["B"] = msb
    CPU.registers["C"] = lsb
    CPU.write_log("LD BC, u16 " + format(msb, 'x') +  ' ' + format(lsb, 'x'))
    CPU.cycles = 12
    CPU.pc += 3

def _0x31(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.write_log("LD SP, u16 " + format(msb, 'x') +  ' ' + format(lsb, 'x'))
    CPU.cycles = 12
    CPU.pc += 3

def _0xEA(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    addr = (msb << 8) | lsb
    CPU.memory[addr] = CPU.registers["A"]
    CPU.write_log("LD (u16), A " + format(msb, 'x') +  ' ' + format(lsb, 'x'))
    CPU.cycles = 16
    CPU.pc += 3

def _0x3E(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.registers["A"] = val
    CPU.write_log("LD A, u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2

def _0xE0(CPU):
    val = CPU.memory[CPU.pc + 1]
    addr = 0xFF00 + val
    CPU.memory[addr] = CPU.registers["A"]
    CPU.write_log("LD (FF00+u8),A " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 12
    CPU.pc += 2

def _0x7D(CPU):
    CPU.registers["A"] = CPU.registers["L"]
    CPU.write_log("LD A, L")
    CPU.cycles = 4
    CPU.pc += 1

def _0x7C(CPU):
    CPU.registers["A"] = CPU.registers["H"]
    CPU.write_log("LD A, H")
    CPU.cycles = 4
    CPU.pc += 1

def _0xF0(CPU):
    val = CPU.memory[CPU.pc + 1]
    addr = 0xFF00 + val
    CPU.registers["A"] = CPU.memory[addr]
    CPU.write_log("LD A,(FF00+u8) " + format(CPU.memory[addr], 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 12
    CPU.pc += 2

def _0xFA(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    addr = (msb << 8) | lsb
    val = CPU.memory[addr]
    CPU.registers["A"] = val
    CPU.write_log("LD A,(u16) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 16
    CPU.pc += 3

def _0x06(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.registers["B"] = val
    CPU.write_log("LD B, u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2

def _0x77(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["A"]
    CPU.write_log("LD (HL), A " + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x1A(CPU):
    addr = (CPU.registers["D"] << 8) | CPU.registers["E"]
    val = CPU.memory[addr]
    CPU.registers["A"] = val
    CPU.write_log("LD A, (DE) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x22(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["A"]
    addr += 1
    if addr > 0xFFFF:
        addr = 0
    CPU.registers["H"] = (addr >> 8)
    CPU.registers["L"] = (addr & 0x00ff)
    CPU.write_log("LD (HL+), A " + format(CPU.registers["A"], 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x32(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["A"]
    addr -= 1
    if addr < 0:
        addr = 0xFFFF
    CPU.registers["H"] = (addr >> 8)
    CPU.registers["L"] = (addr & 0x00ff)
    CPU.write_log("LD (HL-), A " + format(CPU.registers["A"], 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x46(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["B"] = val
    CPU.write_log("LD B, (HL) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x4E(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["C"] = val
    CPU.write_log("LD C, (HL) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x56(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["D"] = val
    CPU.write_log("LD D, (HL) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1