import time
import sys
import functools
def performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        mem_usage = sys.getsizeof(result)

        wrapper.counter += 1
        wrapper.total_time += (end_time - start_time)
        wrapper.total_mem += mem_usage
        
        return result

    wrapper.counter = 0
    wrapper.total_time = 0
    wrapper.total_mem = 0

    return wrapper