from typing import Optional


def calculation(left_value: int, input_value: tuple) -> int:
    operation = input_value[0]
    right_value = input_value[1]
    if operation == "+":
        return left_value + right_value
    elif operation == "-":
        return left_value - right_value
    elif operation == "*":
        return left_value * right_value
    elif operation == "/":
        if right_value:
            return left_value // right_value
        raise Exception("division by zero")
    raise Exception("invalid operation")


def zero(input_value: Optional[tuple] = None) -> Optional[int]:
    """
    >>> zero(plus(zero()))
    0
    >>> zero(minus(zero()))
    0
    >>> zero(times(zero()))
    0
    >>> zero(divided_by(two()))
    0
    >>> zero(divided_by(zero()))
    Traceback (most recent call last):
        ...
    Exception: division by zero
    """
    return calculation(0, input_value) if input_value else 0


def one(input_value: Optional[tuple] = None) -> Optional[int]:
    """
    >>> one(plus(one()))
    2
    >>> one(plus(eight()))
    9
    """
    return calculation(1, input_value) if input_value else 1


def two(input_value: Optional[tuple] = None) -> Optional[int]:
    """
    >>> two()
    2
    """
    return calculation(2, input_value) if input_value else 2


def three(input_value: Optional[tuple] = None) -> Optional[int]:
    """
    >>> three()
    3
    """
    return calculation(3, input_value) if input_value else 3


def four(input_value: Optional[tuple] = None) -> Optional[int]:
    """
    >>> four(times(five()))
    20
    """
    return calculation(4, input_value) if input_value else 4


def five(input_value: Optional[tuple] = None) -> Optional[int]:
    """
    >>> five()
    5
    """
    return calculation(5, input_value) if input_value else 5


def six(input_value: Optional[tuple] = None) -> Optional[int]:
    """
    >>> six()
    6
    """
    return calculation(6, input_value) if input_value else 6


def seven(input_value: Optional[tuple] = None) -> Optional[int]:
    """
    >>> seven(minus(three()))
    4
    """
    return calculation(7, input_value) if input_value else 7


def eight(input_value: Optional[tuple] = None) -> Optional[int]:
    """
    >>> eight()
    8
    """
    return calculation(8, input_value) if input_value else 8


def nine(input_value: Optional[tuple] = None) -> Optional[int]:
    """
    >>> nine(divided_by(three()))
    3
    """
    return calculation(9, input_value) if input_value else 9


def plus(value: int):
    return ("+", value)


def minus(value: int):
    return ("-", value)


def times(value: int):
    return ("*", value)


def divided_by(value: int):
    return ("/", value)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
