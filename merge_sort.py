def MergeSort(a):
    if len(a)>1:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]
        MergeSort(left)
        MergeSort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if int(left[i]) <= int(right[j]):
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
x=input().split(",")
MergeSort(x)
print(x)
