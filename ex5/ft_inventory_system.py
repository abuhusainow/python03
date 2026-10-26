import random
import typing

unique_actions = ["move", "grab", "use", "swim", "run", "climb", "release"]
unique_people = ["charlie", "dylan", "alice", "bob"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        a = random.choice(unique_people)
        b = random.choice(unique_actions)
        yield (a, b)


def consume_event(lst: list[tuple[str, str]]) -> typing.Generator[
        tuple[str, str], None, None]:
    while lst:
        yield lst.pop(random.randint(0, len(lst) - 1))


if __name__ == "__main__":
    lst: list[tuple[str, str]] = []
    for i in range(1000):
        a, b = next(gen_event())
        print(f"Event {i}: Player {a} did action {b}")

    for _ in range(10):
        lst.append(next(gen_event()))
    print(f"Built list of 10 events: {lst}")

    for event in consume_event(lst):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {lst}")
