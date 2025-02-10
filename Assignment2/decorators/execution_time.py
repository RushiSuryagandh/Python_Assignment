import time
def execution_time(func):
    """
    decorator used to calculate execution time.
    """
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print(f'Execution time :{end_time-start_time}')
    return wrapper