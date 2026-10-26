# mypy: ignore-errors
# flake8: noqa

import math


def user_input() -> list:
    while True:
        while True:
            pos = [item.strip() for item in input("Ask for input: ").split(",")]
            if len(pos) == 3:
                break
            print("Invalid syntax")
        while True:
            for i in range(len(pos)):
                try:
                    pos[i] = float(pos[i])
                except ValueError:
                    print(
                        f"Error on parameter '{pos[i]}': could not convert",
                        f"string to float: '{pos[i]}'"
                    )
                break




print(user_input())
