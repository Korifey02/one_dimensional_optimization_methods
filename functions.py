from math import sin
def Functions(argument):
    
    def firstFunction(x):
        return 4*(x**3) - 8*(x**2) - 11*x + 5

    def secondFunction(x):
        if x == 0:
            x = 0.001
        return x + (3 / x**2)

    def thirdFunction(x):
        if x == 2:
            x = 2.001
            print(x)
        elif x == -2:
            x = -2.001
        return (x + 2.5)/(4-x*x)

    def fourthFunction(x):
        return -sin(x) - (sin(3*x)/3)

    def fifthFunction(x):
        return -2*sin(x) - sin(2*x) - (2*sin(3*x)/3)

    def sithFunction(x: int):
        return (x-1)**2

    match argument:
        case 1:
            return firstFunction
        case 2:
            return secondFunction
        case 3:
            return thirdFunction
        case 4:
            return fourthFunction
        case 5:
            return fifthFunction
        case 6:
            return sithFunction