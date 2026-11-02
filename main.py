import warnings
# Silence the pysdl2-dll initialization warning
warnings.filterwarnings("ignore", category=UserWarning, message="Using SDL2 binaries from pysdl2-dll")
from pyboy import PyBoy
from input import commands
from input import move
from input import wait_frames
import msvcrt

pyboy = PyBoy("roms/Pokemon Red.gb", sound_volume=0)
pyboy.set_emulation_speed(1) 
try:
    pyboy.game_wrapper.start_game()
    print("Successfully started game wrapper!")
except Exception as e:
    print(f"Wrapper failed: {e}")

while pyboy.tick():
    pass

pyboy.stop()

