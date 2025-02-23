import cv2
import os
import string

img = cv2.imread("idle_logo.png") # Replace with the correct image path

msg = input("Enter secret message:")
#password = input("Enter a passcode:")

d = {}

for i in range(255):
    d[chr(i)] = i

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)
print("The Encryption was done successfully and image is saved")
