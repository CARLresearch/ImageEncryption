#Arnold Cat Map Shuffling for sqaure images

def transform_ac(img, times_shuffled=1, p=1,q=1):                                                        #arnold cat map
    n=img.shape[0]
    output = np.zeros([n, n])
    for itr in range(times_shuffled):
        for x in range(0, n):
            for y in range(0, n):
                output[x][y] = img[(x+p*y)%n][(q*x+(p*q+1)*y)%n]
#         cv.imwrite('test/'+str(itr).zfill(2)+'.png', output)
#     cv.imwrite('testfinal/'+str(itr).zfill(2)+'.png', output)
    return output

#Driver Code
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('/home/aditya/Desktop/res_img/lena/lena.png',0)
shuffled_img = transform_ac(img)
print shuffled_img
plt.imshow(shuffled_img)