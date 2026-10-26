# mypy: ignore-errors
# flake8: noqa

set1 = set(range(0,5))
set2 = set(range(1,6))
set3 = set(range(2,7))

print("Union:", set1.union(set2))
print("Inter:", set1.intersection(set2))
print("Diff:", set1.difference(set2))
print("Diff:", set1.symmetric_difference(set2))
print((set2 | set3 | set1) - set1)
print(set1.union(set1,set2,set3).difference(set1))