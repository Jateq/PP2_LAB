viper=list()
kayo=list()
while True:
    n1=int(input())
    if n1==0:
        break
    else: viper.append(n1)
x=len(viper)-1
if len(viper)%2==0:
    for i in range(len(viper)//2):
        kayo.append(viper[i]+viper[x])
        x-=1
else:
    for i in range(len(viper)//2+1):
        if i ==len(viper)//2:
            kayo.append(viper[i])
            continue
        kayo.append(viper[i]+viper[x])
        x-=1
for i in kayo:
    print(i,end=" ")