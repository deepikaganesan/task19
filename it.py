def product(a,b):
    if(b == 0):
        return 0
    if(b > 0):
        return (a + product(a, b - 1))
    if(b < 0):
        return -product(a, -b)
print product(2, 3)

def flatten_dict(d, sep='.', prefix=''):
     return { prefix + sep + k if prefix else k : v
              for kk, vv in d.items()
              for k, v in flatten_dict(vv, sep, kk).items()
              } if isinstance(d, dict) else {prefix : d }

def unflatten_dict(d):
     result = {}
     for k, v in d.items():
         context = result
         for sub_key in k.split('.')[:-1]:
             if sub_key not in context:
                 context[sub_key] = {}
             context = context[sub_key]
             context[k.split('.')[-1]] = v
     return result

def map(List):
     for i, ele in enumerate(List):
         if isinstance(ele, list):
             List[i] = map(ele)
         else:
             List[i] = ele**2
     return List

s = ([[1, 2], [3, [4, 5]], 6])
def rev(List):
    if len(List) == 0:
        return
    if len(List) == 1:
        if isinstance(List[0], list):
            return [rev(List[0])]
        else:
            return List
    else:
        return rev(List[1:]) + rev(List[:1])

print s
print rev(s)

def count(S, a, b):
     table = [0 for k in range(b+1)]
     table[0] = 1
     for i in range(0,a):
         for j in range(S[i], b+1):
             table[j] += table[j-S[i]]
     return table[b]

from itertools import permutations
perm = permutations([1,2,3])
for i in list(perm):
    print i

import profile
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
fib = profile(fib)
fib(20)

x=[1,2,3,4]
y=reversed(x)
y.next()

def grep(pattern, dir):
    for f in dir:
        for line in open(f):
            if pattern in line:
                print line,

grep(".py","Downloads")


s=iter(range(5))
peek = next(s)
s=(value for g in([peek], s) for value in g)
print(peek, list(s))


s1= ['a', 'b', 'c']
for index, value in enumerate(s1):
print index, value
list(enumerate(s1))

from itertools import *
for in izip(['k','l','m'], [8, 9, 7]):
    print i


