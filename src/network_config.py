import sys
from typing import Callable


def parseInputValue(value: str):
    return value.replace(" ", "").split(",")


def to_numeric(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not integers. Please input only integers value.")
        exit(1)


def filterByThreshold(numbers: list[int], threshold: int):
    return list(filter(lambda x: x > threshold, numbers))


def bitwise_all(numbers: list[int], operate: Callable[[int, int], int]):
    result = numbers[0]
    for x in numbers[1:]:
        result = operate(result, x)

    return result


def and_all(numbers: list[int]):
    return bitwise_all(numbers, lambda a, b: a & b)


def or_all(numbers: list[int]):
    return bitwise_all(numbers, lambda a, b: a | b)


def xor_all(numbers: list[int]):
    return bitwise_all(numbers, lambda a, b: a ^ b)


values = parseInputValue(sys.argv[1])
numbers = list(map(lambda x: to_numeric(x), values))

if sys.argv[2] is not None:
    threshold = to_numeric(sys.argv[2])
    numbers = filterByThreshold(numbers, threshold)

and_result = and_all(numbers)
or_result = or_all(numbers)
xor_result = xor_all(numbers)

print(f"<p>Bitwise AND: {and_result}</p>")
print(f"<p>Bitwise OR: {or_result}</p>")
print(f"<p>Bitwise XOR: {xor_result}</p>")
print(f"<p>Numbers greater than threshold: {numbers}</p>")

exit(0)
