print("\033c")

#p1

x = float(input('Input x with 1 decimal place: '))

 # f(x) = 4x^4 + 8x^2 + 2x + 7
poly = [7.0, 2.0, 8.0, 0, 4.0]
def EvalPoly(poly, x):
    y = 0
    #uses both place AND value of tuple
    for index, value in enumerate(poly):
        Piece = value*(x ** index)
        y = y + Piece
    return(y)
print(EvalPoly(poly, x))


# #p2

# f(x) = 4x^4 + 8x^2 + 2x + 7
Poly = (7.0, 2.0, 8.0, 0, 4.0)
def DerivPoly(Poly):
    Deriv = []
    #uses both place AND value of tuple
    for index, value in enumerate(Poly):
        value = (value*index)
        index = index - 1
        if index >= 0:
            Deriv.insert(index, value)
    return(Deriv)
print(DerivPoly(Poly))


#p3 - only issue is negatives arent working

# f(x) = x4 + 3x3 + 17.5x2 + 13.3
Poly = (13.3, 0.0, 17.5, 3.0, 1.0)


E = .0001
x = .1

#calculates value of derivative with value x
def EvalDeriv(Poly, x):
    DerivValue = 0
    #uses both place AND value of tuple
    for index, value in enumerate(Poly):
        value = (value*index)
        index = index - 1
        DerivValue = DerivValue + value*(x ** index)
    return(DerivValue)

#finding root x of poly
def RootPoly(Poly, x):
    while True:
        y = 0
        #uses both place AND value of tuple
        #evaluates poly for value x
        for index, value in enumerate(Poly):
            Piece = value*(x ** index)
            y = y + Piece
        if y <= E and y >= -E:
            # x = abs(x)
            print('root of polynomial is: ', x)
            break
        #changes x value
        else:
            DerivValue = EvalDeriv(Poly, x)
            x = (x - y)/DerivValue
    return x

RootPoly(Poly, x)

