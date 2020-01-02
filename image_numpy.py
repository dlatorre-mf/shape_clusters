"""
Converts images to numpy pixel arrays
"""
import os
from PIL import Image
import numpy as np 
from skimage.io import imread

"""
args: path to images folder
stores: numpy arrays in var - image_dict
"""
class ConvertNumpy:
    def __init__(self, path):
        self.path = path
        pre_dict = {}
        for filename in os.listdir(self.path):  
            if filename.endswith("jpeg"):       
                img = Image.open(self.path + "/" + filename)
                
                im = np.array(img)
                im = im[:,:,0]
              
                file_num = filename.replace("Slide", "").replace(".jpeg", "")
                pre_dict[int(file_num)] = im
        self.image_dict = {}
        for key in sorted(pre_dict.keys()):
            self.image_dict[key] = pre_dict[key]
      