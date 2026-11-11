def get_observation(pyboy):
    collision = pyboy.game_wrapper.game_area_collision()
    game_area = pyboy.game_wrapper.game_area()
    x = pyboy.memory[0xD362]
    y = pyboy.memory[0xD361]
    map_id = pyboy.memory[0xD35E]
    direction = pyboy.memory[0xD52A]

    return {
    "collision": collision,
    "game_area": game_area,
    "x" : x,
    "y" : y,
    "map_id" : map_id,
    "direction" : direction
}