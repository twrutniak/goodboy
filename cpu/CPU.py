from .dispatcher import dispatch
from random import randint

class CPU:
    def __init__(self):

        self.log = open("log.txt", "w")

        self.pc = 0x100
        self.sp = 0xFFFF
        self.stack = []
        self.memory = [0] * 0x10000
        self.memory[0xFF44] = 144
        self.cycles = 0
        self.enable_interrupts = True
        self.instruction = ""
        self.logging = True
        self.last_write = 0

        self.registers = {
            "A":0,
            "B":0, 
            "C":0,
            "D":0, 
            "E":0,
            "F":0, 
            "H":0,
            "L":0, 
        }

        self.flags = {
            "Z":0,
            "N":0,
            "HC":0,
            "C":0,
        }

        self.log.write('CPU initialized.\n')
    
    def push_stack(self, val):
        self.sp -= 1
        self.memory[self.sp] = val
        return self.sp

    def pop_stack(self):
        val = self.memory[self.sp]
        self.memory[self.sp] = 0
        self.sp += 1
        return val    

    def load_rom(self, rom_path):
        self.log.write("Loading %s..." % rom_path)
        binary = open(rom_path, "rb").read()
        i = 0
        while i < len(binary):
            self.memory[i] = binary[i]
            i += 1

    def write_log(self, mnemonic):
        if self.logging:
            self.log.write("\nPC: {} instruction: {}   mnemonic: {}\n{}\n{}\n".format(hex(self.pc), hex(self.memory[self.pc]), mnemonic, str(self.registers), str(self.flags)))
        else:
            return