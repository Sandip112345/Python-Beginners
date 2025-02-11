from typing import List, Union, Tuple, Dict


n : int = 5

name : str = "Sandip"


def sum(a: int, b: int) -> int:
    return a+b

print(sum(2,4))



# List of integers

number: List[int] = [1, 2, 3, 4, 5]


# Tuple of a string and an integer

person: Tuple[str, int] = ("Alice", 20)


# Dictionary with string keys and integer values

scores: Dict[str, int] = {"key": "value", "num": 24}

#Union type for variables that can hold multiple types

identifier: Union[int, str] = "ID123"

identifier = 12345 # also valid