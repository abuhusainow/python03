# mypy: ignore-errors
# flake8: noqa

import random as rdm

lst = "sword,potion,shield,armor,helmet,sword".split(",")

def gen(lst) -> list:
    lst = rdm.choices(lst, k=10)
    for _ in lst:
        yield _

lst2 = gen(lst)

print(next(lst2))
print(next(lst2))
print(next(lst2))
print(next(lst2))
print(next(lst2))