import cv2
c = {}
for i in range(255):
    c[i] = chr(i)
img = cv2.imread("/content/encryptedImage.png")
message=""
n = 0
m = 0
z = 0
passw = input("Enter passcode for Decryption")
if passw == "abc123":
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
