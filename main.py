def greet(name: str) -> None:
    print(f"Hello, {name}!")


def main() -> None:
    greet("World")
    pwd = "super_secret_123"
    user_code = input("code: ")
    eval(user_code)


if __name__ == "__main__":
    main()
