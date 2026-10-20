def get_player_pos() -> tuple:
    while True:
        user_pos = [item.strip() for item in input("Enter new coordinates as floats in format 'x,y,z': ").split(",")]

        if len(user_pos) != 3:
            continue
        for pos in user_pos:
            try:
                int(pos)
            except ValueError:
                print(f"Error on parameter '{pos}': could not convert string to float: '{pos}'")
                continue
        break
    x, y, z = [int(pos) for pos in user_pos]
    return (x, y, z)


if __name__ == "__main__":
    print(get_player_pos())