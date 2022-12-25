'''
a = [1,2,3,4,5,6,7,8,9,10]
res=0
for i in a:
    res=res+i
print(res)

'''
'''
a = input()

if a[::]== a[::-1]:
    print("the given string is Palindrome")
else:
    print("the given string is not a Palindrome")
'''
'''

n = int(input("enter the number: "))
for i in range(1, n+1):
    if (n%i==0):
        print(i)
'''

n = int(input())
for i in range(n):
    for j in range(2,i):
        if i%j == 0:
            break

    else:
        print(i)
    
        
    



