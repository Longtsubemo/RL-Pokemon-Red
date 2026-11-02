previous_position = None
previous_map_id = None
previous_direction = None

def playerinfo(pyboy):
    global previous_position, previous_map_id, previous_direction
    player_y = pyboy.memory[0xD361]
    player_x = pyboy.memory[0xD362]
    current_map_id = pyboy.memory[0xD35E]
    current_direction = pyboy.memory[0xD52A]
    if (player_x, player_y) != previous_position:
        print(f"Player position: X={player_x}, Y={player_y}")
        previous_position = (player_x, player_y)

    if current_map_id != previous_map_id:
        print(f"Current map id: {current_map_id}")
        previous_map_id = current_map_id

    if current_direction != previous_direction:
        if current_direction == 1:
            print(f"Player Direction: right")
            previous_direction = current_direction
        elif current_direction == 2:
            print(f"Player Direction: left")
            previous_direction = current_direction
        elif current_direction == 4:
            print(f"Player Direction: down")
            previous_direction = current_direction
        elif current_direction == 8:
            print(f"Player Direction: up")
            previous_direction = current_direction