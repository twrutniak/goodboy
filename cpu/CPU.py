from .dispatcher import dispatch

class CPU:
    def __init__(self):

        self.log = open("log.txt", "w")

        self.pc = 0x100
        self.stack = []
        self.memory = [0] * 0xFFFF
        self.memory[0x100] = 0x53
        self.cycles = 0
        self.mnemonic = ""
        self.instruction = ""

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

        self.registers["E"] = 6

        self.flags = {
            "Z":0,
            "S":0,
            "HC":0,
            "C":0,
        }

        self.log.write('CPU initialized.\n')
    
    def load_rom(self, rom_path):
        self.log.write("Loading %s..." % rom_path)
        binary = open(rom_path, "rb").read()
        i = 0
        while i < len(binary):
            self.memory[i] = ord(binary[i])
            i += 1

    def write_log(self):
        self.log.write("\nPC: {} instruction: {}   mnemonic: {}\n{}\n".format(hex(self.pc), hex(self.memory[self.pc]), self.mnemonic, str(self.registers)))