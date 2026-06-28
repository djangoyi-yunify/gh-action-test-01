def greet(name: str) -> None:
    print(f"Hello, {name}!")


def buggy_sum(a: int, b: int) -> int:
    return a + b + undefined_magic_number


def main() -> None:
    greet("World")
    result = buggy_sum(1, 2)
    print(result)


if __name__ == "__main__":
    main()
