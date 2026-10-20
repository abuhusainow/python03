import math


def get_player_pos() -> tuple[float, float, float]:
    prompt = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        user_pos = [item.strip() for item in input(prompt).split(",")]

        valid = True
        if len(user_pos) == 3:
            for pos in user_pos:
                try:
                    float(pos)
                except ValueError:
                    print(
                        f"Error on parameter '{pos}': could not convert",
                        f"string to float: '{pos}'"
                    )
                    valid = False
                    break
            if valid:
                x, y, z = [float(pos) for pos in user_pos]
                return (x, y, z)
        else:
            print("Invalid syntax")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")
    dist1 = math.sqrt(
        first_pos[0] ** 2 + first_pos[1] ** 2 + first_pos[2] ** 2
        )
    print(f"Distance to center: {dist1:.4f}")
    print()

    print("Get a second set of coordinates")
    sec_pos = get_player_pos()
    dist2 = math.sqrt(
        (sec_pos[0] - first_pos[0]) ** 2 +
        (sec_pos[1] - first_pos[1]) ** 2 +
        (sec_pos[2] - first_pos[2]) ** 2)
    print(f"Distance between the 2 sets of coordinates: {dist2:.4f}")
