def custom_power(x, e=1):
    return x ** e

def custom_equation(x, y, a=1, b=1, *, c=1):
    return (x ** a + y ** b) / c

_calls = {}

def fn_w_counter():
    caller = __import__('inspect').currentframe().f_back.f_code.co_name
    _calls[caller] = _calls.get(caller, 0) + 1
    return (_calls[caller], dict(_calls))

def performance(f):
    def w(*a, **k):
        import time, tracemalloc
        tracemalloc.start()
        t = time.time()
        r = f(*a, **k)
        w.total_time += time.time() - t
        w.total_mem += tracemalloc.get_traced_memory()[0]
        tracemalloc.stop()
        w.counter += 1
        return r
    w.counter = w.total_time = w.total_mem = 0
    return w