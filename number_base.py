def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    decimal_number = int(number, from_base)
    return convert_to_base(decimal_number, to_base)


def convert_to_base(number: int, base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if number == 0:
        return "0"

    result = ""

    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number //= base

    return result