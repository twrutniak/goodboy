from .instructions import JP, NOP, LD, INC, JR, DEC, DI, CALL, RET, PUSH, POP, OR, CP

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
    elif instruction == 0x3E:
        LD._0x3E(CPU)
    elif instruction == 0xE0:
        LD._0xE0(CPU)
    elif instruction == 0xCD:
        CALL._0xCD(CPU)
    elif instruction == 0x7D:
        LD._0x7D(CPU)
    elif instruction == 0x7C:
        LD._0x7C(CPU)
    elif instruction == 0x18:
        JR._0x18(CPU)
    elif instruction == 0xC9:
        RET._0xC9(CPU)
    elif instruction == 0xE5:
        PUSH._0xE5(CPU)
    elif instruction == 0xE1:
        POP._0xE1(CPU)
    elif instruction == 0xF5:
        PUSH._0xF5(CPU)
    elif instruction == 0x23:
        INC._0x23(CPU)
    elif instruction == 0xF1:
        POP._0xF1(CPU)
    elif instruction == 0xC5:
        PUSH._0xC5(CPU)
    elif instruction == 0x03:
        INC._0x03(CPU)
    elif instruction == 0xB1:
        OR._0xB1(CPU)
    elif instruction == 0x28:
        JR._0x28(CPU)
    elif instruction == 0xF0:
        LD._0xF0(CPU)
    elif instruction == 0xFE:
        CP._0xFE(CPU)
    elif instruction == 0xC1:
        POP._0xC1(CPU)
    elif instruction == 0xFA:
        LD._0xFA(CPU)
    else:
        print("Unsupported instruction %s" % hex(instruction))