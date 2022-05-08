# import the necessary packages
import argparse
from PIL import Image
import cv2
import numpy as np
import zbarlight

# construct the argument parse and parse the arguments
def detect(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	ret,thresh = cv2.threshold(gray,127,255,0)
	im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	mask = np.ones(image.shape[:2], dtype="uint8") * 255

	gmbar = Image.open(mask)
	gmbar.load()

	codes = zbarlight.scan_codes('qrcode', gmbar)
	print('QR codes: %s' % codes)