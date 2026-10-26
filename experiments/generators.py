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

# from dualthread

def coroutine_beispiel():
    print("Start")
    while True:
        # Hier pausiert die Funktion und wartet auf Input
        wert = yield 
        print(f"Empfangen: {wert}")

co = coroutine_beispiel()
next(co)           # Initialisierung (bis zum ersten yield)
co.send("this is my message!")  # Die Coroutine nimmt den Wert entgegen und läuft weiter
co.send("also mine!")  # Die Coroutine nimmt den Wert entgegen und läuft weiter


def accumulator():
    total = 0
    while True:
        value = yield total  # Wert empfangen und Zustand zurückgeben
        if value is None: break
        total += value

gen = accumulator()
next(gen)          # Initialisierung (startet bis zum yield)
print(gen.send(10)) # 10
print(gen.send(20)) # 30