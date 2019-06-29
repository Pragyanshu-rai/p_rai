x= int(input('enter the number to search repetetion'))
y= int(input('enter the lower limit'))
z= int(input('enter the upper limit'))
v=y
a=0
i=0
while y<z:
    while(y>0):
        a=y%10
        if a==x:
           # print('10')
            i+=1
        y//=10
    y=v
    v+=1
    y+=1
print(i)
