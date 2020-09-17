def _0x76(CPU):
    '''
    Power down CPU until an interrupt occurs. Use this
    when ever possible to reduce energy consumption.
    '''
    CPU.pc += 1
    CPU.mnemonic = "HALT"
    CPU.cycles = 4
