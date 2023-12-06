import re
from typing import Final, Pattern


COLORS: Final = ["red", "green", "blue"]
GAME_PARAMS: Final = {"red": 12, "green": 13, "blue": 14}
CUBE_REGEXES: Final = {
    "red": re.compile("(\\d+) red"),
    "green": re.compile("(\\d+) green"),
    "blue": re.compile("(\\d+) blue"),
}


def get_cube_num(grab_string: str, regex: Pattern) -> int:
    match = regex.search(grab_string)
    return 0 if match is None else int(match.group(1))


def is_grab_valid(grab_string: str) -> bool:
    return all(
        get_cube_num(grab_string, CUBE_REGEXES[color]) <= GAME_PARAMS[color]
        for color in COLORS
    )


def is_game_valid(game_string: str) -> bool:
    # It's okay to leave the "Game: X" text in the beginning since we're searching anyways
    grabs = game_string.split(";")
    return all(is_grab_valid(grab_string) for grab_string in grabs)


def main():
    with open("input.txt", "r") as input:
        print(
            sum(
                index + 1  # We add one here since the file starts with Game 1
                for index, line in enumerate(input)
                if is_game_valid(line.rstrip())
            )
        )


if __name__ == "__main__":
    main()
