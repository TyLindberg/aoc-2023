def compute_calibration_value(line: str):
    left_digit = "0"
    right_digit = "0"

    for char in line:
        if char.isdigit():
            left_digit = char
            break

    for char in reversed(line):
        if char.isdigit():
            right_digit = char
            break

    return int(f"{left_digit}{right_digit}")


def main():
    acc = 0
    with open("1.txt", "r") as f:
        for line in f:
            acc += compute_calibration_value(line)

    print(acc)


if __name__ == "__main__":
    main()
