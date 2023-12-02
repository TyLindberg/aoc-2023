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


def check_for_digit_string(char_buffer: str) -> str:
    """
    Check for a string representation of a digit (e.g. "zero", "one", ..., or "nine") in the provided string

    Parameters
    ----------
    char_buffer : str
        The string to search for a digit within

    Returns
    -------
    str
        Digit as string (e.g. "0", "1", ..., "9") or "" if no digit was found
    """
    if len(char_buffer) < 3:
        return ""

    for i in range(10):
        if char_buffer.find(DIGIT_STRINGS[i]) != -1:
            return str(i)

    return ""


def find_digit(line: str, reverse: bool) -> str:
    """
    Find the first digit from a string, either character string or number

    Parameters
    ----------
    line : str
        A line from the calibration file (okay to have newline at the end)
    reverse : bool
        Whether or not to parse the string in reverse

    Returns
    -------
    str
        The digit as a string (e.g. "0", "1", ..., or "9")
    """
    found_digit = ""
    char_buffer = ""

    line_iter = line if not reverse else reversed(line)

    for char in line_iter:
        if found_digit != "":
            break

        char_buffer = f"{char_buffer}{char}" if not reverse else f"{char}{char_buffer}"
        # We check for this first to avoid overwriting the value found by the `isdigit` section
        found_digit = check_for_digit_string(char_buffer)

        if char.isdigit():
            found_digit = char

    return found_digit


def compute_calibration_value(line: str) -> int:
    """
    Return integer calibration value from a given line

    Parameters
    ----------
    line: str
        A line from the calibration file (okay to have newline at the end)

    Returns
    -------
    int
        The computed calibration value
    """
    left_digit = find_digit(line, reverse=False)
    right_digit = find_digit(line, reverse=True)

    return int(f"{left_digit}{right_digit}")


def main():
    acc = 0
    with open("1.txt", "r") as f:
        for line in f:
            acc += compute_calibration_value(line)

    print(acc)


if __name__ == "__main__":
    main()
