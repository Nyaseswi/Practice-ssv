#Positional A'
def find_biggest_number(a, b):
    return max(a, b)

# between 2 and 6
num1 = 2
num2 = 6
result = find_biggest_number(num1, num2)
print(f"The biggest number between {num1} and {num2} is: {result}")

#keyword A'
def find_biggest_number(**kwargs):
    num1 = kwargs['num1']
    num2 = kwargs['num2']
    return max(num1, num2)


result = find_biggest_number(num1=2, num2=6)
print(f"The biggest number is: {result}")

#Default A'
def find_biggest_number(num1, num2=0):
    return max(num1, num2)


result1 = find_biggest_number(2, 6)
result2 = find_biggest_number(5)
print(f"The biggest number between 2 and 6 is: {result1}")
print(f"The biggest number between 5 and 0 is: {result2}")

#AA'
def find_biggest_number(*args):
    return max(args)


result1 = find_biggest_number(2, 6, 1, 9)
result2 = find_biggest_number(5, 3, 8)
print(f"The biggest number is: {result1}")
print(f"The biggest number is: {result2}")


