from pathlib import Path
from collections import defaultdict


def letter_count(word: str) -> defaultdict:
    word_dict = defaultdict(lambda: 0)
    for letter in word:
        word_dict[letter] += 1
    return word_dict


def n_duplicates(word: str, n: int) -> bool:
    word_dict = letter_count(word)
    for letter, count in word_dict.items():
        if count == n:
            return True
    else:
        return False


def checksum(input_path: Path) -> int:
    with open(input_path) as f:
        input_values = list(f.readlines())
    
    two_letters = 0
    two_letters = sum(n_duplicates(x, 2) for x in input_values)
    three_letters = 0
    three_letters = sum(n_duplicates(x, 3) for x in input_values)

    return two_letters * three_letters


if __name__ == '__main__':
    cs = checksum(Path.cwd() / '2018/day_2.txt')
    print(cs)
