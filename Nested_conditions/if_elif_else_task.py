#finding grade of a student based on percentage 
percentage = int(input())
if percentage>=80 and percentage<=100:
    print("Grade: A")
elif percentage>=65 and percentage<=80:
    print("Grade: B")
elif percentage>=50 and percentage<=65:
    print("Grade: C")
elif percentage>=45 and percentage<=50:
    print("Grade: D")
elif percentage>=100 and percentage<=0:
    print("Inavlid percentage")
elif percentage<=45:
    print("Fail")
