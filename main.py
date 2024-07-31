from typing import Optional


def calculation(left_value: int, input_value: tuple):
    left = input_value[0]
    right_value = input_value[1]
    if left == "+":
        return left_value + right_value
    elif left == "-":
        return left_value - right_value
    elif left == "*":
        return left_value * right_value
    elif left == "/":
        return (left_value // right_value) if left_value and right_value else 0
    raise Exception("invalid operation")


def zero(input_value: Optional[tuple] = None):
    if input_value:
        print(calculation(0, input_value))
    return 0


def one(input_value: Optional[tuple] = None):
    if input_value:
        print(calculation(1, input_value))
    return 1


def two(input_value: Optional[tuple] = None):
    if input_value:
        print(calculation(2, input_value))
    return 2


def three(input_value: Optional[tuple] = None):
    if input_value:
        print(calculation(3, input_value))
    return 3


def four(input_value: Optional[tuple] = None):
    if input_value:
        print(calculation(4, input_value))
    return 4


def five(input_value: Optional[tuple] = None):
    if input_value:
        print(calculation(5, input_value))
    return 5


def six(input_value: Optional[tuple] = None):
    if input_value:
        print(calculation(6, input_value))
    return 6


def seven(input_value: tuple = None):
    if input_value:
        print(calculation(7, input_value))
    return 7


def eight(input_value: Optional[tuple] = None):
    if input_value:
        print(calculation(8, input_value))
    return 8


def nine(input_value: Optional[tuple] = None):
    if input_value:
        print(calculation(9, input_value))
    return 9


def plus(value: int):
    return ("+", value)


def minus(value: int):
    return ("-", value)


def times(value: int):
    return ("*", value)


def divided_by(value: int):
    return ("/", value)
