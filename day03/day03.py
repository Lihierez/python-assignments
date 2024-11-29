#width = int(input("Enter Width:"))
#height= int(input("Enter height:"))
#area= width * height
#print(area)

import argparse
parser= argparse.ArgumentParser
parser.add_argument('--width', help='Width with pixels', required=True, type=int)
parser.add_argument('--height', help='Height with pixels', required=True, type=int)
args=parser.parse_args()

if ((not args.size and not args.width)):
    exit ("Need euther hieght ot width")

