from functions import Functions

# def nullCheck(param1, param2):
#     if param1 == 'ERROR' or param2 == 'ERROR':
#         return 0
#     return 1 

def GoldenRatio(a, b, e, func):
    t = 1.618
    x1 = a + ((b-a)/(t*t))
    x2 = a + ((b-a)/t)
    while (b-a)/2 >= e:
        Fx1 = func(x1)
        Fx2 = func(x2)
        if Fx1 <= Fx2:
            b = x2 
            x2 = x1
            x1 = a + b - x2
        else:
            a = x1
            x1 = x2
            x2 = a + b - x1
    return (a+b)/2

def PassiveSearch(a, b, N, func):
    xArray = N * [0]
    funcArray = N * [0]
    ind = 0
    for i in range(N):
        xArray[i] = a + (i * ((b-a)/(N-1)))
        funcArray[i] = func(xArray[i])
        if funcArray[i] < funcArray[ind]:
            ind = i
    # return xArray[i]
    return xArray[ind]


def findSection(x0, h, funcNum):
    Function = Functions(funcNum)
    k = 1
    a, b = -1000000000000, 1000000000000
    
    Fx_k_1 = Function(x0)
    Fx_k = Function(x0+h)
    
    # if not nullCheck(Fx_k_1, Fx_k):
    #     return 'bad', 'param'

    if Fx_k_1 > Fx_k:
        a = x0
        k = 2
        Fx_k_1 = Fx_k
        Fx_k = Function(x0 + h * (2**(k-1)))

        # if not nullCheck(Fx_k_1, Fx_k):
        #     return 'bad', 'param'

    else:
        h = -h
        Fx_k_1 = Function(x0)
        Fx_k = Function(x0+h)

        # if not nullCheck(Fx_k_1, Fx_k):
        #     return 'bad', 'param'

        if Fx_k >= Fx_k_1:
            a, b = x0+h, x0-h
            # return min(a, b) , max(a,b)
            return a, b
        else:
            b = x0
            k = 2
            Fx_k_1 = Fx_k
            Fx_k = Function(x0 + h * (2**(k-1)))

            # if not nullCheck(Fx_k_1, Fx_k):
            #     return 'bad', 'param'
    
    while a == -1000000000000 or b == 1000000000000:
    # Fx_k_1 > Fx_k:
            if Fx_k_1 <= Fx_k:
                if h > 0:
                    b = x0 + 2**(k-1)*h
                else:
                    a = x0 + 2**(k-1)*h
            else:
                if h>0:
                    a =  x0 + 2**(k-2)*h
                else:
                    b = x0 + 2**(k-2)*h
            k += 1
            Fx_k_1 = Fx_k
            Fx_k = Function(x0 + (2**(k-1))*h)

            # if not nullCheck(Fx_k_1, Fx_k):
            #     return 'bad', 'param'

    return min(a,b), max(a,b)
    
        
        

