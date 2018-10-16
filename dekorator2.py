class Recorded:
    def __init__(self, func):
        self.func = func
        self.calls= []
    def __call__(self, *args,**kwargs):
        entry ={'args':args, 'kwargs':kwargs, 'return':self.func(*args,**kwargs)}
        self.calls.append(entry)
        return entry['return']

@Recorded
def foo(a,b):
    return a*b

foo(12,b=32)
foo(2,1)
foo(5,6)
foo.calls
