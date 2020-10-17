from .instructions import JP, NOP, LD, INC, JR, DEC, DI

def dispatch(CPU):
    pc = CPU.pc
    instruction = CPU.memory[pc]

    if instruction == 0xC3:
        JP.__0xC3(CPU)
    elif instruction == 0x00:
        NOP._0x00(CPU)
    elif instruction == 0x21:
        LD._0x21(CPU)
    elif instruction == 0x47:
        LD._0x47(CPU)
    elif instruction == 0x11:
        LD._0x11(CPU)
    elif instruction == 0x0E:
        LD._0x0E(CPU)
    elif instruction == 0x2A:
        LD._0x2A(CPU)
    elif instruction == 0x12:
        LD._0x12(CPU)
    elif instruction == 0x1C:
        INC._0x1C(CPU)
    elif instruction == 0x20:
        JR._0x20(CPU)
    elif instruction == 0x14:
        INC._0x14(CPU)
    elif instruction == 0x0D:
        DEC._0x0D(CPU)
    elif instruction == 0x78:
        LD._0x78(CPU)
    elif instruction == 0x01:
        LD._0x01(CPU)
    elif instruction == 0x04:
        INC._0x04(CPU)
    elif instruction == 0x05:
        DEC._0x05(CPU)
    elif instruction == 0xF3:
        DI._0xF3(CPU)
    elif instruction == 0x31:
        LD._0x31(CPU)
    elif instruction == 0xEA:
        LD._0xEA(CPU)
    else:
        print("Unsupported instruction %s" % hex(instruction))