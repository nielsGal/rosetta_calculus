const I = a => a
const M = a => a(a)
const K = a => b => a
const C = f => a => b => f(b)(a)
const B = f => g => a => f(g(a))
const Th = a => f => f(a)
const V = a => b => f => f(a)(b)
const B1 = f => g => a => b => f(g(a)(b))
const KI = a => b => b
const Y = f => M( x => f(M(x)))
const Z = f => M(x => f( v=> M(x)(v)))

const T = a => b => a
const F = a => b => b
const Not =  p => p(F)(T)
const And = p => q => p(q)(p)
const Or = p => q => p(p)(q)
const Beq = p => q => p(q)((Not(q)))

const succ = n => f => a => f(n(f)(a))
const add = n => k => f => B(n(f))(k(f))
const exp = n => k => k(n)

const pair = a => b => f => f(a)(b)
const first = p => p(K)
const second = p => p(KI)
const phi = p => pair(second(p))(succ(second(p)))
const setFirst = c => p => pair(c)(second(p))
const setSecond = c => p => pair(first(p))(c)

const pred = n => first(n(phi)(pair(n0)(n0)))
const sub = null

const n0 = f => a => a
const n1 = f => a => f(a)
const n2 = f => a => f(f(a))
const n3 = f => a => f(f(f(a)))
const n4 = f => a => f(f(f(f(a))))
const n5 = f => a => f(f(f(f(f(a)))))

