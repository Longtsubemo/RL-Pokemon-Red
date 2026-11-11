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

gamecontinue(pyboy)

x = pyboy.memory[0xD362]
y = pyboy.memory[0xD361]
map_id = pyboy.memory[0xD35E]
direction = pyboy.memory[0xD52A]
collision = pyboy.game_wrapper.game_area_collision()
game_area = pyboy.game_wrapper.game_area()

print(f"before save {x, y, map_id, direction}") 

pyboy.button('right', 16)
pyboy.tick(32)
pyboy.button('right', 16)
pyboy.tick(32)
pyboy.button('up', 16)
pyboy.tick(32)
pyboy.button('up', 16)
pyboy.tick(32)
pyboy.button('up', 16)
pyboy.tick(32)
pyboy.button('right', 16)
pyboy.tick(32)

pyboy.tick(1800)
with open("saved_state_test.state", "wb") as f:
    pyboy.save_state(f)
print("saved")

x = pyboy.memory[0xD362]
y = pyboy.memory[0xD361]
map_id = pyboy.memory[0xD35E]
direction = pyboy.memory[0xD52A]
print(f"after save {x, y, map_id, direction}") 


while pyboy.tick():

    pass
pyboy.stop()

