def taf(a,i):
    x=0
    s=0
    while s<=i:
        if a[s]%3==0 and a[s]%5==0:
            x+=a[s]
        s+=1
    print(x)
a=[]
b=int(input("enter the size of the list"))
b-=1
i=b
while b>=0:
    b -= 1
    a.append(int(input("enter the element")))
taf (a,i)