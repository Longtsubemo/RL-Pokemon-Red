import numpy as np
def get_observation(pyboy):
    collision = pyboy.game_wrapper.game_area_collision()
    game_area = pyboy.game_wrapper.game_area()
    x = np.array([pyboy.memory[0xD362]], dtype=np.uint8)
    y = np.array([pyboy.memory[0xD361]], dtype=np.uint8)
    map_id = np.array([pyboy.memory[0xD35E]], dtype= np.uint8)
    direction = np.array([pyboy.memory[0xD52A]], dtype= np.uint8)

    return {
    "collision": collision,
    "game_area": game_area,
    "x" : x,
    "y" : y,
    "map_id" : map_id,
    "direction" : direction
}