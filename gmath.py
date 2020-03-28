import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot product of a . b
def dot_product(a, b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    
def cross_product(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    x = polygons[i]
    y = polygons[i+1]
    z = polygons[i+2]
    a = [y[0]-x[0],y[1]-x[1],y[2]-x[2]]
    b = [z[0]-x[0],z[1]-x[1],z[2]-x[2]]
    return cross_product(a,b)
