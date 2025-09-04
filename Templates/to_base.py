def to_base(number, base):
    base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while number:
        result += base_string[number % base]
        number //= base
    return result[::-1] or "0"
