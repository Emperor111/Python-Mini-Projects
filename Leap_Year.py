# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
"""
a = year%4
b = year%100
c = year%400

if c==0:
    print("Leap year.")
elif b==0:
    print("Not leap year.")
elif a==0:
    print("Leap year.")
else:
    print("Not leap year.")
"""
#ANOTHER Solution

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")