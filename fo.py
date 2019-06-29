a=int(input('enter the size'))
i=0
b=[]
c=0
while i<a:
     b.insert(i,int(input("enter the element")))
     i+=1
i=0
while i<a:
     c=(c*10)+(b[i]%10)
     i+=1
print(c)
c=0
i=0
while i<a:
     if b[i]%2==0:
          c=(c*10)+(b[i]%10)
          i+=1
     i += 1
print(c)

