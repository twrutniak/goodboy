class CPU:
    def __init__(self):

        self.log = open("log.txt", "w")

        self.pc = 0x100
        self.stack = []
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

        self.flags = {
            "Z":0,
            "S":0,
            "HC":0,
            "C":0,
        }
    
    def write_log(self):
        log.write("{} {}   {}\n".format(hex(self.pc), hex(self.memory[self.pc]), self.mnemonic)



