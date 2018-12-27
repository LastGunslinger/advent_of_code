'''
--- Part Two ---

Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?
'''
from pathlib import Path
from typing import List, Set, Optional
from collections import defaultdict

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class Box:
    id: int
    point: Point
    width: int
    height: int
    point_array: Set[Point] = field(default_factory=set)

    def __post_init__(self):
        for y in range(self.point.y, self.point.y + self.height):
            for x in range(self.point.x, self.point.x + self.width):
                self.point_array.add(
                    Point(x=x, y=y)
                )

    def intersection(self, other: 'Box') -> Set[Point]:
        if self == other:
            return set()
        return self.point_array.intersection(other.point_array)


def make_boxes(path: Path) -> dict:
    results = []
    with open(path) as f:
        for line in f.readlines():
            tokens = line.split()
            box_id = int(tokens[0][1:])

            x = int(tokens[2].split(',')[0])
            y = int(tokens[2].split(',')[1][:-1])

            width = int(tokens[3].split('x')[0])
            height = int(tokens[3].split('x')[1])
            box = Box(
                id=box_id,
                point=Point(x=x, y=y),
                width=width,
                height=height
            )
            results.append(
                box
            )
    return results


def check_intersections(boxes: List['Box']) -> Optional['Box']:
    points = defaultdict(int)
    for box in boxes:
        for other_box in boxes:
            intersections = box.intersection(other_box)
            points[box.id] += len(intersections)
        if points[box.id] == 0:
            return box
    else:
        return None


if __name__ == '__main__':
    boxes = make_boxes(Path.cwd() / '2018/day_3.txt')
    box = check_intersections(boxes)
    print(box)

