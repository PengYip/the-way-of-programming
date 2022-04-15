import time


def cal_time(func):
    """装饰器，计时"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args,**kwargs)
        ti = time.perf_counter() - start
        print(func.__name__)
        print(ti)
    return wrapper
