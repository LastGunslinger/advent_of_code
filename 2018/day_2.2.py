from pathlib import Path
from typing import List


def string_diff(str_1: str, str_2: str) -> int:
    ''' Given two strings of equal length,
    return the number of different characters '''

    diff = 0
    for first, second in zip(str_1, str_2):
        if first != second:
            diff += 1
    return diff


def string_common(str_1: str, str_2: str) -> str:
    ''' Given two strings of equal length,
    return common characters '''

    common = ''
    for first, second in zip(str_1, str_2):
        if first == second:
            common += first
    return common


def compare_ids(input_data: List[str]) -> str:
    for first_id in input_data:
        for second_id in input_data:
            if string_diff(first_id, second_id) == 1:
                return string_common(first_id, second_id)


if __name__ == '__main__':
    input_path = Path.cwd() / '2018/day_2.txt'
    with open(input_path) as f:
        input_data = list(f.readlines())
    result = compare_ids(input_data)
    print(result)
