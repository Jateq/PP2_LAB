proposition = input()
leas = proposition.split(' ')
leorio = list()
for i in leas:
    if len(i) >=3:
        leorio.append(i)
print(*leorio, sep = " ")