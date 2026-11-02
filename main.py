import warnings
# Silence the pysdl2-dll initialization warning
warnings.filterwarnings("ignore", category=UserWarning, message="Using SDL2 binaries from pysdl2-dll")
from pyboy import PyBoy
from input import commands, move, wait_frames
from gameinitial import gamestart, gamecontinue

pyboy = PyBoy("roms/Pokemon Red.gb", sound_volume=0)
pyboy.set_emulation_speed(1) 

gamecontinue(pyboy)
print(f"x pos = {pyboy.memory[0xD361]}") # x
print(f"y pos = {pyboy.memory[0xD362]}") # y
print(f"current map id = {pyboy.memory[0xD35E]}") # current map id
#gamestart(pyboy)

previous_position = None
previous_map_id = None

while pyboy.tick():
    player_y = pyboy.memory[0xD361]
    player_x = pyboy.memory[0xD362]
    current_map_id = pyboy.memory[0xD35E]
    if (player_x, player_y) != previous_position:
        print(f"Player position: X={player_x}, Y={player_y}")
        previous_position = (player_x, player_y)
    if current_map_id !=previous_map_id:
        print(f"Current map id: {current_map_id}")
        previous_map_id = current_map_id
    pass

pyboy.stop()

