import numpy as np
import cv2
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

def make_gaussian_kernel(size,sigma):
    if size % 2 == 0:
        raise ValueError("Kernel size muts be odd!")

    kernel = np.zeros((size,size))
    center = size//2

    for x in range(size):
     for y in range(size):
            #dist. from centre
      dx = x - center
      dy = y - center

      exponent = -(dx**2 + dy**2) / (2 * sigma**2)
      kernel[x,y] = (1 / (2 * np.pi * sigma**2))

      kerel /= np.sum(kernel)
      return kernel


def apply_gauss_blur(image,kernel_size, sigma):
   kernel = make_gaussian_kernel(kernel_size,sigma)

   blurred_channel = []
   for i in range(3):
      #for RGB img
      blurred_channel = convolve2d(image[:,:,i],kernel,mode="same",boundary="symm")
      blurred_channel.append(blurred_channel)
   #
   blurred_image = np.stack(blurred_channel,axis=-1)#merging channels back

   blurred_image = np.clip(blurred_image, 0, 255).astype(np.uint8)

   return blurred_image
      

if __name__ == "__main__ ":
   img = cv2.imread("C:/Dev/Python/fd_one/SacKern.png")
   if img is None:
      print("No Image")
      exit()
   rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

   custom_blur = apply_gauss_blur(rgb_img, kernel_size=15, sigma = 20)

   fig,axes = plt.subplots(1,3,figsize=(15,5))
   axes[0].imshow(rgb_img); axes[0].set_title("original image")
   axes[1].imshow(custom_blur); axes[1].set_title("our blurred image")
   plt.show()