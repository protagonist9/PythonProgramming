import sys

custom_power = lambda x=0, /, e=1: x**e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Belirtilen formüle göre kayan noktalı bir sayı döndürür.

    :param x: Konumsal-tek parametre (Varsayılan 0).
    :param y: Konumsal-tek parametre (Varsayılan 0).
    :param a: Konumsal-veya-anahtar kelime parametresi (Varsayılan 1).
    :param b: Konumsal-veya-anahtar kelime parametresi (Varsayılan 1).
    :param c: Anahtar kelime-tek parametre (Varsayılan 1).
    :returns: (x**a + y**b) / c formülünün sonucunu döndürür.
    :rtype: float
    """
    return (x**a + y**b) / c

def fn_w_counter() -> tuple[int, dict[str, int]]:
    if not hasattr(fn_w_counter, 'count'):
        fn_w_counter.count = 0
        fn_w_counter.callers = {}

    caller_name = sys._getframe(1).f_globals['__name__']
    
    fn_w_counter.count += 1
    fn_w_counter.callers[caller_name] = fn_w_counter.callers.get(caller_name, 0) + 1

    return fn_w_counter.count, fn_w_counter.callers