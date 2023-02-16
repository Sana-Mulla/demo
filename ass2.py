
#for i in range(30,19,-1):
#       print(i)

#for i in range(1,11):
#       print(i)


#printing no from 30 to 20 using while loop.

i=30
while i>=20:
        print(i)
        i-=1


# Print even no from 20 to 40.
'''
for i in range(20,41):
        if i%2 == 0:
                print(i)
        else:
                print()
'''
'''
for i in range(50,29,-1):
        if i%2!=0:
                print(i)
'''
'''
for i in range(100,201):
        if i%7==0:
                print(i)
'''

'''
sum = 0
for i in range(1,11):
        sum+= i
print("The sum of first ten no is:",sum)
'''
sum = 0
for i in range(30,51):
        if i%2==0:
                sum+=i
        
print("The sum of even no from 30 to 50 is:",sum)

sum = 0
for i in range(40,51):
        if i%2!=0:
                sum+=i
        
print("The sum of odd no from 40 to 50 is:",sum)

