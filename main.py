def greet(name: str) -> None:
    print(f"Hello, {name}!")


def buggy_sum(a: int, b: int) -> int:
    # 故意引入未定义变量错误
    return a + b + undefined_magic_number


def main() -> None:
    greet("World")
    print(buggy_sum(1, 2))


if __name__ == "__main__":
    main()
