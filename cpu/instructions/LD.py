from .misc import *

def _0x40(CPU):
    CPU.pc += 1
    CPU.registers["B"] = CPU.registers["B"]
    CPU.mnemonic = "LD B,B"
    CPU.cycles = 4


def _0x50(CPU):
    CPU.pc += 1
    CPU.registers["D"] = CPU.registers["B"]
    CPU.mnemonic = "LD D,B"
    CPU.cycles = 4
    

def _0x60(CPU):
    CPU.pc += 1
    CPU.registers["H"] = CPU.registers["B"]
    CPU.mnemonic = "LD H,B"
    CPU.cycles = 4

def _0x70(CPU):
    CPU.pc += 1
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["B"]
    CPU.mnemonic = "LD (HL),B"
    CPU.cycles = 8

def _0xE0(CPU):
    u8 = CPU.memory[CPU.pc + 1]
    val = 0xFF00 + u8
    CPU.memory[val] = CPU.registers["A"]
    CPU.mnemonic = "LD (FF00+u8), A"
    CPU.cycles = 12
    CPU.pc += 2

def _0xF0(CPU):
    u8 = CPU.memory[CPU.pc + 1]
    val = 0xFF00 + u8
    CPU.registers["A"] = CPU.memory[val]
    CPU.mnemonic = "LD A, (FF00+u8)"
    CPU.cycles = 12
    CPU.pc += 2

def _0x01(CPU):
    lsb = CPU.memory[CPU.pc + 1]
    msb = CPU.memory[CPU.pc + 2]
    CPU.registers["C"] = lsb
    CPU.registers["B"] = msb
    CPU.mnemonic = "LD BC, {}{}".format(str(hex(msb)), str(hex(lsb)))
    CPU.cycles = 12
    CPU.pc += 3

def _0x11(CPU):
    lsb = CPU.memory[CPU.pc + 1]
    msb = CPU.memory[CPU.pc + 2]
    CPU.registers["E"] = lsb
    CPU.registers["D"] = msb
    CPU.mnemonic = "LD DE, {}{}".format(str(hex(msb)), str(hex(lsb)))
    CPU.cycles = 12
    CPU.pc += 3

def _0x21(CPU):
    lsb = CPU.memory[CPU.pc + 1]
    msb = CPU.memory[CPU.pc + 2]
    CPU.registers["L"] = lsb
    CPU.registers["H"] = msb
    CPU.mnemonic = "LD HL, {}{}".format(str(hex(msb)), str(hex(lsb)))
    CPU.cycles = 12
    CPU.pc += 3

def _0x31(CPU):
    lsb = CPU.memory[CPU.pc + 1]
    msb = CPU.memory[CPU.pc + 2]
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.mnemonic = "SP , {}{}".format(str(hex(msb)), str(hex(lsb)))
    CPU.cycles = 12
    CPU.pc += 3

def _0x41(CPU):
    CPU.pc += 1
    CPU.registers["B"] = CPU.registers["C"]
    CPU.mnemonic = "LD B,C"
    CPU.cycles = 4
    

def _0x51(CPU):
    CPU.pc += 1
    CPU.registers["D"] = CPU.registers["C"]
    CPU.mnemonic = "LD D,C"
    CPU.cycles = 4


def _0x61(CPU):
    CPU.pc += 1
    CPU.registers["H"] = CPU.registers["C"]
    CPU.mnemonic = "LD H,C"
    CPU.cycles = 4


def _0x71(CPU):
    CPU.pc += 1
    lsb = CPU.registers["L"]
    msb = CPU.registers["H"] << 8
    CPU.memory[(msb | lsb)] = CPU.registers["C"]
    CPU.mnemonic = "LD (HL),C"
    CPU.cycles = 4

def _0x02(CPU):
    CPU.pc += 1
    lsb = CPU.registers["C"]
    msb = CPU.registers["B"] << 8
    CPU.memory[(msb | lsb)] = CPU.registers["A"]
    CPU.mnemonic = "LD (BC),A"
    CPU.cycles = 8

