from pyboy import PyBoy

pyboy = PyBoy("roms/Pokemon Red.gb")
pyboy.set_emulation_speed(1)

# Let the intro run for 10 seconds
pyboy.tick(1800)

# Now press Start
pyboy.button("start")
pyboy.tick()

while pyboy.tick():
    pass

pyboy.stop()