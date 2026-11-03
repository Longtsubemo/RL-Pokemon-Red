import numpy as np

previous_position = None
previous_map_id = None
previous_direction = None
previous_collision = None

DIRECTIONS = {
    1: "right",
    2: "left",
    4: "down",
    8: "up"
}


def playerinfo(pyboy):
    global previous_position, previous_map_id
    global previous_direction, previous_collision

    player_y = pyboy.memory[0xD361]
    player_x = pyboy.memory[0xD362]
    current_map_id = pyboy.memory[0xD35E]
    current_direction = pyboy.memory[0xD52A]

    current_collision = pyboy.game_wrapper.game_area_collision()

    if (player_x, player_y) != previous_position:
        print(f"Player position: X={player_x}, Y={player_y}")
        previous_position = (player_x, player_y)

    if current_map_id != previous_map_id:
        print(f"Current map ID: {current_map_id}")
        previous_map_id = current_map_id

    if current_direction != previous_direction:
        direction = DIRECTIONS.get(current_direction, "unknown")
        print(f"Player direction: {direction}")
        previous_direction = current_direction

    if previous_collision is None or not np.array_equal(
        current_collision, previous_collision
    ):
        print("Collision changed:")
        print(current_collision)
        previous_collision = current_collision.copy()