x=int(input("enter the number"))
i=0
a=0
while(x!=0):
    a=x%10
    if (a%2==0):
        i+=a
    x//=10

print(i)
