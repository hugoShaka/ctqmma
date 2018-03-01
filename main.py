#!/usr/bin/python

#Imports librairies
import sys

#Import classes et methodes
from parser import parse
import trajets
import car

#import hugo/mathieu/iris/juliette.py

file = sys.argv[1]
print("opening file" + file)

(R, C, F, N, B, T, rides, cars) = parse(file)

# Have fun :)
