def int_to_roman(number: int) -> str:
    res: str = ""

    roman_dict: dict[int, str] = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    if number < 1 or number > 3999:
        return "ERROR"
    while number > 0:
        for num in roman_dict:
            if num <= number:
                res += roman_dict[num]
                number -= num
                break
    return res


if __name__ == "__main__":
    print(int_to_roman(3))     # III
    print(int_to_roman(4))     # IV
    print(int_to_roman(9))     # IX
    print(int_to_roman(58))    # LVIII
    print(int_to_roman(1994))  # MCMXCIV
    print(int_to_roman(3999))  # MMMCMXCIX
    print(int_to_roman(0))     # ERROR
    print(int_to_roman(4000))  # ERROR
