# Q1: find smallest number
a=eval(input())
min=a[0]
for i in range(len(a)):
    if a[i]<min:
        min=a[i]
print(min)

# Q2: bubble sort
a=eval(input())
counter=0
while(counter<len(a)):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    counter+=1
print(a)

# Q3: binary search
a=eval(input())
goat=int(input())
lower=0
upper=len(a)-1
count=0
for i in a:
    if i==goat:
        count+=1
if count==0:
    print("-1")
else:
    while lower<=upper:
        mid=int((lower+upper)/2)
        if a[mid]<goat:
            lower = mid+1
        elif a[mid]>goat:
            upper = mid-1
        else:
            print(mid)
            break