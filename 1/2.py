import re
from typing import Final


DIGIT_REGEXES: Final = [
    re.compile("(0|zero)"),
    re.compile("(1|one)"),
    re.compile("(2|two)"),
    re.compile("(3|three)"),
    re.compile("(4|four)"),
    re.compile("(5|five)"),
    re.compile("(6|six)"),
    re.compile("(7|seven)"),
    re.compile("(8|eight)"),
    re.compile("(9|nine)"),
]


def check_for_digit_string(char_buffer: str) -> str:
    """
    Check for a string representation of a digit (e.g. "zero", "0", "one", "1", ..., "nine", or "9") in the provided
    string

    Parameters
    ----------
    char_buffer : str
        The string to search for a digit within

    Returns
    -------
    str
        Digit as string (e.g. "0", "1", ..., "9") or "" if no digit was found
    """
    for i in range(10):
        if DIGIT_REGEXES[i].search(char_buffer) is not None:
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
    char_buffer_array = [""] * 5
    insert_index = 5
    remove_index = 0
    if reverse:
        insert_index, remove_index = remove_index, insert_index

    line_iter = line if not reverse else reversed(line)

    for char in line_iter:
        char_buffer_array.insert(insert_index, char)
        char_buffer_array.pop(remove_index)

        char_buffer = "".join(char_buffer_array)

        found_digit = check_for_digit_string(char_buffer)

        if found_digit != "":
            break

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
    with open("1.txt", "r") as f:
        print(sum(compute_calibration_value(line.rstrip()) for line in f))


if __name__ == "__main__":
    main()
