import sys


def ft_inventory_system(sys_input: list[str]) -> dict:
    inventory: dict[str, int] = {}
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


def update_intory(inventory: dict[str, int], item: str, qty: int) -> None:
    inventory.update({item: qty})
    print(f"Updated inventory: {list(inventory)}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inv_dict = ft_inventory_system(sys.argv)
    print(f"Got inventory: {inv_dict}")
    print(f"Item list: {list(inv_dict.keys())}")
    sum_val = sum(inv_dict.values())
    print(
        f"Total quantity of the {len(inv_dict.keys())} items:",
        f"{sum_val}"
    )

    for key, val in inv_dict.items():
        print(f"Item {key} represents {(val/sum_val):.1%}")

    most_item = ""
    most_qty = 0
    least_item = ""
    least_qty = 0

    for item, qty in inv_dict.items():
        if most_item == "" or qty > most_qty:
            most_item = item
            most_qty = qty
        if least_item == "" or qty < least_qty:
            least_item = item
            least_qty = qty

    print(
        f"Item most abundant: {most_item}",
        f"with quantity {most_qty}"
    )
    print(
        f"Item most abundant: {least_item}",
        f"with quantity {least_qty}"
    )
    update_intory(inv_dict, "magic_item", 1)