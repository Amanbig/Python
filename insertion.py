a=[]
print('Enter size of array')
b=int(input())
print('Enter array elements')
for i in range(b):
    c=int(input())
    a.append(c)
print('Applying insertion sort')
for i in range(1,len(a)):
    d=a[i]
    j=i-1
    while j>=0 and a[j]>d:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=d
print('The sorted array is')
for i in a:
    print(i,sep="")
