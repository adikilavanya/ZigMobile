
def maskify(number):
    masked_number = '#' * (len(number) - 3) + number[-3:]
    print(masked_number)

# Test case
input = input()
maskify(input)

#example
#maskify("9988776655")  # Output: #######655




