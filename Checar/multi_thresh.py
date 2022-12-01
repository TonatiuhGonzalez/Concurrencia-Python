#Código de Tona
from multiprocessing import Pool
from multiprocessing import Process

import numpy as np
import glob
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters

# Read Images
def multi_thresh(threshold):
  
  print(threshold)
  
  img = skimage.io.imread("shapes-01.jpg")
  #img = mpimg.imread('/content/sample_data/tangram.jpg')
  # Output Images

  #fig, ax = plt.subplots()
  #plt.imshow(img)

  # convert the image to grayscale
  gray_image = skimage.color.rgb2gray(img)

  # blur the image to denoise
  blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)

  #fig, ax = plt.subplots()
  #plt.imshow(blurred_image, cmap="gray")
  # create a histogram of the blurred grayscale image
  histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))

  #fig, ax = plt.subplots()
  #plt.plot(bin_edges[0:-1], histogram)
  #plt.title("Grayscale Histogram")
  #plt.xlabel("grayscale value")
  #plt.ylabel("pixels")
  #plt.xlim(0, 1.0)
  # create a mask based on the threshold

  print(type(threshold))

  binary_mask = blurred_image < threshold

  #fig, ax = plt.subplots()
  plt.imshow(binary_mask, cmap="gray")

  # use the binary_mask to select the "interesting" part of the image
  selection = img.copy()
  selection[~binary_mask] = 0

  #fig, ax = plt.subplots()
  #plt.imshow(selection)

value = 0.8
print(type(value))
multi_thresh(value)

#if __name__ == '__main__':
  #with Pool() as p:
  #  numeros = (0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8)
  #  p.map(multi_thresh,numeros)

  #numeros = (0.1)
  #p = Process(target = multi_thresh, args=(numeros,))
  #p.start()
  #p.join()