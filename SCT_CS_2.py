# Task 2: Develop a simple image encryption tool using pixel manipulation. Support operations like swapping pixel values or applying a basic mathematical operation to each pixel.

# import the required libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# define the encryption function
def encrypt_image(img_array):
        # swap the red and blue channels
        img_array[:,:,0], img_array[:,:,2] = img_array[:,:,2], img_array[:,:,0]
        return img_array

# load the image
img = Image.open('offer.jpg')

# convert the image to a numpy array
img_array = np.array(img)

# display the image
plt.imshow(img_array)
plt.show()

# encrypt the image
encrypted_img_array = encrypt_image(img_array)

# display the encrypted image
plt.imshow(encrypted_img_array)
plt.show()

# save the encrypted image
encrypted_img = Image.fromarray(encrypted_img_array)
encrypted_img.save('encrypted_image.jpg')