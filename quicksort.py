def partition(a,low,high):
    b=a[high]
    i=low-1
    for j in range(low,high):
        if a[j]<=b:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1
def quicksort(a,low,high):
    if(low<high):
        pi=partition(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)
a=[]
print('Enter size of array')
b=int(input())
print('Enter array elements')
for i in range(b):
    c=int(input())
    a.append(c)
print('Applying quick sort')
quicksort(a,0,len(a)-1)
print('The sorted array is')
for i in a:
    print(i,sep="")