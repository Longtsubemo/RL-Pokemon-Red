from pyboy import PyBoy

pyboy = PyBoy("roms/Pokemon Red.gb", sound_volume=0)
pyboy.set_emulation_speed(0) 

with open("roms/Pokemon Red.gb.state","rb") as f:
    pyboy.load_state(f)

while pyboy.tick():
    pass
pyboy.stop()
