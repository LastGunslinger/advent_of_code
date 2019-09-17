'''
--- Day 6: Chronal Coordinates ---

The device on your wrist beeps several times, and once again you feel like you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9

If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.

This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf

Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?
'''

from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class Point:
    x: int
    y: int
    closest: List['Point'] = field(default_factory=list)

    def closest_point(self, other_points: List['Point']):
        distances = []

        for point in other_points:
            if self == point:
                continue

            distance = self.manhattan_distance(point)
            if distance != 0:
                distances.append(
                    (point, distance)
                )

        distances.sort(key=lambda x: x[1])
        self.closest = [x[0] for x in distances]

    def manhattan_distance(self, other: 'Point') -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))


def main(data):

    p1 = Point(1, 1)
    p2 = Point(1, 6)

    print(p1.manhattan_distance(p2))

    points = set()
    for line in data:
        line = line.strip()
        tokens = line.split(',')
        points.add(Point(
            x=int(tokens[0]),
            y=int(tokens[1])
        ))

    for point in points:

        point.closest_point(points)
        # print(point)

    return None


if __name__ == '__main__':
    filepath = Path.cwd() / '2018/day_6.txt'
    with open(filepath) as f:

        result = main(f.readlines())
        print(result)
