from .instructions import ADC, ADD, AND, CALL, CCF, CP, CPL, DAA, DEC, DI, EI, HALT, INC, JP, JR, LD, NOP, OR, POP, PUSH, RET, RLCA, RRCA, RST, SBC, SCF, STOP, SUB, XOR

def dispatch(CPU):
    instruction = CPU.memory[CPU.pc]
    if instruction == 0x0:
        NOP._0x00(CPU)
    if instruction == 0x10:
        STOP._0x10(CPU)
    if instruction == 0x20:
        JR._0x20(CPU)
    if instruction == 0x30:
        JR._0x30(CPU)
    if instruction == 0x40:
        LD._0x40(CPU)
    if instruction == 0x50:
        LD._0x50(CPU)
    if instruction == 0x60:
        LD._0x60(CPU)
    if instruction == 0x70:
        LD._0x70(CPU)
    if instruction == 0x80:
        ADD._0x80(CPU)
    if instruction == 0x90:
        SUB._0x90(CPU)
    if instruction == 0xA0:
        AND._0xA0(CPU)
    if instruction == 0xB0:
        OR._0xB0(CPU)
    if instruction == 0xC0:
        RET._0xC0(CPU)
    if instruction == 0xD0:
        RET._0xD0(CPU)
    if instruction == 0xE0:
        LD._0xE0(CPU)
    if instruction == 0xF0:
        LD._0xF0(CPU)
    if instruction == 0x01:
        LD._0x01(CPU)
    if instruction == 0x11:
        LD._0x11(CPU)
    if instruction == 0x21:
        LD._0x21(CPU)
    if instruction == 0x31:
        LD._0x31(CPU)
    if instruction == 0x41:
        LD._0x41(CPU)
    if instruction == 0x51:
        LD._0x51(CPU)
    if instruction == 0x61:
        LD._0x61(CPU)
    if instruction == 0x71:
        LD._0x71(CPU)
    if instruction == 0x81:
        ADD._0x81(CPU)
    if instruction == 0x91:
        SUB._0x91(CPU)
    if instruction == 0xA1:
        AND._0xA1(CPU)
    if instruction == 0xB1:
        OR._0xB1(CPU)
    if instruction == 0xC1:
        POP._0xC1(CPU)
    if instruction == 0xD1:
        POP._0xD1(CPU)
    if instruction == 0xE1:
        POP._0xE1(CPU)
    if instruction == 0xF1:
        POP._0xF1(CPU)
    if instruction == 0x02:
        LD._0x02(CPU)
    if instruction == 0x12:
        LD._0x12(CPU)
    if instruction == 0x22:
        LD._0x22(CPU)
    if instruction == 0x32:
        LD._0x32(CPU)
    if instruction == 0x42:
        LD._0x42(CPU)
    if instruction == 0x52:
        LD._0x52(CPU)
    if instruction == 0x62:
        LD._0x62(CPU)
    if instruction == 0x72:
        LD._0x72(CPU)
    if instruction == 0x82:
        ADD._0x82(CPU)
    if instruction == 0x92:
        SUB._0x92(CPU)
    if instruction == 0xA2:
        AND._0xA2(CPU)
    if instruction == 0xB2:
        OR._0xB2(CPU)
    if instruction == 0xC2:
        JP._0xC2(CPU)
    if instruction == 0xD2:
        JP._0xD2(CPU)
    if instruction == 0xE2:
        LD._0xE2(CPU)
    if instruction == 0xF2:
        LD._0xF2(CPU)
    if instruction == 0x03:
        INC._0x03(CPU)
    if instruction == 0x13:
        INC._0x13(CPU)
    if instruction == 0x23:
        INC._0x23(CPU)
    if instruction == 0x33:
        INC._0x33(CPU)
    if instruction == 0x43:
        LD._0x43(CPU)
    if instruction == 0x53:
        LD._0x53(CPU)
    if instruction == 0x63:
        LD._0x63(CPU)
    if instruction == 0x73:
        LD._0x73(CPU)
    if instruction == 0x83:
        ADD._0x83(CPU)
    if instruction == 0x93:
        SUB._0x93(CPU)
    if instruction == 0xA3:
        AND._0xA3(CPU)
    if instruction == 0xB3:
        OR._0xB3(CPU)
    if instruction == 0xC3:
        JP._0xC3(CPU)
    if instruction == 0xF3:
        DI._0xF3(CPU)
    if instruction == 0x04:
        INC._0x04(CPU)
    if instruction == 0x14:
        INC._0x14(CPU)
    if instruction == 0x24:
        INC._0x24(CPU)
    if instruction == 0x34:
        INC._0x34(CPU)
    if instruction == 0x44:
        LD._0x44(CPU)
    if instruction == 0x54:
        LD._0x54(CPU)
    if instruction == 0x64:
        LD._0x64(CPU)
    if instruction == 0x74:
        LD._0x74(CPU)
    if instruction == 0x84:
        ADD._0x84(CPU)
    if instruction == 0x94:
        SUB._0x94(CPU)
    if instruction == 0xA4:
        AND._0xA4(CPU)
    if instruction == 0xB4:
        OR._0xB4(CPU)
    if instruction == 0xC4:
        CALL._0xC4(CPU)
    if instruction == 0xD4:
        CALL._0xD4(CPU)
    if instruction == 0x05:
        DEC._0x05(CPU)
    if instruction == 0x15:
        DEC._0x15(CPU)
    if instruction == 0x25:
        DEC._0x25(CPU)
    if instruction == 0x35:
        DEC._0x35(CPU)
    if instruction == 0x45:
        LD._0x45(CPU)
    if instruction == 0x55:
        LD._0x65(CPU)
    if instruction == 0x65:
        LD._0x65(CPU)
    if instruction == 0x75:
        LD._0x75(CPU)
    if instruction == 0x85:
        ADD._0x85(CPU)
    if instruction == 0x95:
        SUB._0x95(CPU)
    if instruction == 0xA5:
        AND._0xA5(CPU)
    if instruction == 0xB5:
        OR._0xB5(CPU)
    if instruction == 0xC5:
        PUSH._0xC5(CPU)
    if instruction == 0xD5:
        PUSH._0xD5(CPU)
    if instruction == 0xE5:
        PUSH._0xE5(CPU)
    if instruction == 0xF5:
        PUSH._0xF5(CPU)
    if instruction == 0x06:
        LD._0x06(CPU)
    if instruction == 0x16:
        LD._0x16(CPU)
    if instruction == 0x26:
        LD._0x26(CPU)
    if instruction == 0x36:
        LD._0x36(CPU)
    if instruction == 0x46:
        LD._0x46(CPU)
    if instruction == 0x56:
        LD._0x56(CPU)
    if instruction == 0x66:
        LD._0x66(CPU)
    if instruction == 0x76:
        HALT._0x76(CPU)
    if instruction == 0x86:
        ADD._0x86(CPU)
    if instruction == 0x96:
        SUB._0x96(CPU)
    if instruction == 0xA6:
        AND._0xA6(CPU)
    if instruction == 0xB6:
        OR._0xB6(CPU)
    if instruction == 0xC6:
        ADD._0xC6(CPU)
    if instruction == 0xD6:
        SUB._0xD6(CPU)
    if instruction == 0xE6:
        AND._0xE6(CPU)
    if instruction == 0xF6:
        OR._0xF6(CPU)
    if instruction == 0x07:
        RLCA._0x07(CPU)
    if instruction == 0x17:
        RLCA._0x17(CPU)
    if instruction == 0x27:
        DAA._0x27(CPU)
    if instruction == 0x37:
        SCF._0x37(CPU)
    if instruction == 0x47:
        LD._0x47(CPU)
    if instruction == 0x57:
        LD._0x57(CPU)
    if instruction == 0x67:
        LD._0x67(CPU)
    if instruction == 0x77:
        LD._0x77(CPU)
    if instruction == 0x87:
        ADD._0x87(CPU)
    if instruction == 0x97:
        SUB._0x97(CPU)
    if instruction == 0xA7:
        AND._0xA7(CPU)
    if instruction == 0xB7:
        OR._0xB7(CPU)
    if instruction == 0xC7:
        RST._0xC7(CPU)
    if instruction == 0xD7:
        RST._0xD7(CPU)
    if instruction == 0xE7:
        RST._0xE7(CPU)
    if instruction == 0xF7:
        RST._0xF7(CPU)
    if instruction == 0x08:
        LD._0x08(CPU)
    if instruction == 0x18:
        JR._0x18(CPU)
    if instruction == 0x28:
        JR._0x28(CPU)
    if instruction == 0x38:
        JR._0x38(CPU)
    if instruction == 0x48:
        LD._0x48(CPU)
    if instruction == 0x58:
        LD._0x58(CPU)
    if instruction == 0x68:
        LD._0x68(CPU)
    if instruction == 0x78:
        LD._0x78(CPU)
    if instruction == 0x88:
        ADC._0x88(CPU)
    if instruction == 0x98:
        SBC._0x98(CPU)
    if instruction == 0xA8:
        XOR._0xA8(CPU)
    if instruction == 0xB8:
        CP._0xB8(CPU)
    if instruction == 0xC8:
        RET._0xC8(CPU)
    if instruction == 0xD8:
        RET._0xD8(CPU)
    if instruction == 0xE8:
        ADD._0xE8(CPU)
    if instruction == 0xF8:
        LD._0xF8(CPU)
    if instruction == 0x0A:
        LD._0x0A(CPU)
    if instruction == 0x1A:
        LD._0x1A(CPU)
    if instruction == 0x2A:
        LD._0x2A(CPU)
    if instruction == 0x3A:
        LD._0x3A(CPU)
    if instruction == 0x4A:
        LD._0x4A(CPU)
    if instruction == 0x5A:
        LD._0x5A(CPU)
    if instruction == 0x6A:
        LD._0x6A(CPU)
    if instruction == 0x7A:
        LD._0x7A(CPU)
    if instruction == 0x8A:
        ADC._0x8A(CPU)
    if instruction == 0x9A:
        SBC._0x9A(CPU)
    if instruction == 0xAA:
        XOR._0xAA(CPU)
    if instruction == 0xBA:
        CP._0xBA(CPU)
    if instruction == 0xCA:
        JP._0xCA(CPU)
    if instruction == 0xDA:
        JP._0xDA(CPU)
    if instruction == 0xEA:
        LD._0xEA(CPU)
    if instruction == 0xFA:
        LD._0xFA(CPU)
    if instruction == 0x0B:
        DEC._0x0B(CPU)
    if instruction == 0x1B:
        DEC._0x1B(CPU)
    if instruction == 0x2B:
        DEC._0x2B(CPU)
    if instruction == 0x3B:
        DEC._0x3B(CPU)
    if instruction == 0x4B:
        LD._0x4B(CPU)
    if instruction == 0x5B:
        LD._0x5B(CPU)
    if instruction == 0x6B:
        LD._0x6B(CPU)
    if instruction == 0x7B:
        LD._0x7B(CPU)
    if instruction == 0x8B:
        ADC._0x8B(CPU)
    if instruction == 0x9B:
        SBC._0x9B(CPU)
    if instruction == 0xAB:
        XOR._0xAB(CPU)
    if instruction == 0xBB:
        CP._0xBB(CPU)
    # 0xCB prefix table not yet implemented
    if instruction == 0xFB:
        EI._0xFB(CPU)
    if instruction == 0x0C:
        INC._0x0C(CPU)
    if instruction == 0x1C:
        INC._0x1C(CPU)
    if instruction == 0x2C:
        INC._0x2C(CPU)
    if instruction == 0x3C:
        INC._0x3C(CPU)
    if instruction == 0x4C:
        LD._0x4C(CPU)
    if instruction == 0x5C:
        LD._0x5C(CPU)
    if instruction == 0x6C:
        LD._0x6C(CPU)
    if instruction == 0x7C:
        LD._0x7C(CPU)
    if instruction == 0x8C:
        ADC._0x8C(CPU)
    if instruction == 0x9C:
        SBC._0x9C(CPU)
    if instruction == 0xAC:
        XOR._0xAC(CPU)
    if instruction == 0xBC:
        CP._0xBC(CPU)
    if instruction == 0xCC:
        CALL._0xCC(CPU)
    if instruction == 0xDC:
        CALL._0xDC(CPU)
    if instruction == 0x0D:
        DEC._0x0D(CPU)
    if instruction == 0x1D:
        DEC._0x1D(CPU)
    if instruction == 0x2D:
        DEC._0x2D(CPU)
    if instruction == 0x3D:
        DEC._0x3D(CPU)
    if instruction == 0x4D:
        LD._0x4D(CPU)
    if instruction == 0x5D:
        LD._0x5D(CPU)
    if instruction == 0x6D:
        LD._0x6D(CPU)
    if instruction == 0x7D:
        LD._0x7D(CPU)
    if instruction == 0x8D:
        ADC._0x8D(CPU)
    if instruction == 0x9D:
        SBC._0x9D(CPU)
    if instruction == 0xAD:
        XOR._0xAD(CPU)
    if instruction == 0xBD:
        CP._0xBD(CPU)
    if instruction == 0xCD:
        CALL._0xCD(CPU)
    if instruction == 0x0E:
        LD._0xE0(CPU)
    if instruction == 0x1E:
        LD._0x1E(CPU)
    if instruction == 0x2E:
        LD._0x2E(CPU)
    if instruction == 0x3E:
        LD._0x3E(CPU)
    if instruction == 0x4E:
        LD._0x4E(CPU)
    if instruction == 0x5E:
        LD._0x5E(CPU)
    if instruction == 0x6E:
        LD._0x6E(CPU)
    if instruction == 0x7E:
        LD._0x7E(CPU)
    if instruction == 0x8E:
        ADC._0x8E(CPU)
    if instruction == 0x9E:
        SBC._0x9E(CPU)
    if instruction == 0xAE:
        XOR._0xAE(CPU)
    if instruction == 0xBE:
        CP._0xBE(CPU)
    if instruction == 0xCE:
        ADC._0xCE(CPU)
    if instruction == 0xDE:
        SBC._0xDE(CPU)
    if instruction == 0xEE:
        XOR._0xEE(CPU)
    if instruction == 0xFE:
        CP._0xFE(CPU)
    if instruction == 0x0F:
        RRCA._0x0F(CPU)
    if instruction == 0x1F:
        RRCA._0x1F(CPU)
    if instruction == 0x2F:
        CPL._0x2F(CPU)
    if instruction == 0x3f:
        CCF._0x3F(CPU)
    if instruction == 0x4F:
        LD._0x4F(CPU)
    if instruction == 0x5F:
        LD._0x5F(CPU)
    if instruction == 0x6F:
        LD._0x6F(CPU)
    if instruction == 0x7F:
        LD._0x7F(CPU)
    if instruction == 0x8F:
        ADC._0x8F(CPU)
    if instruction == 0x9F:
        SBC._0x9F(CPU)
    if instruction == 0xAF:
        XOR._0xAF(CPU)
    if instruction == 0xBF:
        CP._0xBF(CPU)
    if instruction == 0xCF:
        RST._0xCF(CPU)
    if instruction == 0xDF:
        RST._0xDF(CPU)
    if instruction == 0xEF:
        RST._0xEF(CPU)
    if instruction == 0xFF:
        RST._0xFF(CPU)
    return