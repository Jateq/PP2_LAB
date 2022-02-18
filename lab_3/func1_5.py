from itertools import permutations
def permutate(s):
    # key -> kye -> eky, eyk, if len is three 3! if for 4!
    perms = [''.join(p) for p in permutations(s)]
    print(*perms)

s = input()
permutate(s)