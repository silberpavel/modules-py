# compose functions (with lambda)  Лямбда не хранится в памяти!
##def compose(f, g):
##    return lambda x: f(g(x))

double = lambda x: x * 2
inc = lambda x: x + 1
inc_and_double = lambda x: double(inc(x))

print(inc_and_double(10))

# lambda (only one expression)
def add(x):
    return lambda y: x + y

a = add(10) # lambda y: 10 + y
# a(10) => 20

# closure counter
def counter(w):
    def ret(y):
        return y + w
    return ret

g = counter(1)
print(g(1))
print(g(5))
print(g(3))
print(g(1))

# example 0:58









