from random import randint
cnt = 0 
rand_number = randint(1, 20)
print("Hello! What is your name?")
name = input()
n = 0
print("Well," + name + ", I am thinking of a number between 1 and 20.")
while n != rand_number: 
    print("Take a guess")
    n = int(input())
    print()
    if n > rand_number:
        print("Your guess is too high.")
    elif n < rand_number:
        print("Your guess is too low.")
    elif n == rand_number:
        print("Good job, "+name+ " You guessed my number in "+ str(cnt+1) + " guesses!")
        print()
    cnt += 1