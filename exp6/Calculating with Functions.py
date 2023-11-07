def zero(f = None): return f(0) if callable(f) else 0
def one(f = None): return f(1) if callable(f) else 1
def two(f = None): return f(2) if callable(f) else 2
def three(f = None): return f(3) if callable(f) else 3
def four(f = None): return f(4) if callable(f) else 4
def five(f = None): return f(5) if callable(f) else 5
def six(f = None): return f(6) if callable(f) else 6
def seven(f = None): return f(7) if callable(f) else 7
def eight(f = None): return f(8) if callable(f) else 8
def nine(f = None): return f(9) if callable(f) else 9

def plus(x): return lambda y: x + y
def minus(x): return lambda y: y - x
def times(x): return lambda y: y * x
def divided_by(x): return lambda y:int(y/x)
