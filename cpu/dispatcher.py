from .instructions import JP, NOP, LD, INC, JR, DEC, DI, CALL, RET, PUSH, POP, OR, CP, AND, XOR, ADD, SUB, SRL, RR, RRA, ADC

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
    elif instruction == 0xE6:
        AND._0xE6(CPU)
    elif instruction == 0xC4:
        CALL._0xC4(CPU)
    elif instruction == 0x06:
        LD._0x06(CPU)
    elif instruction == 0x77:
        LD._0x77(CPU)
    elif instruction == 0x2C:
        INC._0x2C(CPU)
    elif instruction == 0x24:
        INC._0x24(CPU)
    elif instruction == 0x1A:
        LD._0x1A(CPU)
    elif instruction == 0x13:
        INC._0x13(CPU)
    elif instruction == 0xA9:
        XOR._0xA9(CPU)
    elif instruction == 0x22:
        LD._0x22(CPU)
    elif instruction == 0xC6:
        ADD._0xC6(CPU)
    elif instruction == 0x32:
        LD._0x32(CPU)
    elif instruction == 0xD6:
        SUB._0xD6(CPU)
    elif instruction == 0xB7:
        OR._0xB7(CPU)
    elif instruction == 0xD5:
        PUSH._0xD5(CPU)
    elif instruction == 0x46:
        LD._0x46(CPU)
    elif instruction == 0x2D:
        DEC._0x2D(CPU)
    elif instruction == 0x4E:
        LD._0x4E(CPU)
    elif instruction == 0x56:
        LD._0x56(CPU)
    elif instruction == 0xAE:
        XOR._0xAE(CPU)
    elif instruction == 0x26:
        LD._0x26(CPU)
    elif instruction == 0x1F:
        RRA._0x1F(CPU)
    elif instruction == 0x30:
        JR._0x30(CPU)
    elif instruction == 0x5F:
        LD._0x5F(CPU)
    elif instruction == 0xEE:
        XOR._0xEE(CPU)
    elif instruction == 0x79:
        LD._0x79(CPU)
    elif instruction == 0x4F:
        LD._0x4F(CPU)
    elif instruction == 0x7A:
        LD._0x7A(CPU)
    elif instruction == 0x57:
        LD._0x57(CPU)
    elif instruction == 0x7B:
        LD._0x7B(CPU)
    elif instruction == 0x25:
        DEC._0x25(CPU)
    elif instruction == 0x72:
        LD._0x72(CPU)
    elif instruction == 0x71:
        LD._0x71(CPU)
    elif instruction == 0x70:
        LD._0x70(CPU)
    elif instruction == 0xD1:
        POP._0xD1(CPU)
    elif instruction == 0xCE:
        ADC._0xCE(CPU)
    elif instruction == 0xD0:
        RET._0xD0(CPU)
    elif instruction == 0xC8:
        RET._0xC8(CPU)
    elif instruction == 0x3D:
        DEC._0x3D(CPU)
    elif instruction == 0xB6:
        OR._0xB6(CPU)
    elif instruction == 0x35:
        DEC._0x35(CPU)
    elif instruction == 0x6E:
        LD._0x6E(CPU)
    elif instruction == 0x6F:
        LD._0x6F(CPU)
    elif instruction == 0x29:
        ADD._0x29(CPU)
    elif instruction == 0x1D:
        DEC._0x1D(CPU)
    elif instruction == 0xE9:
        JP.__0xE9(CPU)
    elif instruction == 0x2E:
        LD._0x2E(CPU)
    elif instruction == 0xAF:
        XOR._0xAF(CPU)
    elif instruction == 0x5D:
        LD._0x5D(CPU)
    elif instruction == 0x73:
        LD._0x73(CPU)
    elif instruction == 0x40:
        LD._0x40(CPU)
    elif instruction == 0xAD:
        XOR._0xAD(CPU)
    elif instruction == 0x7E:
        LD._0x7E(CPU)
    elif instruction == 0x67:
        LD._0x67(CPU)
    elif instruction == 0xB0:
        OR._0xB0(CPU)
    elif instruction == 0x41:
        LD._0x41(CPU)
    elif instruction == 0x42:
        LD._0x42(CPU)
    elif instruction == 0x43:
        LD._0x43(CPU)
    elif instruction == 0x44:
        LD._0x44(CPU)
    elif instruction == 0x45:
        LD._0x45(CPU)
    elif instruction == 0x48:
        LD._0x48(CPU)
    elif instruction == 0x49:
        LD._0x49(CPU)
    elif instruction == 0x4A:
        LD._0x4A(CPU)
    elif instruction == 0x4B:
        LD._0x4B(CPU)
    elif instruction == 0x4C:
        LD._0x4C(CPU)
    elif instruction == 0x4D:
        LD._0x4D(CPU)
    elif instruction == 0x50:
        LD._0x50(CPU)
    elif instruction == 0x51:
        LD._0x51(CPU)
    elif instruction == 0x52:
        LD._0x52(CPU)
    elif instruction == 0x53:
        LD._0x53(CPU)
    elif instruction == 0x54:
        LD._0x54(CPU)
    elif instruction == 0x55:
        LD._0x55(CPU)
    elif instruction == 0x58:
        LD._0x58(CPU)
    elif instruction == 0x59:
        LD._0x59(CPU)
    elif instruction == 0x5A:
        LD._0x5A(CPU)
    elif instruction == 0x5B:
        LD._0x5B(CPU)
    elif instruction == 0x5C:
        LD._0x5C(CPU)
    elif instruction == 0x5D:
        LD._0x5D(CPU)
    elif instruction == 0x5E:
        LD._0x5E(CPU)
    elif instruction == 0x60:
        LD._0x60(CPU)
    elif instruction == 0x61:
        LD._0x61(CPU)
    elif instruction == 0x62:
        LD._0x62(CPU)
    elif instruction == 0x63:
        LD._0x63(CPU)
    elif instruction == 0x64:
        LD._0x64(CPU)
    elif instruction == 0x65:
        LD._0x65(CPU)
    elif instruction == 0x66:
        LD._0x66(CPU)
    elif instruction == 0x68:
        LD._0x68(CPU)
    elif instruction == 0x69:
        LD._0x69(CPU)
    elif instruction == 0x6A:
        LD._0x6A(CPU)
    elif instruction == 0x6B:
        LD._0x6B(CPU)
    elif instruction == 0x6C:
        LD._0x6C(CPU)
    elif instruction == 0x6D:
        LD._0x6D(CPU)
    elif instruction == 0x74:
        LD._0x74(CPU)
    elif instruction == 0x75:
        LD._0x75(CPU)
    elif instruction == 0x7F:
        LD._0x7F(CPU)
    elif instruction == 0x3C:
        INC._0x3C(CPU)
    elif instruction == 0xD8:
        RET._0xD8(CPU)
    elif instruction == 0xCB:
        instruction = CPU.memory[pc + 1]
        if instruction == 0x38:
            SRL._0x38(CPU)
        elif instruction == 0x19:
            RR._0x19(CPU)
        elif instruction == 0x1A:
            RR._0x1A(CPU)
        elif instruction == 0x1B:
            RR._0x1B(CPU)
        else:
            print("Unsupported CB table instruction %s" % hex(instruction)) 
    else:
        print("Unsupported instruction %s" % hex(instruction))