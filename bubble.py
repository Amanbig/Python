a=[]
print('Enter size of array')
b=int(input())
print('Enter array elements')
for i in range(b):
    c=int(input())
    a.append(c)
print('Applying bubble sort')
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if(a[j]>=a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]
print('The sorted array is')
for i in a:
    print(i,sep="")