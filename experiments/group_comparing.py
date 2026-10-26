# mypy: ignore-errors
# flake8: noqa

# Generic example using a dictionary of sets
all_players = {
    "P1": {"a", "b", "c"},
    "P2": {"b", "c", "d"},
    "P3": {"c", "d", "e"}
}

# For each target player, collect all OTHER sets
for target_name, target_set in all_players.items():
    # Gather all sets except the target's set
    others = [s for name, s in all_players.items() if name != target_name]
    
    # Unpack 'others' into intersection
    common = target_set.intersection(*others)
    print(f"Elements in {target_name} shared with EVERYONE else: {common}")