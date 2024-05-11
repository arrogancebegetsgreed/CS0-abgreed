import random
for i in random.sample(range(1, 21), 20):
    test = int(input("Please enter a number between -10 and 10"))
    if test >= -10 and test <= 10:
        if test % 2 == 0:
            print("x is even")
        else:
            print("x is odd")
    else:
        break
