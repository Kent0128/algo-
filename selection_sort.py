l=[63,92,27,36,45,71,58,7]
for t in range(len(l)): 
    idx=t
    small=l[t]
    for q in range(t+1,len(l)):
        if l[q]<small:
            small=l[q]
            idx=q
    l[idx],l[t]=l[t],l[idx]
    print(l)

   