def _0x12(CPU):
    CPU.pc += 1
    lsb = CPU.registers["E"]
    msb = CPU.registers["D"] << 8
    CPU.memory[(msb | lsb)] = CPU.registers["A"]
    CPU.mnemonic = "LD (DE),A"
    CPU.cycles = 8

def _0x22(CPU):
    CPU.pc += 1
    lsb = CPU.registers["L"]
    msb = CPU.registers["H"] << 8
    CPU.memory[(msb | lsb)] = CPU.registers["A"]
    CPU.memory[(msb | lsb)] += 1
    CPU.mnemonic = "LD (HL+),A"
    CPU.cycles = 8

def _0x32(CPU):
    CPU.pc += 1
    lsb = CPU.registers["L"]
    msb = CPU.registers["H"] << 8
    CPU.memory[(msb | lsb)] = CPU.registers["A"]
    CPU.memory[(msb | lsb)] -= 1
    CPU.mnemonic = "LD (HL-),A"
    CPU.cycles = 8

def _0x42(CPU):
    CPU.pc += 1
    CPU.registers["B"] = CPU.registers["D"]
    CPU.mnemonic = "LD B,D"
    CPU.cycles = 4

def _0x52(CPU):
    CPU.pc += 1
    CPU.registers["D"] = CPU.registers["D"]
    CPU.mnemonic = "LD D,D"
    CPU.cycles = 4

def _0x62(CPU):
    CPU.pc += 1
    CPU.registers["H"] = CPU.registers["D"]
    CPU.mnemonic = "LD H,D"
    CPU.cycles = 4

def _0x72(CPU):
    CPU.pc += 1
    lsb = CPU.registers["L"]
    msb = CPU.registers["H"] << 8
    CPU.memory[(msb | lsb)] = CPU.registers["D"]
    CPU.mnemonic = "LD (HL),D"
    CPU.cycles = 8


def _0xE2(CPU):
    CPU.pc += 1
    CPU.memory[0xFF00 + CPU.registers["C"]] = CPU.registers["D"]                
    CPU.mnemonic = "LD (FF00+C),D"
    CPU.cycles = 8

def _0xF2(CPU):
    CPU.pc += 1
    CPU.registers["A"] = CPU.memory[0xFF00 + CPU.registers["C"]]
    CPU.mnemonic = "LD A,(0xFF00 + C)"
    CPU.cycles = 8


def _0x43(CPU):
    CPU.registers["B"] = CPU.registers["E"]
    CPU.mnemonic = "LD B,E"
    CPU.cycles = 4
    CPU.pc += 1

def _0x53(CPU):
    CPU.pc += 1
    CPU.registers["D"] = CPU.registers["E"]
    CPU.mnemonic = "LD D,E"
    CPU.cycles = 4

def _0x63(CPU):
    CPU.pc += 1
    CPU.registers["H"] = CPU.registers["E"]
    CPU.mnemonic = "LD H,E"
    CPU.cycles = 4

def _0x73(CPU):
    CPU.pc += 1
    msb = CPU.registers["H"]
    lsb = CPU.registers["L"]

    CPU.memory[(msb << 8) | lsb] = CPU.registers["E"]

    CPU.mnemonic = "LD (HL),E"
    CPU.cycles = 8


def _0x44(CPU):
    CPU.pc += 1
    CPU.registers["B"] = CPU.registers["H"]
    CPU.mnemonic = "LD B,H"
    CPU.cycles = 4


def _0x54(CPU):
    CPU.pc += 1
    CPU.registers["D"] = CPU.registers["L"]
    CPU.mnemonic = "LD D,L"
    CPU.cycles = 4


def _0x64(CPU):
    CPU.pc += 1
    CPU.registers["H"] = CPU.registers["L"]
    CPU.mnemonic = "LD H,L"
    CPU.cycles = 4


def _0x74(CPU):
    CPU.pc += 1
    msb = CPU.registers["H"]
    lsb = CPU.registers["L"]
    addr = (msb << 8) | lsb
    CPU.memory[addr] = CPU.registers["H"]
    CPU.mnemonic = "LD (HL),H"
    CPU.cycles = 8

def _0x45(CPU):
    CPU.pc += 1
    CPU.registers["B"] = CPU.registers["L"]
    CPU.mnemonic = "LD B,L"
    CPU.cycles = 4

