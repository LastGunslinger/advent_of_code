from pathlib import Path
from typing import List, Set

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
            print(f'{box.id}: {len(box.point_array)}')
            results.append(
                box
            )
    return results


def check_intersections(boxes: List['Box']) -> Set[Point]:
    points = set()
    for index, box in enumerate(boxes[:-1]):
        for other_box in boxes[index + 1:]:
            intersections = box.intersection(other_box)
            points.update(intersections)
    return points


if __name__ == '__main__':
    boxes = make_boxes(Path.cwd() / '2018/day_3.txt')
    points = check_intersections(boxes)
    print(len(points))
