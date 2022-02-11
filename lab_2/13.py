pje=input()

sova=list()

for i in range(len(pje)):

    if pje[i]=='(' or pje[i]=='{' or pje[i]=='[':

        sova.append(pje[i])

    elif pje[i]==')':

        if len(sova)==0:

            print("No")

            exit()

        elif sova[-1]=='(':

            sova.pop()

        else:

            print("No")

            exit()

    elif pje[i]=='}':

        if len(sova)==0:

            print("No")

            exit()

        elif sova[-1]=='{':

            sova.pop()

        else:

            print("No")

            exit()
    elif pje[i]==']':

        if len(sova)==0:

            print("No")

            exit()

        elif sova[-1]=='[':

            sova.pop()

        else:

            print("No")

            exit()

if len(sova)==0:

    print("Yes")

else:

    print("No")