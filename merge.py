def merge(a,b,c,d):
    n1=c-b+1
    n2=d-c
    e=[]
    f=[]
    for i in range(n1):
        e.append(a[i+b])
    for j in range(n2):
        f.append(a[j+c+1])
    i,j,k=0,0,b
    while i<n1 and j<n2:
        if(e[i]<=f[j]):
            a[k]=e[i]
            i=i+1
        else:
            a[k]=f[j]
            j=j+1
        k=k+1
    while i<n1:
        a[k]=e[i]
        i=i+1
        k=k+1
    while j<n2:
        a[k]=f[j]
        j=j+1
        k=k+1
def mergesort(a,b,c):
    if(b<c):
        mid=int(b+(c-b)/2)
        mergesort(a,b,mid)
        mergesort(a,mid+1,c)
        merge(a,b,mid,c)
a=[]
print('Enter size of array')
b=int(input())
print('Enter array elements')
for i in range(b):
    c=int(input())
    a.append(c)
print('Applying merge sort')
mergesort(a,0,len(a)-1)
print('The sorted array is')
for i in a:
    print(i,sep="")
