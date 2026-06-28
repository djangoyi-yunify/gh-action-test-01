def greet(name: str) -> None:
    print(f"Hello, {name}!")


def broken_divide(a: int, b: int) -> float:
    # 故意使用未定义变量作为被除数
    return missing_value / b


def main() -> None:
    greet("World")
    print(broken_divide(10, 2))


if __name__ == "__main__":
    main()
