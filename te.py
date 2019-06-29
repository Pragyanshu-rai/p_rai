cont={}
cont1={}
def ac(na,nu,cont):
    if na not in cont:
        cont[na]=nu
        print("the contact %s: %s is added"%(na,nu))
    else:
        print("the contact %s already exists"%na)
    #print(cont)
    sc(na, nu, cont)
    return cont
def sc(na,nu,cont):
    if na in cont:
        print("the contact %s: %s is in the list"%(na,nu))
    else :
        print("the contact %s is not in the list" %na)
    ucnu(na, nu, cont)
def dc(na,nu,cont):
    print(nu)
    if na in cont:
        print('the contact %s: %s is deleted'%(na,nu))
        del cont[na]
    else:
        print("the contact %s: %s does not exist"%(na,nu))
def ucnu(na,nu,cont):
    if na in cont:
        nu=input('enter the number')
        cont[na]=nu
        print(nu)
        print(na,'the contact  is updated',cont[na])
    else:
        print('the contact does not exist')
    print(nu)
    dc(na, nu, cont)
    return cont,na,nu
#print(cont)
na ='rai'
nu ='0123456789'
ac(na,nu,cont)

print(cont)
