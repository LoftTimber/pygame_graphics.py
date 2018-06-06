#This program contains functions that evaluate formulas used in geometry.
#
#Shane Farral
#9/5/2017

import math

def triangle_area(b,h):
    a=(1/2)*b*h
    return a

def circle_area(r):
    a=math.pi*r**2
    return a

#function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))

def parallelogram_area(b,h):
    a=b*h
    return a

def trapezoid_area(a,b,h):
    A=(a/2+b/2)*h
    return A

def rectangular_prism_volume(w,h,L):
    V=w*h*L
    return V

def cone_volume(r,h):
    V=math.pi*(r**2)*(h/3)
    return V

def sphere_volume(r):
    V=(4/3)*math.pi*r**3
    return V

def rectangular_prism_surface_area(w,L,h):
    A=2*(w*L+h*L+h*w)
    return A

def sphere_surface_area(r):
    A=4*math.pi*r**2
    return A

def right_triangle_hypotenuse(a,b):
    c=math.sqrt(a**2+b**2)
    return c

def herons_formula(A,B,C):
    S=(A+B+C)/2
    R=math.sqrt(S*(S-A)*(S-B)*(S-C))
    return R
