def fac(a):
    if a==0 or a==1:
        return 1
    else:
        return a*fac(a-1)
a=int(input('Enter number \n'))
print(fac(a))