l=[63,92,27,36,45,71,58,7]
L=[]
for t in range(len(l)):
    if len(L)==0:
        L.append(l[t])
    else:
        for i in range(len(L)):
            if l[t]<=L[i]:
                L.insert(i,l[t])
                break
            elif i==len(L)-1:
                L.append(l[t])

    print(L)