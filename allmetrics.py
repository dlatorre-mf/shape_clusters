"""
Calculates distance matrix for all metrics and shape images
"""

import numpy as np
from scipy.spatial.distance import directed_hausdorff
from skimage.measure import inertia_tensor


"""
args: numpy_arrays containing the pixel information for each image shape

"""
class DistanceMatrix:
    def __init__(self, numpy_arrays):
        self.numpy_arrays = numpy_arrays
  

    def L2Distance(self):
        self.l2_matrix = []
        for im1, arr1 in self.numpy_arrays.items():
            row_dist = []
            for im2, arr2 in self.numpy_arrays.items():
                dist = np.sum((arr1-arr2)**2)
                
                row_dist.append(dist/1000000)
            self.l2_matrix.append(row_dist) 

        return self.l2_matrix

    def Hausdorff_dist(self):
        self.h_matrix = []
        for im1, arr1 in self.numpy_arrays.items():
            row_dist = []
            #print("hey")
            for im2, arr2 in self.numpy_arrays.items():
                dist = directed_hausdorff(arr1,arr2)            
                row_dist.append(dist)
            self.h_matrix.append(row_dist) 
        return self.h_matrix
    
    def Moments_inertia(self):
        self.inertia_matrix = []
        for im1, arr1 in self.numpy_arrays.items():
            row_dist = []     
            for im2, arr2 in self.numpy_arrays.items():
                
                dist = np.sum((inertia_tensor(arr1)-inertia_tensor(arr2))**2) 
            
                row_dist.append(dist/100000)
    
            self.inertia_matrix.append(row_dist) 
        return self.inertia_matrix



