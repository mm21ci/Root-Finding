import matplotlib.pyplot as plt
import numpy as np

#gets the real roots
def foundReal(roots):
    realRoots = []
    for i in roots:
        if (np.isreal(i)):
            realRoots.append(i)
    print(realRoots)
    return (realRoots)

#checks if root was found
def foundRoot(roots, root):
    found = False
    for item in realRoots:
        if root == item:
            print("found correct root!")
            found = True
            break
    return (found)


#goes through the bisectionMethod to get a close enough root
def bisectionMethod(a, b, TOL, maxIt, f, i=1):
    FA = f(a)
    ps = []
    while (i <= maxIt):
        p = a + (b - a)/2
        ps.append(p)
        FP = f(p)
        if (FP == 0 or ((b-a)/2 < TOL)):
            print ("Number of Iterations for bisection method: ", i)
            print("Root found with Bisection Mehtod: ", p)
            return p, i, ps
        i += 1
        if (FA*FP > 0):
            a = p
            FA = FP
        else:
            b = p
    print("finished after N0 iterations, N0=", maxIt)

#Newton's method for faster root finding
def newtonMethod(p0, TOL, maxIt, f, fderiv):
    i = 1
    ps = []
    while (i <= maxIt):
        p = p0 - f(p0)/fderiv(p0)
        ps.append(p)
        if (abs(p - p0) < TOL):
            return(p, i, ps)
        i += 1
        p0 = p
    print("Method failed after N0 iterations, N0 = ", maxIt)

# creating an empty list
lst = []
  
# number of elements as input
n = int(input("Enter number of terms in the polynomial: "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input("enter coefficiants(starting with constant and ending with highest power of x): "))
  
    lst.append(ele) # adding the element
      
#creates a polynomial function
func = np.polynomial.Polynomial(lst)

#calculates the derivative
fderiv = func.deriv()

#find all roots for error checking
roots = func.roots()

#finds the estimation of the root using bisection method
for r in roots: 
    startLft = float(input("Please input the left starting interval: "))
    startRight = float(input("Please input the right starting interval: "))

    root, i, p = bisectionMethod(startLft, startRight, 0.00000000000001, 100, func)

    errors = []
    for x in p: 
        if x == 0:
            errors.append(root)
        else: 
            fnd = abs((root - x)/x)
            errors.append(fnd)

    k=[]
    j=1
    while i != 0:
        k += [j]
        j += 1
        i -= 1

    plt.plot(k, errors)
    plt.axhline(y=0, c="black")
    plt.axvline(x=0, c="black")
    plt.show()

#finds estimation of root using Newton's method

for r in roots: 
    root = input("Give root estimation: ")
    root, j, jr = newtonMethod(-1, 0.00000000000001, 20, func, fderiv)
    print ("Root found with Newton's method: ", root)
    print ("Number of iterations with Newton's method: ", j)
    errors2 = []
    for x in jr: 
        if x == 0:
            errors.append(root)
        else: 
            fnd = abs((root - x)/x)
            errors2.append(fnd)


    s=[]
    l=1
    while j != 0:
        s += [l]
        l += 1
        j -= 1


    plt.plot(s, errors2)
    plt.axhline(y=0, c="black")
    plt.axvline(x=0, c="black")
    plt.show()

#finds estimation of root using a combined method
for r in roots: 
    startLft = float(input("Please input left starting interval: "))
    startRight = float(input("Please input the right starting interval: "))
    root, i, p = bisectionMethod(startLft, startRight, 0.1, 20, func)

    #calculate errors of each iteration
    errors = []
    for x in p: 
        if x == 0:
            errors.append(root)
        else: 
            fnd = abs((root - x)/x)
            errors.append(fnd)

    k=[]
    j=1
    while i != 0:
        k += [j]
        j += 1
        i -= 1


    #is the root exactly correct
    realRoots = foundReal(roots)
    found = foundRoot(realRoots, root)
    print("Estimation of root found with bisection method: ",root)

    #if not exactly correct, run it through Newton's Method
    if found == False:
        root, j, jr = newtonMethod(root, 0.00000000000001, 20, func, fderiv)
        print("Root found with Newton's Method: ", root)
    print("Number of iterations for Newton's Method: ", j)

    #gets the error of the found root compared to the real root
    for item in realRoots: 
        error = abs((root - item)/item)
        print("Error is: ", error)

    errors2 = []
    for x in jr: 
        if x == 0:
            errors.append(root)
        else: 
            fnd = abs((root - x)/x)
            errors2.append(fnd)


    s=[]
    l=1
    while j != 0:
        s += [l]
        l += 1
        j -= 1

    plt.plot(k, errors)
    plt.axhline(y=0, c="black")
    plt.axvline(x=0, c="black")
    plt.show()

    plt.plot(s,errors2,color="red")
    plt.axhline(y=0, c="black")
    plt.axvline(x=0, c="black")
    plt.show()


#prints plot for comparison
x = []
y = []
i = -20
while (i != 10):
    x.append(i)
    y.append(func(i))
    i += 1
    if i == 10:
        break
plt.plot(x, y)
plt.axhline(y=0, c="black")
plt.axvline(x=0, c="black")

plt.show()
