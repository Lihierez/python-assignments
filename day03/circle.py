import math
import argparse

parser= argparse.ArgumentParser()
parser.add_argument('--radius',help='Radius of the circle', required=True, type=int)
args=parser.parse_args()
radius = args.radius
area= math.pi * radius**2
circumference= 2*math.pi* radius
print('circle area is:', area)
print('circle circumference is:', circumference)python circle.py --radius 5