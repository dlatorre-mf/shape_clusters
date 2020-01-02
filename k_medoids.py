"""
Performs k-medoids algorithm on shapes
"""
from pyclustering.samples.definitions import SIMPLE_SAMPLES
from pyclustering.cluster import cluster_visualizer
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.utils import read_sample
from pyclustering.utils import read_sample, calculate_distance_matrix
from pyclustering.samples.definitions import FCPS_SAMPLES


"""
args: distance matrix for all 50 shape images
stires: cluster results in variable cluster_dict
"""
class Cluster:
    def __init__(self, matrix):
     
      
        initial_medoids = [1,2,3,4,5]
    
        kmedoids_instance = kmedoids(matrix, initial_medoids)
        
        kmedoids_instance.process()

        clusters = kmedoids_instance.get_clusters()
  
        medoids = kmedoids_instance.get_medoids()
   

        re_clustered = [[item + 1 for item in list] for list in clusters]

        group_num = 0
        self.cluster_dict = {}
        for group in re_clustered:
            group_num += 1 
            for img in group:
                self.cluster_dict[img] = group_num

     

