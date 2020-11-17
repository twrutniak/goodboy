from cpu.CPU import CPU, dispatch

emulator = CPU()
emulator.load_rom('tests/07-jr,jp,call,ret,rst.gb')

while True:
    if emulator.cycles != 0:
        emulator.log.write("Cycles: " + str(emulator.cycles) + "\n")
        emulator.cycles -= 1
    else:
        if emulator.memory[0xFF02] == 0x81:
            print(chr(emulator.memory[0xFF01]), end="")
            emulator.memory[0xFF02] = 0x0
        dispatch(emulator)