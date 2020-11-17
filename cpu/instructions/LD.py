def _0x21(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    CPU.registers["H"] = msb
    CPU.registers["L"] = lsb
    CPU.write_log("LD HL,u16 " + format(msb, 'x') + format(lsb, 'x'))
    CPU.cycles = 12
    CPU.pc += 3

def _0x47(CPU):
    CPU.registers["B"] = CPU.registers["A"]
    CPU.write_log("LD B,A")
    CPU.cycles = 4
    CPU.pc += 1

def _0x11(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    CPU.registers["D"] = msb
    CPU.registers["E"] = lsb
    CPU.write_log("LD DE,u16 " + format(msb, 'x') + format(lsb, 'x'))
    CPU.cycles = 12
    CPU.pc += 3

def _0x0E(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.registers["C"] = val
    CPU.write_log("LD C,u8 " + format(val, 'x'))
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
    CPU.write_log("LD A,(HL+) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x12(CPU):
    addr = (CPU.registers["D"] << 8) | CPU.registers['E']
    CPU.memory[addr] = CPU.registers['A']
    CPU.write_log("LD (DE),A " + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x78(CPU):
    CPU.registers["A"] = CPU.registers["B"]
    CPU.write_log("LD A,B")
    CPU.cycles = 4
    CPU.pc += 1

def _0x01(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    CPU.registers["B"] = msb
    CPU.registers["C"] = lsb
    CPU.write_log("LD BC,u16 " + format(msb, 'x') +  ' ' + format(lsb, 'x'))
    CPU.cycles = 12
    CPU.pc += 3

def _0x31(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    CPU.sp = (msb << 8) | lsb
    CPU.write_log("LD SP,u16 " + format(msb, 'x') +  ' ' + format(lsb, 'x'))
    CPU.cycles = 12
    CPU.pc += 3

def _0xEA(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    addr = (msb << 8) | lsb
    CPU.memory[addr] = CPU.registers["A"]
    CPU.write_log("LD (u16),A " + format(msb, 'x') +  ' ' + format(lsb, 'x'))
    CPU.cycles = 16
    CPU.pc += 3

def _0x3E(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.registers["A"] = val
    CPU.write_log("LD A,u8 " + format(val, 'x'))
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
    CPU.write_log("LD A,L")
    CPU.cycles = 4
    CPU.pc += 1

def _0x7C(CPU):
    CPU.registers["A"] = CPU.registers["H"]
    CPU.write_log("LD A,H")
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
    CPU.write_log("LD B,u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2

def _0x77(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["A"]
    CPU.write_log("LD (HL),A " + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x1A(CPU):
    addr = (CPU.registers["D"] << 8) | CPU.registers["E"]
    val = CPU.memory[addr]
    CPU.registers["A"] = val
    CPU.write_log("LD A,(DE) " + format(val, 'x') + ' ' + format(addr, 'x'))
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
    CPU.write_log("LD (HL+),A " + format(CPU.registers["A"], 'x') + ' ' + format(addr, 'x'))
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
    CPU.write_log("LD (HL-),A " + format(CPU.registers["A"], 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x46(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["B"] = val
    CPU.write_log("LD B,(HL) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x4E(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["C"] = val
    CPU.write_log("LD C,(HL) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x56(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["D"] = val
    CPU.write_log("LD D,(HL) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x26(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.registers["H"] = val
    CPU.write_log("LD H,u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2

def _0x5F(CPU):
    CPU.registers["E"] = CPU.registers["A"]
    CPU.write_log("LD E,A ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x79(CPU):
    CPU.registers["A"] = CPU.registers["C"]
    CPU.write_log("LD A,C ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x4F(CPU):
    CPU.registers["C"] = CPU.registers["A"]
    CPU.write_log("LD C,A ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x7A(CPU):
    CPU.registers["A"] = CPU.registers["D"]
    CPU.write_log("LD A,D ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x57(CPU):
    CPU.registers["D"] = CPU.registers["A"]
    CPU.write_log("LD D,A ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x7B(CPU):
    CPU.registers["A"] = CPU.registers["E"]
    CPU.write_log("LD A,E ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x72(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["D"]
    CPU.write_log("LD (HL),D " + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x71(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["C"]
    CPU.write_log("LD (HL),C " + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x70(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["B"]
    CPU.write_log("LD (HL),B " + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x73(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["E"]
    CPU.write_log("LD (HL),E " + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x6E(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["L"] = val
    CPU.write_log("LD L,(HL) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x7E(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["A"] = val
    CPU.write_log("LD A,(HL) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x6F(CPU):
    CPU.registers["L"] = CPU.registers["A"]
    CPU.write_log("LD L,A ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x2E(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.registers["L"] = val
    CPU.write_log("LD L,u8 " + format(val, 'x'))
    CPU.cycles = 8
    CPU.pc += 2

def _0x5D(CPU):
    CPU.registers["E"] = CPU.registers["L"]
    CPU.write_log("LD E,L ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x40(CPU):
    CPU.registers["B"] = CPU.registers["B"]
    CPU.write_log("LD B,B ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x67(CPU):
    CPU.registers["H"] = CPU.registers["A"]
    CPU.write_log("LD H,A ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x41(CPU):
    CPU.registers["B"] = CPU.registers["C"]
    CPU.write_log("LD B,C ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x42(CPU):
    CPU.registers["B"] = CPU.registers["D"]
    CPU.write_log("LD B,D ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x43(CPU):
    CPU.registers["B"] = CPU.registers["E"]
    CPU.write_log("LD B,E ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x44(CPU):
    CPU.registers["B"] = CPU.registers["H"]
    CPU.write_log("LD B,H ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x45(CPU):
    CPU.registers["B"] = CPU.registers["L"]
    CPU.write_log("LD B,L ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x48(CPU):
    CPU.registers["C"] = CPU.registers["B"]
    CPU.write_log("LD C,B ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x49(CPU):
    CPU.registers["C"] = CPU.registers["C"]
    CPU.write_log("LD C,C ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x4A(CPU):
    CPU.registers["C"] = CPU.registers["D"]
    CPU.write_log("LD C,D ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x4B(CPU):
    CPU.registers["C"] = CPU.registers["E"]
    CPU.write_log("LD C,E ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x4C(CPU):
    CPU.registers["C"] = CPU.registers["H"]
    CPU.write_log("LD C,H ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x4D(CPU):
    CPU.registers["C"] = CPU.registers["L"]
    CPU.write_log("LD C,L ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x50(CPU):
    CPU.registers["D"] = CPU.registers["B"]
    CPU.write_log("LD D,B ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x51(CPU):
    CPU.registers["D"] = CPU.registers["C"]
    CPU.write_log("LD D,C ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x52(CPU):
    CPU.registers["D"] = CPU.registers["D"]
    CPU.write_log("LD D,D ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x53(CPU):
    CPU.registers["D"] = CPU.registers["E"]
    CPU.write_log("LD D,E ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x54(CPU):
    CPU.registers["D"] = CPU.registers["H"]
    CPU.write_log("LD D,H ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x55(CPU):
    CPU.registers["D"] = CPU.registers["L"]
    CPU.write_log("LD D,L ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x58(CPU):
    CPU.registers["E"] = CPU.registers["B"]
    CPU.write_log("LD E,B ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x59(CPU):
    CPU.registers["E"] = CPU.registers["C"]
    CPU.write_log("LD E,C ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x5A(CPU):
    CPU.registers["E"] = CPU.registers["D"]
    CPU.write_log("LD E,D ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x5B(CPU):
    CPU.registers["E"] = CPU.registers["E"]
    CPU.write_log("LD E,E ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x5C(CPU):
    CPU.registers["E"] = CPU.registers["H"]
    CPU.write_log("LD E,H ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x5D(CPU):
    CPU.registers["E"] = CPU.registers["L"]
    CPU.write_log("LD E,L ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x5E(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["E"] = val
    CPU.write_log("LD E,(HL) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x60(CPU):
    CPU.registers["H"] = CPU.registers["B"]
    CPU.write_log("LD H,B ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x61(CPU):
    CPU.registers["H"] = CPU.registers["C"]
    CPU.write_log("LD H,C ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x62(CPU):
    CPU.registers["H"] = CPU.registers["D"]
    CPU.write_log("LD H,D ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x63(CPU):
    CPU.registers["H"] = CPU.registers["E"]
    CPU.write_log("LD H,E ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x64(CPU):
    CPU.registers["H"] = CPU.registers["H"]
    CPU.write_log("LD H,H ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x65(CPU):
    CPU.registers["H"] = CPU.registers["L"]
    CPU.write_log("LD H,L ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x66(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    val = CPU.memory[addr]
    CPU.registers["H"] = val
    CPU.write_log("LD H,(HL) " + format(val, 'x') + ' ' + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x68(CPU):
    CPU.registers["L"] = CPU.registers["B"]
    CPU.write_log("LD L,B ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x69(CPU):
    CPU.registers["L"] = CPU.registers["C"]
    CPU.write_log("LD L,C ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x6A(CPU):
    CPU.registers["L"] = CPU.registers["D"]
    CPU.write_log("LD L,D ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x6B(CPU):
    CPU.registers["L"] = CPU.registers["E"]
    CPU.write_log("LD L,E ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x6C(CPU):
    CPU.registers["L"] = CPU.registers["H"]
    CPU.write_log("LD L,H ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x6D(CPU):
    CPU.registers["L"] = CPU.registers["L"]
    CPU.write_log("LD L,L ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x74(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["H"]
    CPU.write_log("LD (HL),H " + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x75(CPU):
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["L"]
    CPU.write_log("LD (HL),L " + format(addr, 'x'))
    CPU.cycles = 8
    CPU.pc += 1

def _0x7F(CPU):
    CPU.registers["A"] = CPU.registers["A"]
    CPU.write_log("LD A,A ")
    CPU.cycles = 4
    CPU.pc += 1

def _0x08(CPU):
    msb = CPU.memory[CPU.pc + 2]
    lsb = CPU.memory[CPU.pc + 1]
    addr = (msb << 8) | lsb
    stack_msb = CPU.pop_stack()
    stack_lsb = CPU.pop_stack()
    CPU.memory[addr] = stack_lsb
    CPU.memory[addr + 1] = stack_msb
    CPU.write_log("LD (u16),SP " + format(addr, 'x') +  ' ' + format(stack_msb, 'x') +  ' ' + format(stack_lsb, 'x'))
    CPU.cycles = 20
    CPU.pc += 3

def _0xF9(CPU):
    #CPU.stack.append(CPU.registers["L"])
    #CPU.stack.append(CPU.registers["H"])
    CPU.sp = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.write_log("LD SP,HL " +  ' ' + format(CPU.registers["H"], 'x') +  ' ' + format(CPU.registers["L"], 'x'))
    CPU.cycles = 8
    CPU.pc += 1