def _0x55(CPU):
    CPU.pc += 1
    CPU.registers["D"] = CPU.registers["L"]
    CPU.mnemonic = "LD D,L"
    CPU.cycles = 4

def _0x65(CPU):
    CPU.pc += 1
    CPU.registers["H"] = CPU.registers["L"]
    CPU.mnemonic = "LD H,L"
    CPU.cycles = 4

def _0x75(CPU):
    CPU.pc += 1
    msb = CPU.registers["H"]
    lsb = CPU.registers["L"]
    addr = (msb << 8) | lsb
    CPU.memory[addr] = CPU.registers["L"]
    CPU.mnemonic = "LD (HL), L"
    CPU.cycles = 8

def _0x06(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.pc += 2
    CPU.registers["B"] = val
    CPU.mnemonic = "LD B, u8"
    CPU.cycles = 8

def _0x16(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.pc += 2
    CPU.registers["D"] = val
    CPU.mnemonic = "LD D, u8"
    CPU.cycles = 8

def _0x26(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.pc += 2
    CPU.registers["H"] = val
    CPU.mnemonic = "LD H, u8"
    CPU.cycles = 8

def _0x36(CPU):
    val = CPU.memory[CPU.pc + 1]
    CPU.pc += 2
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.registers[addr] = val
    CPU.mnemonic = "LD (HL), u8"
    CPU.cycles = 12

def _0x46(CPU):
    CPU.pc += 1
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.registers["B"] = CPU.memory[addr] 
    CPU.mnemonic = "LD B, (HL)"
    CPU.cycles = 8

def _0x56(CPU):
    CPU.pc += 1
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.registers["D"] = CPU.memory[addr] 
    CPU.mnemonic = "LD D, (HL)"
    CPU.cycles = 8

def _0x66(CPU):
    CPU.pc += 1
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.registers["H"] = CPU.memory[addr] 
    CPU.mnemonic = "LD H, (HL)"
    CPU.cycles = 8

def _0x47(CPU):
    CPU.pc += 1
    CPU.registers["B"] = CPU.registers["A"]
    CPU.mnemonic = "LD B,A"
    CPU.cycles = 4

def _0x57(CPU):
    CPU.pc += 1
    CPU.registers["D"] = CPU.registers["A"]
    CPU.mnemonic = "LD D,A"
    CPU.cycles = 4

def _0x67(CPU):
    CPU.pc += 1
    CPU.registers["H"] = CPU.registers["A"]
    CPU.mnemonic = "LD H,A"
    CPU.cycles = 4

def _0x77(CPU):
    CPU.pc += 1
    addr = (CPU.registers["H"] << 8) | CPU.registers["L"]
    CPU.memory[addr] = CPU.registers["A"]
    CPU.mnemonic = "LD (HL),A"
    CPU.cycles = 8

def _0x08(CPU):
    lsb = CPU.memory[CPU.pc + 1]
    msb = CPU.memory[CPU.pc + 2]
    addr = (msb << 8) | lsb
    CPU.memory[addr] = CPU.stack[-2]
    CPU.memory[addr + 1] = CPU.stack[-1]
    CPU.pc += 3
    CPU.mnemonic = "LD (u16),SP"
    CPU.cycles = 20

def _0x48(CPU):
    CPU.pc += 1
    CPU.registers["C"] = CPU.registers["B"]
    CPU.mnemonic = "LD C,B"
    CPU.cycles = 4

def _0x58(CPU):
    CPU.pc += 1
    CPU.registers["E"] = CPU.registers["B"]
    CPU.mnemonic = "LD E,B"
    CPU.cycles = 4

def _0x68(CPU):
    CPU.pc += 1
    CPU.registers["L"] = CPU.registers["B"]
    CPU.mnemonic = "LD L,B"
    CPU.cycles = 4

def _0x78(CPU):
    CPU.pc += 1
    CPU.registers["A"] = CPU.registers["B"]
    CPU.mnemonic = "LD A,B"
    CPU.cycles = 4

def _0xf8(CPU):
    val = convert_signed(CPU.memory[CPU.pc + 1])
    CPU.pc += 2
    msb = CPU.stack.pop()
    lsb = CPU.stack.pop()
    addr = (msb << 8) | lsb
    hcflag = check_halfcarry(addr, val, "16")
    addr, cflag = check_carry(addr, val, "16")
    CPU.registers["H"] = (addr & 0xff00) >> 8
    CPU.registers["L"] = addr & 0xff
    CPU.flags["Z"] = 0
    CPU.flags["S"] = 0
    CPU.flags["HC"] = hcflag
    CPU.flags["C"] = cflag
    CPU.mnemonic = "LD HL, SP + i8"
    CPU.cycles = 4

def _0x49(CPU):
    CPU.pc += 1
    CPU.registers['C'] = CPU.registers['C']
    CPU.mnemonic = "LD C,C"
    CPU.cycles = 4

def _0x59(CPU):
    CPU.pc += 1
    CPU.registers['E'] = CPU.registers['C']
    CPU.mnemonic = "LD E,C"
    CPU.cycles = 4

def _0x69(CPU):
    CPU.pc += 1
    CPU.registers['L'] = CPU.registers['C']
    CPU.mnemonic = "LD L,C"
    CPU.cycles = 4

def _0x79(CPU):
    CPU.pc += 1
    CPU.registers['A'] = CPU.registers['C']
    CPU.mnemonic = "LD A,C"
    CPU.cycles = 4

def _0xF9(CPU):
    CPU.pc += 1 
    CPU.stack.append(CPU.registers['L'])
    CPU.stack.append(CPU.registers['H'])
    CPU.mnemonic = "LD SP,HL"
    CPU.cycles = 8

def _0x0A(CPU):
    CPU.pc += 1
    addr = (CPU.registers['B'] < 8) | CPU.registers['C']
    CPU.registers['A'] = CPU.memory[addr]
    CPU.mnemonic = "LD A,(BC)"
    CPU.cycles = 8

def _0x1A(CPU):
    CPU.pc += 1
    addr = (CPU.registers['D'] < 8) | CPU.registers['E']
    CPU.registers['A'] = CPU.memory[addr]
    CPU.mnemonic = "LD A,(DE)"
    CPU.cycles = 8

def _0x2A(CPU):
    CPU.pc += 1
    addr = (CPU.registers['H'] < 8) | CPU.registers['L']
    CPU.registers['A'] = CPU.memory[addr+1]
    CPU.mnemonic = "LD A,(HL+)"
    CPU.cycles = 8

def _0x3A(CPU):
    CPU.pc += 1
    addr = (CPU.registers['H'] < 8) | CPU.registers['L']
    CPU.registers['A'] = CPU.memory[addr-1]
    CPU.mnemonic = "LD A,(HL-)"
    CPU.cycles = 8

def _0x4A(CPU):
    CPU.pc += 1
    CPU.registers['C'] = CPU.registers['D']
    CPU.mnemonic = "LD C,D"
    CPU.cycles = 4

def _0x5A(CPU):
    CPU.pc += 1
    CPU.registers['E'] = CPU.registers['D']
    CPU.mnemonic = "LD E,D"
    CPU.cycles = 4

def _0x6A(CPU):
    CPU.pc += 1
    CPU.registers['L'] = CPU.registers['D']
    CPU.mnemonic = "LD L,D"
    CPU.cycles = 4

def _0x7A(CPU):
    CPU.pc += 1
    CPU.registers['A'] = CPU.registers['D']
    CPU.mnemonic = "LD A,D"
    CPU.cycles = 4

def _0xEA(CPU):
    lsb = CPU.memory[CPU.pc + 1]
    msb = CPU.memory[CPU.pc + 2]
    CPU.memory[(msb << 8) | lsb] = CPU.registers['A']
    CPU.pc += 3
    CPU.mnemonic = "LD (u16), A"
    CPU.cycles = 16

def _0xEA(CPU):
    lsb = CPU.memory[CPU.pc + 1]
    msb = CPU.memory[CPU.pc + 2]
    CPU.registers['A'] = CPU.memory[(msb << 8) | lsb]
    CPU.pc += 3
    CPU.mnemonic = "LD A,(u16)"
    CPU.cycles = 16