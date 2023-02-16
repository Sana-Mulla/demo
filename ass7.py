'''
num = 1
if num ==0:
        print("zero")
elif num ==1:
        print("one")
elif num ==2:
        print("two")
elif num ==3:
        print("three")
elif num ==4:
        print("four")
elif num ==5:
        print("five")
elif num ==6:
        print("six")
elif num ==3:
        print("seven")
elif num ==4:
        print("eight")
elif num ==5:
        print("nine")

else:
        print("Invalid digit")
'''

k = 16
tim = 1
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k - 4
    for j in range(0, tim):
        print("* ", end="")
    tim = tim + 2
    print()