
from pyboy import PyBoy
from gameinitial import gamecontinue
import numpy as np

ROM_PATH = "roms/Pokemon Red.gb"

pyboy = PyBoy(ROM_PATH, sound_volume=0)

DIRECTIONS = {
    "w": "up",
    "s": "down",
    "a": "left",
    "d": "right"
}


def get_player_position():
    return (
        pyboy.memory[0xD35E],  # Map ID
        pyboy.memory[0xD362],  # Player X
        pyboy.memory[0xD361]   # Player Y
    )


def get_camera_position():
    return {
        "SCX": pyboy.memory[0xFF43],
        "SCY": pyboy.memory[0xFF42]
    }


def get_collision():
    return pyboy.game_wrapper.game_area_collision().copy()


def inspect_state(label):
    print("\n" + "=" * 50)
    print(label)
    print("=" * 50)

    print("Player position:", get_player_position())
    print("Player direction:", pyboy.memory[0xD52A])
    print("Camera:", get_camera_position())

    collision = get_collision()

    print("Collision shape:", collision.shape)
    print("Collision matrix:")
    print(collision)

    return collision


try:
    gamecontinue(pyboy)

    print("\nControls:")
    print("W = Up")
    print("S = Down")
    print("A = Left")
    print("D = Right")
    print("Q = Quit")

    inspect_state("INITIAL STATE")

    while True:
        command = input("\nMove (W/A/S/D) or Q: ").lower().strip()

        if command == "q":
            break

        if command not in DIRECTIONS:
            print("Invalid input")
            continue

        previous_position = get_player_position()
        previous_camera = get_camera_position()
        previous_collision = get_collision()

        button = DIRECTIONS[command]

        print("\nAction:", button)

        pyboy.button(button, delay=16)
        pyboy.tick(32)

        print("\n--- AFTER INPUT (32 FRAMES) ---")
        print("Position:", get_player_position())
        print("Camera:", get_camera_position())

        # Advance the game without pressing another button
        pyboy.tick(16)

        print("\n--- AFTER WAITING (16 MORE FRAMES) ---")
        print("Position:", get_player_position())
        print("Camera:", get_camera_position())

        current_position = get_player_position()
        current_camera = get_camera_position()
        current_collision = get_collision()
        current_camera = get_camera_position()
        current_collision = get_collision()

        print("\n--- MOVEMENT COMPARISON ---")
        print("Previous position:", previous_position)
        print("Current position: ", current_position)
        print("Position changed:  ", previous_position != current_position)

        print("\n--- CAMERA COMPARISON ---")
        print("Previous camera:", previous_camera)
        print("Current camera: ", current_camera)
        print("Camera changed:  ", previous_camera != current_camera)

        print("\n--- COLLISION COMPARISON ---")
        print(
            "Collision changed:",
            not np.array_equal(previous_collision, current_collision)
        )

        print("\n--- CURRENT STATE ---")
        print("Player direction:", pyboy.memory[0xD52A])
        print("Collision matrix:")
        print(current_collision)

finally:
    pyboy.stop()
