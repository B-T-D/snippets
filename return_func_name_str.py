"""Return the name of a function object as a string."""

def my_function(x):
    return f"{my_function.__name__} was called on argument {x}"

print(my_function('x'))
