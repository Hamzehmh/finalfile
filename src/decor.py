def parent(num):
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")
    if num == 2:
        return first_child
    else:
        return second_child


#-------



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
        
    return wrapper

@my_decorator
def say_whee():
    """
    This function returns some stuff!
    """
    print("Whee!")

print(say_whee())    