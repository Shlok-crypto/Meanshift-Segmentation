import cv2 as cv

img = cv.imread('MeanShift.jpg')

# Mean Shift the image pixel (X,Y) are confined to their neighborhood in the joint space-color(assign to individual color Hill)
MeanShiftImage = cv.pyrMeanShiftFiltering(img,90,20,)

cv.imshow("Mean Shift Segmentation",MeanShiftImage)
cv.imshow("Original",img)

cv.waitKey(0)
