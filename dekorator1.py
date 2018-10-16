def logger(f):
    def _wrapper(*args, **kwargs):
        print("args= ", args)
        print ("kwargs= ", kwargs)
        result= f(*args, **kwargs)
        print("result= ", result)
        return result
    return _wrapper

@logger
def mul(x,y):
    return x*y

mul(3,4)
