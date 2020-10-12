from cpu.CPU import CPU, dispatch

emulator = CPU()
#emulator.load_rom('rom.gb')

while True:
    if emulator.cycles != 0:
        emulator.log.write("Cycles: " + str(emulator.cycles) + "\n")
        emulator.cycles -= 1
    else:
        emulator.write_log()
        dispatch(emulator)