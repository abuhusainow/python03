# mypy: ignore-errors
# flake8: noqa

notemptylst = ["a","b","c",1,2,3,4]
emptylst = []

print(bool(notemptylst))

if notemptylst:
    print("this list is NOT empty")

if emptylst:
    print("this is empty - thats why its not printing this message")