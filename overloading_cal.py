from multipledispatch import dispatch

@dispatch(int)
def calci(a):
    res=a*a
    print("square",res)

@dispatch(int,int)
def calci(a,b):
    add=a+b
    print("addition",add)

calci(2)
calci(3,5)




overloading -- calculator
class Calculator:
    def add(self, a, b):
        return a + b


    def add(self, a, b, c):
        return a + b + c


    def subtract(self, a, b):
        return a - b


    def multiply(self, a, b):
        return a * b


# Usage
calc = Calculator()
print(calc.add(2, 3))       # Overloaded add method with 2 arguments
print(calc.add(2, 3, 4))    # Overloaded add method with 3 arguments
print(calc.subtract(5, 2))
print(calc.multiply(4, 6))
