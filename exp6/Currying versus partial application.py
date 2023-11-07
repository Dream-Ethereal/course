def curry_partial(f, *args):  
    if not callable(f): 
        return f
    num_args = f.__code__.co_argcount

    if num_args == 0:
        return f(*args)
    if len(args) >= num_args:
        return f(*args[:num_args])
    def inner(*params):    
        all_args = [*args, *params]
        if not args:
            return curry_partial(f, *all_args)        
        if not callable(args[0]):
            return curry_partial(f, *all_args)
        fn = args[0]
        num_args2 = fn.__code__.co_argcount

        if num_args2 == 0:
            return fn(*all_args)
        if len(all_args) >= num_args2:
            return fn(*all_args[:num_args2])
        else:
            return curry_partial(fn, *all_args)
        
    return inner