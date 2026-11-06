
from pyboy import PyBoy
from gameinitial import gamecontinue

ROM_PATH = "roms/Pokemon Red.gb"

pyboy = PyBoy(ROM_PATH, sound_volume=0)


def inspect_game():
    memory = pyboy.memory

    # Player coordinates
    x = memory[0xD362]
    y = memory[0xD361]

    # Player block coordinates
    x_block = memory[0xD364]
    y_block = memory[0xD363]

    # Current map
    map_id = memory[0xD35E]

    # 16-bit pointer to the visible map's upper-left corner
    pointer_low = memory[0xD35F]
    pointer_high = memory[0xD360]

    map_view_pointer = pointer_low | (pointer_high << 8)

    # Collision matrix
    collision = pyboy.game_wrapper.game_area_collision()

    print("\n" + "=" * 40)
    print("MAP ID:", map_id)
    print("PLAYER X:", x)
    print("PLAYER Y:", y)
    print("PLAYER X BLOCK:", x_block)
    print("PLAYER Y BLOCK:", y_block)
    print("MAP VIEW POINTER:", hex(map_view_pointer))

    print("\nCOLLISION SHAPE:", collision.shape)
    print("COLLISION MATRIX:")
    print(collision)
    print("=" * 40)
    print("SCX:", pyboy.memory[0xFF43])
    print("SCY:", pyboy.memory[0xFF42])

try:
    gamecontinue(pyboy)

    print("\nInitial game state:")
    inspect_game()

    directions = {
        "w": "up",
        "s": "down",
        "a": "left",
        "d": "right"
    }

    while True:
        command = input(
            "\nMove (W/A/S/D) or Q to quit: "
        ).lower()

        if command == "q":
            break

        if command not in directions:
            print("Invalid input")
            continue

        button = directions[command]

        pyboy.button(button, delay=16)
        pyboy.tick(16)

        inspect_game()

finally:
    pyboy.stop()
