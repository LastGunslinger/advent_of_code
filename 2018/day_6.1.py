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
import operator
from dataclasses import dataclass, field
from typing import Set
from collections import defaultdict


@dataclass
class Point:
    x: int = field(default_factory=int)
    y: int = field(default_factory=int)

    def _distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def closest_point(self, points: Set['Point']):
        min_distance = 0
        closest = self

        for point in points:
            if self == point:
                return point, 0

            distance = self._distance(point)
            if min_distance == 0 or distance < min_distance:
                min_distance = distance
                closest = point
            elif distance == min_distance:
                return None, 0

        return closest, min_distance

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        origin = Point(0, 0)
        return origin._distance(self) < origin._distance(other)

    def __gt__(self, other):
        origin = Point(0, 0)
        return origin._distance(self) > origin._distance(other)


def main(data: str):

    points_of_interest = set(
        Point(int(p.split(',')[0]), int(p.split(',')[1])) for p in data
    )

    all_points = set()
    min_x = min(p.x for p in points_of_interest)
    min_y = min(p.y for p in points_of_interest)
    max_x = max(p.x for p in points_of_interest)
    max_y = max(p.y for p in points_of_interest)
    distance_dict = defaultdict(int)

    # The points that have x or y values matching the min and max x and y values are defacto infinite

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            p = Point(x, y)
            all_points.add(p)

    for point in all_points:
        closest, distance = point.closest_point(points_of_interest)
        if not closest:
            distance_dict[point] += 1
        elif closest.x == min_x or closest.x == max_x:
            continue
        elif closest.y == min_y or closest.y == max_y:
            continue
        else:
            distance_dict[closest] += 1

            # print(f'{point} is closest to {closest} at {distance} meters')

    # print(sorted(list(all_points)))

    # print(distance_dict[Point(3, 4)])
    # print(distance_dict[Point(5, 5)])
    return max(distance_dict, key=distance_dict.get), max(distance_dict.values())


if __name__ == '__main__':
    filepath = Path.cwd() / '2018/day_6.txt'

    with open(filepath) as f:
        data = [x.strip() for x in f.readlines()]

    result = main(data)
    print(f'Result: {result}')

