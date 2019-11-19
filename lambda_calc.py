#use this to test, for example N5(P1)(0) should be 5
P1 = lambda x: x + 1

# some set of combinators
I = lambda x: x
M = lambda x: x(x)
K = lambda a: lambda b: a
KI = lambda a: lambda b: b
C = lambda f: lambda a: lambda b: f(b)(a)
B = lambda f: lambda g: lambda a: f(g(a))
Th = lambda a: lambda f: f(a)
V = lambda a: lambda b: lambda f: f(a)(b)
B1 = lambda f: lambda g: lambda a: lambda b: f(g(a)(b))

#booleans True and False
T = lambda a: lambda b: a
F = lambda a: lambda b: b

#boolean functions, supply with T and F return T and F
Not = lambda p: p(F)(T)
And = lambda p: lambda q: p(q)(p)
Or = lambda p: lambda q: p(p)(q)
Beq = lambda p: lambda q: p(q)(Not(q))

#some hard coded church numerals
N0 = lambda f: lambda a: a 
N1 = lambda f: lambda a: f(a)
N2 = lambda f: lambda a: f(f(a))
N3 = lambda f: lambda a: f(f(f(a)))
N4 = lambda f: lambda a: f(f(f(f(a))))
N5 = lambda f: lambda a: f(f(f(f(f(a)))))
churchToInt = lambda n: n(P1)(0)

#lists and list operators
pair = lambda a: lambda b: lambda f: f(a)(b)
first = lambda p: p(K)
second = lambda p: p(KI)
phi = lambda p: pair(second(p))(succ(second(p)))
setFirst = lambda c: lambda p: pair(c)(second(p))
setSecond = lambda c: lambda p: pair(first(p))(c)

#chuch bool operations
succ = lambda n: lambda f: lambda a: f(n(f)(a))
add = lambda n: lambda k: lambda f: B(n(f))(k(f))
exp = lambda n: lambda k: k(n)
mult = lambda n: lambda k: lambda f: n(k(f))
pred = lambda n: first( n (phi) (pair(N0)(N0)))
sub = lambda n: lambda k: k(pred)(n)

#these functions take Church numerals and return church bools
isZero = lambda n: n(K(F))(T)
LeQ = lambda n: lambda k: isZero(sub(n)(k))
eQ = lambda n: lambda k: And(LeQ(n)(k))(LeQ(n)(k))

#lists
nil = pair(T)(T)
const = lambda h: lambda t: pair(F)(pair(h)(t))
head = lambda z: first(second(z)) 
tail = lambda z: second(second(z))

#binary trees
Empty = lambda e: lambda b: e
Branch = lambda x: lambda l: lambda r: lambda e: lambda b: b(x)(l(e)(b))(r(e)(b))
Treesum = lambda t: t(0)(lambda x:lambda l:lambda r: x+l+r)
#todo DFS BFS