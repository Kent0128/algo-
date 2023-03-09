def QuickSort(a):
    i=k=0
    j=len(a)-1
    while i<=len(a) and j>=1:
        if a[i]>a[k]:
            if a[j]<a[k]:
                if j>i:
                    a[i],a[j]=a[j],a[i]
                    return QuickSort(a)

                elif j<=i:
                    a[k],a[j]=a[j],a[k]
                    QuickSort(a[k:j])
                    QuickSort(a[j:])
                    return QuickSort(a)
            else:
                j-=1
        else: 
            i+=1
x=list(map(int,input().split(",")))
QuickSort(x)
print(x)