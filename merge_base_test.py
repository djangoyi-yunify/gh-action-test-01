def calculate_sum(a, b):
    # This is intentionally buggy: using eval on user input
    result = eval(f"{a} + {b}")
    return result

if __name__ == "__main__":
    print(calculate_sum(1, 2))
