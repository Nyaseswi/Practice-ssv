matches_won = 20
goals = 11
if matches_won >=15:
    if goals >=10:
        print("Hurry")
        print("You won ")
#age
aged = 80
geriatric = 50
if aged >=60:
    if geriatric >=50:
        print("You are old people")
else:
    print("pediatric")
#not(opposite_value)
if not(not(True)): 
    if not(False):
        print("Yes")
#condition1 and condition2 should be true
a = (len("Tiger")) == (len("Mouse")) #True
b = (True or False) #True
sum = 9 
if a:
    sum = sum +10
    print(sum)
    if b:
        sum = sum + 5
        print(sum)
    print(sum)
print("END")
#example1
expression1 = (36 < 16) #false
expression2 = (True or True) #True
if expression1:
    print("expression1 is True")
if expression2:
    print("expression2 is True")
print("END")

