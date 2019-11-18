P1 = lambda x: x + 1


I = lambda x: x
M = lambda x: x(x)
K = lambda a: lambda b: a
C = lambda f: lambda a: lambda b: f(b)(a)
B = lambda f: lambda g: lambda a: f(g(a))
Th = lambda a: lambda f: f(a)
V = lambda a: lambda b: lambda f: f(a)(b)

T = lambda a: lambda b: a
F = lambda a: lambda b: b


Not = lambda p: p(F)(T)
And = lambda p: lambda q: p(q)(p)
Or = lambda p: lambda q: p(p)(q)
Beq = lambda p: lambda q: p(q)(Not(q))

N0 = lambda f: lambda a: a 
N1 = lambda f: lambda a: f(a)
N2 = lambda f: lambda a: f(f(a))
N3 = lambda f: lambda a: f(f(f(a)))
N4 = lambda f: lambda a: f(f(f(f(a))))
N5 = lambda f: lambda a: f(f(f(f(f(a)))))

succ = lambda n: lambda f: lambda a: f(n(f)(a))
add = lambda n: lambda k: lambda f: B(n(f))(k(f))
exp = lambda n: lambda k: k(n)
mult = lambda n: lambda k: lambda f: n(k(f))
pred = lambda n:
sub = lambda n: lambda k: k(pred)(n)