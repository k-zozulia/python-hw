import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b(?:\d+\.\d+|\d+)\b'
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    total = 0.0
    for number in func(text):
        total += number
    return total
