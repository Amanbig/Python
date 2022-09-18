def fac(a):
    if a==1 or a==0:
         return 1
    else :
        return a*fac(a-1)
def main():
    b=0
    c=1
    d=[]
    e=0
    a=int(input("Enter number"))
    while c<=a:
        c+=1
        b=int(input("Enter number"))
        e=fac(b)
        d.append(e)
    for i in d:
        print(i)
main()