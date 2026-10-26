# mypy: ignore-errors
# flake8: noqa

def test_generator(n):
    for _ in range(10):
        print("ok, lets see")
        yield 
        print("first print")


test = test_generator(10)

next(test)
next(test)



