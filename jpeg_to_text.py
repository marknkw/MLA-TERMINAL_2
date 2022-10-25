# Python code to convert an image to txt
from io import TextIOWrapper
import sys
import random
import argparse
from typing import Any, Literal
from typing_extensions import LiteralString
import numpy as np
import math
import func as terminal 
from PIL import Image
 

# 70 levels of gray
gscale1: Literal['$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]…'] = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\^`.'
 
# 10 levels of gray
gscale2: Literal['@%#*+=-:. '] = '@%#*+=-:. '
 
def getAverageL(image) -> Any:
 
    """
    Given PIL Image, return average value of grayscale value
    """
    # get image as numpy array
    im = np.array(image)
 
    # get shape
    w,h = im.shape
 
    # get average
    return np.average(im.reshape(w*h))
 
def covertImageToAscii(fileName, cols, scale, moreLevels):
    """
    Given Image and dims (rows, cols) returns an m*n list of Images
    """
    # declare globals
    global gscale1, gscale2
 
    # open image and convert to grayscale
    image: Image = Image.open(fileName).convert('L')
 
    # store dimensions
    W, H = image.size[0], image.size[1]
    terminal.delay_print("input image dims: %d x %d" % (W, H))
 
    # compute width of tile
    w = W/cols
 
    # compute tile height based on aspect ratio and scale
    h = w/scale
 
    # compute number of rows
    rows = int(H/h)
     
    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))
 
    # check if image size is too small
    if cols > W or rows > H:
        terminal.delay_print("Image too small for specified cols!")
        exit(0)
 
    # ascii image is a list of character strings
    aimg = []
    # generate list of dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
 
        # correct last tile
        if j == rows-1:
            y2 = H
 
        # append an empty string
        aimg.append("")
 
        for i in range(cols):
 
            # crop image to tile
            x1: int = int(i*w)
            x2: int = int((i+1)*w)
 
            # correct last tile
            if i == cols-1:
                x2 = W
 
            # crop image to extract tile
            img = image.crop((x1, y1, x2, y2))
 
            # get average luminance
            avg: int = int(getAverageL(img))
 
            # look up ascii char
            if moreLevels:
                gsval: str = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
 
            # append ascii char to string
            aimg[j] += gsval
     
    # return txt image
    return aimg
 
def main() -> None:
    # create parser
    descStr: Literal['This is converting PIL jpegs to txt to be animated…'] = "This is converting PIL jpegs to txt to be animated."
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=descStr)
    # add expected arguments
    parser.add_argument('--file', dest= 'imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true')
 
    # parse args
    args: argparse.Namespace = parser.parse_args()
   
    # set input file
    imgFile: Literal['./resourses/sphere/sphere_jpgs/sphere.jpeg'] = './resourses/sphere/sphere_jpgs/sphere.jpeg'
    if args.imgFile:
        imgFile = args.imgFile
 
    # set output file
    outFile: Literal['./resourses/sphere/out.txt'] = './resourses/sphere/out.txt'
    if args.outFile:
        outFile = args.outFile
 
    # set scale default as 0.43 which suits
    # a Courier font
    scale = 0.43
    if args.scale:
        scale: float = float(args.scale)
 
    # set cols
    cols: Literal[80] = 80
    if args.cols:
        cols = int(args.cols)
 
    terminal.delay_print('Transforming jpg into text...')
    # convert image to ascii txt
    aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels)
 
    # open file
    f: TextIOWrapper = open(outFile, 'w+')
 
    # write to file
    for row in aimg:
        f.write(row + '\n')
 
    # clean
    f.close()
    terminal.delay_print("Text file written to %s" % outFile)
 
# call main without worring about function's order
if __name__ == '__main__':
    main()