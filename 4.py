# cook your dish here
def main():
    a=[]
    f=0
    g=1
    f=int(input())
    while(g<=f):
        g+=1
        b,c,d=input("").split()
        e=int(b)*4+int(c)*2
        a.append(e)
    for i in a:
        print(i)
if __name__=="__main__":       
       main()