import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 as cv


data = pd.read_csv('fer2013/fer2013/fer2013.csv')
data.head()
length=len(data['pixels'])
per_length=len(data['pixels'][0])
print(length,per_length)
for q in range(0,length):
  face = np.fromstring(data['pixels'][q], dtype=int, sep=' ')
  exp = np.zeros((48,48))
  k = 0
  for i in range(len(exp)):
    for j in range(len(exp[0])):
      exp[i][j] = face[k]
      k = k + 1
  imgplot = plt.imshow(exp, cmap='gray')
  #plt.show()
  print("Saving image "+str(q))
  mpimg.imsave("Images/image"+str(q)+".jpg",exp)
