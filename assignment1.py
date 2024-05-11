def decimal_to_hex(decimal):
    hex_digits = "0123456789ABCDEF"
    if not decimal.isdigit():
        print("Invalid input")
        return
    decimal = int(decimal)
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal = decimal // 16
    print(hexadecimal)

def hex_to_decimal(hexadecimal):
    if not all(c in "0123456789ABCDEF" for c in hexadecimal):
        print("Invalid input")
        return
    decimal = 0
    power = len(hexadecimal) - 1
    for digit in hexadecimal:
        decimal += int(digit, 16) * (16 ** power)
        power -= 1
    print(decimal)

# Test cases
decimal_input = input()

decimal_to_hex(decimal_input)  # Output: 7B
hex_input = input()
hex_to_decimal(hex_input)   # Output: 123
