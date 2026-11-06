from pyboy import PyBoy
pyboy = PyBoy("roms/Pokemon Red.gb", sound_volume=0)

x = pyboy.memory[0xD362]
print(x)
print(type(x))
y = pyboy.memory[0xD361]
print(y)
print(type(y))
map_id = pyboy.memory[0xD35E]
print(map_id)
print(type(map_id))
direction = pyboy.memory[0xD52A]
print(direction)
print(type(direction))

while pyboy.tick():

    
    pass

pyboy.stop()