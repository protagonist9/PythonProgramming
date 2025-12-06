custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Returns (x**a + y**b) / c
    
    :param x: First value
    :param y: Second value
    :param a: Exponent for x
    :param b: Exponent for y
    :param c: Divisor
    :return: Result of (x**a + y**b) / c
    """
    return (x ** a + y ** b) / c

_calls = {}

def fn_w_counter():
    caller = __import__('inspect').currentframe().f_back.f_code.co_name
    _calls[caller] = _calls.get(caller, 0) + 1
    return _calls[caller], dict(_calls)