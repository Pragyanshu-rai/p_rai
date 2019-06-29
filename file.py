import re
def ev(e):
    p = "^[1][2][0-9][a-z]$"
    if re.match(p, e):
        print("true")
    else:
        print('false')
e=input('enter the email')
#ev(e)
def pas(pa):
    p = "^[A-Z][a-z]reg{6-10}[0-9]$"
    if re.match(p, pa):
        print('the password is accepted')
    else:
        print('password is not accepted')
pa=input('enter the password(1.upercase 2.lowercase 3.length(6-10))')
#pas(pa)
def nu(n):
    p = "^reg{9}[0-9]$"
    if re.match(p, n):
        print('the number is valid')
    else:
        print('the number is invalid')
n=input('enter the number')
nu(n)





