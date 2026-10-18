def get_player_pos() -> None:
    pos: list[str] = []
    while len(pos) != 3:
        pos = (input("Enter new coordinates as floats in format 'x,y,z': ")).split(",")
    print(pos)