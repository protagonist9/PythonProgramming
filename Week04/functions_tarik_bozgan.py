def custom_power(x, e=1):
    return x ** e

def custom_equation(x, y, a=1, b=1, *, c=1):
    return (x ** a + y ** b) / c

call_counts = {}

def fn_w_counter():
    caller_name = __import__('inspect').currentframe().f_back.f_code.co_name
    call_counts[caller_name] = call_counts.get(caller_name, 0) + 1
    return (call_counts[caller_name], {k: v for k, v in call_counts.items()})