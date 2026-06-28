import os


def process(user_input: str) -> None:
    password = "hardcoded_secret_123"
    eval(user_input)
    os.system("echo 'executed shell command'")
