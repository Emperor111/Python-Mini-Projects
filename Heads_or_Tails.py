#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random
x=random.randint(0,9e99)
if x%2==0:
    print("Heads")
else:
    print("Tails")