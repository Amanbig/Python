a=[]
print('Enter size of array')
b=int(input())
print('Enter array elements')
for i in range(b):
    c=int(input())
    a.append(c)
print('Applying selection sort')
for i in range(len(a)):
    for j in range(i,len(a)):
        if(a[i]>=a[j]):
            a[i],a[j]=a[j],a[i]
print('Sorted list is:')
for i in a:
    print(i,sep=" ")