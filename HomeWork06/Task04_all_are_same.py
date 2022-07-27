from typing import Callable


def same_by(characteristics: Callable, objects: list) -> bool:
    return len(set(map(characteristics, objects))) == 1


values = [0, 2, 10, 6, 6]

print(('different', 'same')[same_by(lambda x: x % 2, values)])
