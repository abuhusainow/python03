import random as rdm


def gen_player_achievements() -> set:

    ACHIEVEMENTS = [
        "Boss Slayer",
        "Collector Supreme",
        "Crafting Genius",
        "First Steps",
        "Hidden Path Finder",
        "Master Explorer",
        "Sharp Mind",
        "Speed Runner",
        "Strategist",
        "Survivor",
        "Treasure Hunter",
        "Unstoppable",
        "Untouchable",
        "World Savior",
    ]

    return set(rdm.sample(ACHIEVEMENTS, k=rdm.randrange(1, len(ACHIEVEMENTS))))


def main_function() -> None:
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    p_achiev = [gen_player_achievements() for _ in players]
    print("=== Achievement Tracker System ===", end="\n\n")

    for i in range(len(players)):
        print(f"Player {players[i]}: {p_achiev[i]}")
    print()
    print(f"All distinct achievements: {p_achiev[0].union(*p_achiev)}")
    print()
    print(f"Common achievements: {p_achiev[0].intersection(*p_achiev)}")
    print()
    for i in range(len(players)):
        print(f"Only {players[i]} has:",
              f"{p_achiev[i].difference(*p_achiev[:i], *p_achiev[i+1:])}")
    print()
    for i in range(len(players)):
        print(f"{players[i]} is missing:",
              f"{p_achiev[i].union(*p_achiev).difference(p_achiev[i])}")


if __name__ == "__main__":
    main_function()
