import warnings
# Silence the pysdl2-dll initialization warning
warnings.filterwarnings("ignore", category=UserWarning, message="Using SDL2 binaries from pysdl2-dll")
from pyboy import PyBoy
from input import commands, move, wait_frames
from gameinitial import gamestart, gamecontinue

pyboy = PyBoy("roms/Pokemon Red.gb", sound_volume=0)
pyboy.set_emulation_speed(0) 

gamecontinue(pyboy)
#gamestart(pyboy)

while pyboy.tick():
    pass

pyboy.stop()

