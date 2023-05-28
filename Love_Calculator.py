# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1=name1.lower()
name2=name2.lower()

true_name1_test= int(name1.count('t'))+int(name1.count('r'))+int(name1.count('u'))+int(name1.count('e'))
true_name2_test= int(name2.count('t'))+int(name2.count('r'))+int(name2.count('u'))+int(name2.count('e'))
true_test_combined=true_name1_test+true_name2_test

love_name1_test= int(name1.count('l'))+int(name1.count('o'))+int(name1.count('v'))+int(name1.count('e'))
love_name2_test= int(name2.count('l'))+int(name2.count('o'))+int(name2.count('v'))+int(name2.count('e'))
love_test_combined=love_name1_test+love_name2_test

score= str(true_test_combined) + str(love_test_combined)
score= int(score)
if score<=10 or score>=90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

"""
#OTHER SOLUTION

name_string = name1 + name2
name_string = name_string.lower()

t=name_string.count('t')
r=name_string.count('r')
u=name_string.count('u')
e=name_string.count('e')
true = t + r + u + e

l=name_string.count('l')
o=name_string.count('o')
v=name_string.count('v')
e=name_string.count('e')
love = l + o + v + e

score = int(str(true) + str(love))

if score<=10 or score>=90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
"""