def ShellSort(a,interval):
    if interval>=1:
        for i in range(int(len(a)-interval)):
            if int(a[i])>int(a[i+interval]):
                a[i],a[i+interval]=a[i+interval],a[i]
        return ShellSort(a,int(interval/2))
    print(a)
x=input().split(",")
ShellSort(x,int(len(x)/2))
            
            