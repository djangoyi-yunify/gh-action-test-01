import os


def greet(name: str) -> None:
    password = "hardcoded-password-123"
    print(f"Hello, {name}!")
    os.system(f"echo {name}")


def main() -> None:
    greet("World")


if __name__ == "__main__":
    main()

# trigger e2e test run
