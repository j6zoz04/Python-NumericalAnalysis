#借用3-3的程式，觀察由不同起始點(x0)出發，收斂的速度快慢
#試著將x0設為 -0.5,-1,2,1.256,1.26
import numpy as np

def g(x):
        return np.log(2*x+1) 
#在numpy模組中，函式log預設為ln

tol=10**(-12)
i=0
x0=-0.4
x1=g(x0)

while abs(x1-x0)>tol:
    print(i,x1)
    i=i+1
    x0=x1
    x1=g(x0)

#由-0.5出發，收斂至0
#由-1出發，收斂至0
#由2出發，收斂至1.25643..
#由1.26出發，收斂至1.25643..

#由不同起始點出發，會收斂到不同的根(0 or 1.25643..)