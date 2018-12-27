'''
--- Part Two ---
Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
'''

from pathlib import Path
import re


def compare_units(first: str, second: str) -> str:
    if first.lower() == second.lower() and first != second:
        return ''
    else:
        return first + second


def reduce_polymer(polymer: str) -> str:
    index = 0
    while index < len(polymer) - 1:
        comp = compare_units(polymer[index], polymer[index + 1])
        if comp:
            index += 1
        else:
            if index == 0:
                polymer = polymer[2:]
            elif index == len(polymer) - 2:
                polymer = polymer[:-2]
                index -= 1
            else:
                polymer = polymer[:index] + polymer[index + 2:]
                index -= 1

    return polymer


def main(data: str):
    # data = 'dabAcCaCBAcCcaDA'

    available_units = set(data.upper())

    polymer_dict = {}
    for unit in available_units:
        polymer = re.sub(unit, '', data, flags=re.IGNORECASE)
        # reduced_polymer = reduce_polymer(polymer)
        polymer_dict[unit] = reduce_polymer(polymer)

    return min([len(x) for x in polymer_dict.values()])


if __name__ == '__main__':
    filepath = Path.cwd() / '2018/day_5.txt'
    with open(filepath) as f:
        result = main(f.read())
        print(result)


