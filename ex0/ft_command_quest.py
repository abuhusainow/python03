import sys


def ft_sys_calls(sys_input: list[str]) -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys_input[0]}")
    if len(sys_input) <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys_input)-1}")

    for i in range(1, len(sys_input)):
        print(f"Argument {i}: {sys_input[i]}")

    print(f"Total arguments: {len(sys_input)}")


''' # Alternative Method:
def ft_sys_calls2(sys_input: list[str]) -> None:
    print("=== Command Quest ===")
    name, *lst = sys_input
    if lst:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(lst)}")

    for i in range(len(lst)):
        print(f"Argument {i}: {lst[i]}")
    print(f"Total arguments: {len(sys_input)}")
'''

if __name__ == "__main__":
    ft_sys_calls(sys.argv)
#   ft_sys_calls2(sys.argv)
