"""
scan_images.py: A simple Barcode Scanner application that finds barcodes from an image and displays its data.
"""

__author__ = "S Sathish Babu"
__date__   = "19-12-2020 Saturday 23:30"
__email__  = "bumblebee211196@gmail.com"

import argparse

import cv2
from pyzbar import pyzbar

parser = argparse.ArgumentParser("Barcode Scanner")
parser.add_argument('-i', '--image', help="Path to the Image file.", required=True)
args = vars(parser.parse_args())

image = cv2.imread(args['image'])
barcodes = pyzbar.decode(image)

for barcode in barcodes:
    x, y, w, h = barcode.rect
    barcode_data = barcode.data.decode()
    barcode_type = barcode.type
    text = f'{barcode_data} {barcode_type}'
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)
    cv2.putText(image, text, (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

cv2.imshow('Output', image)
cv2.waitKey(0)
