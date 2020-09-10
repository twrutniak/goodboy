def check_carry(val1, val2, datatype):
    if datatype == "8":
        val = val1 + val2
        if val > 0xff:
            val = val & 0xff
            flag = 1
        else:
            flag = 0
    elif datatype == "16":
        val = val1 + val2
        if val > 0xffff:
            val = val & 0xffff
            flag = 1
        else:
            flag = 0

    return val, flag

def check_halfcarry(val1, val2, datatype):
    if datatype == "8":
        val = ((val1 & 0xf) + (val2 & 0xf)) & 0x10
        if (val >> 4) == 1:
            flag = 1
        else:
            flag = 0
    if datatype == "16":
        val = ((val1 & 0xff) + (val2 & 0xff)) & 0x100
        if (val >> 8) == 1:
            flag = 1
        else:
            flag = 0
    
    return flag

def check_zero(val):
    if val == 0:
        return 1
    else:
        return 0

def _16bit_rw(self, registers, mode, val=None):
    if mode = "read":
        r1, r2 = list(registers)
        val = int((self.registers[r1] << 8) ^ self.registers[r2])
        if val <= 0xffff:
            return val
    elif mode="write":
        if val is not None:
            v1 = (val >> 8)
            v2 = (val ^ 0xff00)
            r1, r2 = list(registers)
            registers[r1] = v1
            registers[r2] = v2
            return
    else:
        pass