import cv2
import math
import numpy

#1
angle=30

img = cv2.imread("calvinHobbes.jpeg")
dim = img.shape

while angle>360:
	angle=angle-360
while angle<0:
	angle+=360
m = cv2.getRotationMatrix2D((0,0),angle,1)
if angle>90 and angle<270:
	m[0][2] += dim[1]*abs(math.cos(math.radians(angle)))
if angle>180:
	m[0][2] += dim[0]*abs(math.sin(math.radians(angle)))
if angle<180:
	m[1][2] += dim[1]*abs(math.sin(math.radians(angle)))
if angle>90 and angle<270:
	m[1][2] += dim[0]*abs(math.cos(math.radians(angle)))

rot = cv2.warpAffine(img,m,
	(math.ceil(dim[0]*abs(math.sin(math.radians(angle)))+dim[1]*abs(math.cos(math.radians(angle)))),
	math.ceil(dim[0]*abs(math.cos(math.radians(angle)))+dim[1]*abs(math.sin(math.radians(angle))))))

cv2.imwrite("rotated.jpg",rot)

#2

scl1=cv2.resize(img,(math.ceil(dim[1]*2.5),math.ceil(dim[0]*2.5)),interpolation = cv2.INTER_NEAREST)
scl2=cv2.resize(img,(math.ceil(dim[1]*2.5),math.ceil(dim[0]*2.5)),interpolation = cv2.INTER_LINEAR)
scl3=cv2.resize(img,(math.ceil(dim[1]*2.5),math.ceil(dim[0]*2.5)),interpolation = cv2.INTER_CUBIC)
cv2.imwrite("scaled nearest neighbour.jpg",scl1)
cv2.imwrite("scaled bilinear.jpg",scl2)
cv2.imwrite("scaled bicubic.jpg",scl3)

#3
m=numpy.float32([[1,0,dim[1]/4],[0,1,dim[0]/2]])
trans = cv2.warpAffine(img, m, (dim[1], dim[0])) 
cv2.imwrite("translation.jpg",trans)
