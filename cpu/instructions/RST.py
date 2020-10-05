def _0xC7(CPU):
    msb = (CPU.pc & 0xf0) >> 8
    lsb = CPU.pc & 0xf
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.pc = 0x0000
    CPU.mnemonic = "RST 00h"
    CPU.cycles = 16

def _0xD7(CPU):
    msb = (CPU.pc & 0xf0) >> 8
    lsb = CPU.pc & 0xf
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.pc = 0x0010
    CPU.mnemonic = "RST 10h"
    CPU.cycles = 16

def _0xE7(CPU):
    msb = (CPU.pc & 0xf0) >> 8
    lsb = CPU.pc & 0xf
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.pc = 0x0020
    CPU.mnemonic = "RST 20h"
    CPU.cycles = 16

def _0xF7(CPU):
    msb = (CPU.pc & 0xf0) >> 8
    lsb = CPU.pc & 0xf
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.pc = 0x0030
    CPU.mnemonic = "RST 30h"
    CPU.cycles = 16

def _0xCF(CPU):
    msb = (CPU.pc & 0xf0) >> 8
    lsb = CPU.pc & 0xf
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.pc = 0x0008
    CPU.mnemonic = "RST 08h"
    CPU.cycles = 16

def _0xDF(CPU):
    msb = (CPU.pc & 0xf0) >> 8
    lsb = CPU.pc & 0xf
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.pc = 0x0018
    CPU.mnemonic = "RST 18h"
    CPU.cycles = 16

def _0xEF(CPU):
    msb = (CPU.pc & 0xf0) >> 8
    lsb = CPU.pc & 0xf
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.pc = 0x0028
    CPU.mnemonic = "RST 28h"
    CPU.cycles = 16

def _0xFF(CPU):
    msb = (CPU.pc & 0xf0) >> 8
    lsb = CPU.pc & 0xf
    CPU.stack.append(lsb)
    CPU.stack.append(msb)
    CPU.pc = 0x0038
    CPU.mnemonic = "RST 38h"
    CPU.cycles = 16