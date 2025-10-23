from string import *

def to_base(number, base):
    if number == 0:
        return "0"

    result = ""
    while number:
        result = printable[number % base] + result
        number //= base
    return result.upper()