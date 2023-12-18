import functools
import time
import json



def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

#--------------------------------------------------------------------

def slow_down2(func):
    """_Sleep_
              Arguments:
              func -- _sleep 1 second before calling_
    """
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(b)
        return func(*args, **kwargs)
    return wrapper_slow_down

#--------------------------------------------------------------------
a = int(input('Enter Timer(sec) number: '))
b = int(input('Enter DElay(sec) number: '))


@slow_down2
def countdown(from_number):
    if from_number < 0:
        print("your TIME is over!")
    else:
        print(from_number)
        countdown(from_number - 1)
print(countdown(a))


