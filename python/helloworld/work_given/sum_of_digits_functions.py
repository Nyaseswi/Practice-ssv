def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits(number // 10)

#sum of 1+2+3+4+5
number = 12345
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")
