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