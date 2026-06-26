def greet(name: str) -> None:
    """Greet the given name."""
    print(f"Hello, {name}!")


def farewell(name: str) -> None:
    """Say goodbye to the given name."""
    print(f"Goodbye, {name}!")


def main() -> None:
    greet("World")
    farewell("World")


if __name__ == "__main__":
    main()
