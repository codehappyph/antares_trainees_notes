"""
Python Classes

- Class declaration
- Class special methods
    - constructor / destructor
    - __init__
    - __del__

    - debug helpers / descriptors
    - __str__
    - __repr__
- Functions as first-class citizens

"""


class EmpytBase:
    pass  # Tells the interpreter to do nothing


class InitBase:

    def __init__(self, num1, num2):
        # Constructor method
        # Called when initializing the object.
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f'<InitBase num1={self.num1} num2={self.num2}>'

    __repr__ = __str__

    def __del__(self):
        # Destructor method (del keyword)
        # Called when the object is destroyed / when all there are
        # no more references to the object.
        pass
