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


print(parent(2)())

