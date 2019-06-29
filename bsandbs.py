def bbs(b,a):
    i=1
    j=0
    x=0
    while i<a:
        while j<a-1:
            if b[j]>b[j+1]:
                x=b[j]
                b[j]=b[j+1]
                b[j+1]=x
            j+=1
        j=0
        i+=1
    #print(b)#to check the list
    return b
def bs(b,a,x):
    c = int(input("enter the element to search"))
    x //= 2
    i=0
    if c >= b[x]:
        while x<a:
            if b[x] == c:
                print("element found")
                i+=2
                break
            x += 1
    if c<b[x]:
        while x >= 0:
            if b[x] == c:
                print("element found")
                i+=2
                break
            x -= 1
    if i==0:
        print("element not found")
a=int(input("enter the size of the list"))
x=a
i=0
b=[]
while i<a:
    b.insert(i,int(input("enter the number")))
    i+=1
bbs(b,a)
bs(b,a,x)

