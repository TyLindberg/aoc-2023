from typing import Final, List


DIGIT_STRINGS: Final[List[str]] = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def check_for_digit_string(char_buffer: str) -> str | None:
    if len(char_buffer) < 3:
        return None

    for i in range(10):
        if char_buffer.find(DIGIT_STRINGS[i]) != -1:
            return str(i)

    return None


def compute_calibration_value(line: str) -> int:
    left_digit = ""
    right_digit = ""

    char_buffer = ""

    for char in line:
        if left_digit != "":
            break

        if char.isdigit():
            left_digit = char

        char_buffer = f"{char_buffer}{char}"
        found_char = check_for_digit_string(char_buffer)
        if found_char is not None:
            left_digit = found_char

    char_buffer = ""

    for char in reversed(line):
        if right_digit != "":
            break

        if char.isdigit():
            right_digit = char

        # We reverse the order we add to the buffer here to
        char_buffer = f"{char}{char_buffer}"
        found_char = check_for_digit_string(char_buffer)
        if found_char is not None:
            right_digit = found_char

    return int(f"{left_digit}{right_digit}")


def main():
    acc = 0
    with open("1.txt", "r") as f:
        for line in f:
            acc += compute_calibration_value(line)

    print(acc)


if __name__ == "__main__":
    main()
