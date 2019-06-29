def ls(a,b,key):
    c='!' #['!!']
    j=0
    i=0
    while j<a:
        if key==b[j]:
            if i>0:
                #c=x*(j)
                print(c*j,end =" ")
            #print('element found at')
            #print(a-1)
            else:
                print(c, end= " ")
            i+=1
            #break
        j+=1
    if i==0:
        print('element not found')

a=int(input("enter the size of the list"))
b=[]
i=0
while i<a:
    b.insert(i, int(input('enter the number')))
    print(b)
    i+=1
key=int(input("enter the number to search"))
ls(a,b,key)



