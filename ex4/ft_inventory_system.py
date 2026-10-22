import sys


def ft_inventory_system(sys_input: list[str]) -> dict:
    inventory: dict[str, float] = {}
    for item in sys_input[1:]:
        try:
            key, value, *_ = [var.strip() for var in item.split(":")]
        except ValueError:
            print(f"Error - invalid parameter '{key}'")
            continue
        if key not in inventory.keys():
            try:
                inventory[key] = int(value)
            except ValueError as e:
                print(f"Quantity error for 'key': '{e}'")
            continue
        else:
            print(f"Redundant item '{key}' - discarding")
    return inventory


print(ft_inventory_system(sys.argv))
