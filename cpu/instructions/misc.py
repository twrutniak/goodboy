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

def convert_signed(val):
    if val > 127:
        return (256-val) * (-1)
    else:
        return val

def flip_bits(val):
    bitstr = '{0:b}'.format(val)
    flipped = ''
    for bit in bitstr:
        if bit == '1':
            flipped += 0
        else:
            flipped += 1
    return int(flipped, 2)