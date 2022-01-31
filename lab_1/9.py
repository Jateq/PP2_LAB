amount = input()
amount = int(amount)
kurapika = list()
for i in range(amount):
    gmail = input()
    spliter = gmail.split('@')
    if len(spliter) == 2:
        if spliter[1] =='gmail.com':
            kurapika.append(spliter)

for i,j in kurapika:
    print(i)

