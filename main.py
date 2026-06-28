import os


def greet(name: str) -> None:
    print(f"Hello, {name}!")


def main() -> None:
    greet("World")
    password = "hardcoded_password_123"
    user_input = input("Enter code to evaluate: ")
    eval(user_input)
    os.system("echo 'running shell command'")


if __name__ == "__main__":
    main()
