import warnings
# Silence the pysdl2-dll initialization warning
warnings.filterwarnings("ignore", category=UserWarning, message="Using SDL2 binaries from pysdl2-dll")
from pyboy import PyBoy
from input import commands, move, wait_frames
from gameinitial import gamestart, gamecontinue
from playerinfo import playerinfo
import io

pyboy = PyBoy("roms/Pokemon Red.gb", sound_volume=0)
pyboy.set_emulation_speed(1) 

print("load before")
with open("saved_state_test.state","rb") as f:
    pyboy.load_state(f)
print("loaded")
x = pyboy.memory[0xD362]
y = pyboy.memory[0xD361]
map_id = pyboy.memory[0xD35E]
direction = pyboy.memory[0xD52A]
print(f"after load {x, y, map_id, direction}") 

while pyboy.tick():

    pass
pyboy.stop()

