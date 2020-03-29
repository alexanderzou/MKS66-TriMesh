from display import *
from draw import *
from parse import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()

parse_file( 'script', edges, polygons, transform, screen, color )

screen = new_screen()
color = [ 0, 255, 255 ]
edges = []
polygons = []
transform = new_matrix()

parse_file('orbit',edges,polygons,transform,screen,color)