custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x=0, y=0, /, a=1, b=1, *, c=1):
    return (x ** a + y ** b) / c

_calls = {}

def fn_w_counter():
    caller = __import__('inspect').currentframe().f_back.f_code.co_name
    _calls[caller] = _calls.get(caller, 0) + 1
    return _calls[caller], dict(_calls)