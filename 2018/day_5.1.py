'''
--- Day 5: Alchemical Reduction ---
You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress, but are still struggling with the suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

For example:

In aA, a and A react, leaving nothing behind.
In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
In abAB, no two adjacent units are of the same type, and so nothing happens.
In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.
After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned? (Note: in this puzzle and others, the input is large; if you copy/paste your input, make sure you get the whole thing.)
'''

from pathlib import Path


def compare_units(first: str, second: str) -> str:
    if first.lower() == second.lower() and first != second:
        return ''
    else:
        return first + second


def main(data: str):
    # data = 'dabAcCaCBAcCcaDA'
    history = [data]

    index = 0
    while index < len(data) - 1:
        comp = compare_units(data[index], data[index + 1])
        if comp:
            index += 1
        else:
            history.append(data)
            if index == 0:
                data = data[2:]
            elif index == len(data) - 2:
                data = data[:-2]
                index -= 1
            else:
                data = data[:index] + data[index + 2:]
                index -= 1

    print(data)
    print(f'Solution found in {len(history)} iterations.')
    # PrettyPrinter().pprint(history)
    return len(data)


if __name__ == '__main__':
    filepath = Path.cwd() / '2018/day_5.txt'
    with open(filepath) as f:
        result = main(f.read())
        print(result)


