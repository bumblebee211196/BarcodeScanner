"""
scan_videos.py: A simple Barcode Scanner application that finds barcodes from a video or webcam and displays its data.
"""

__author__ = "S Sathish Babu"
__date__   = "19-12-2020 Saturday 23:30"
__email__  = "bumblebee211196@gmail.com"

import argparse

import cv2
from pyzbar import pyzbar

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--video', help="Path to the video file", default=0)
args = vars(parser.parse_args())

vc = cv2.VideoCapture(args['video'])

while True:
    _, frame = vc.read()
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        barcode_data = barcode.data.decode()
        barcode_type = barcode.type
        text = f'{barcode_data} {barcode_type}'
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Output', frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

vc.release()
cv2.destroyAllWindows()
