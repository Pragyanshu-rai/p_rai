def fact():
    i=int(input("enter the number to fid its factorial"))
    f=1
    while i!=0:
        f=f*i
        i-=1
    print(f)
def power():
    i=int(input("enter the number"))
    a=int(input("enter the power"))
    i=i**a
    print(i)
def gcd():
    i=int(input("enter the first number"))
    a=int(input("enter the second number"))
    x=1
    y=0
    if a<i:
        while x<=i//2:
            if i%x==0 and a%x==0:
                if x>y:
                   y=x
            x+=1
    if a>i:
        while x<=a//2:
            if i%x==0 and a%x==0:
                if x>y:
                   y=x
            x+=1
    print(y)
#gcd ()
def fib():
    i=int(input("enter the number"))
    x=0
    y=0
    z=0
    f=1
    while x<=i:
        if x==0:
            #print(f)
            if x==i-1:
               print(f)
            x+=1
        else:
            y=f
            f=f+z
            #print(f)
            if x==i-1:
               print(f)
            z=y
            x+=1
            #remove"#"to generate fibonacci series
print("enter the choice")
a=int(input('1.Factorial 2.Power 3.GCD 4.Fibonacci'))
if a==1:
    fact ()
if a==2:
    power ()
if a==3:
    gcd ()
if a==4:
    fib ()




