import random

names = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 
         'kevin', 'Liam']

names_cap = [name.capitalize() for name in names]
names_is_cap = [name for name in names if name.capitalize() == name]
names_dict = {key: random.randrange(100, 1000) for key in names_cap}
mean = sum(names_dict.values())/len(names_dict)
names_over_mean = {key:value for key, value in names_dict.items() if value > mean }

if __name__ == "__main__":

    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {names_cap}")
    print(f"New list of capitalized names only: {names_is_cap}")
    print(f"Score dict: {names_dict}")
    print(f"Score average is {mean:.2f}")
    print(f"High scores: {names_over_mean}")
