"""
Performs k-means algorithm
"""
from pyclustering.cluster.kmeans import kmeans
import numpy as np
from pyclustering.utils import read_sample, calculate_distance_matrix
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.samples.definitions import FCPS_SAMPLES
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer

"""
args: features obtained from csv file for each shape
stores: cluster results in varuable cluster_dict
"""
class Cluster:
    def __init__(self, features):

        final_feat = []
        for img, arr in features.items():
            final_feat.append([int(arr[0]), int(arr[-1])])
        print(final_feat)

                # Load list of points for cluster analysis.
        sample = read_sample(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS)
        # Prepare initial centers using K-Means++ method.
        initial_centers = kmeans_plusplus_initializer(sample, 2).initialize()

        matrix = calculate_distance_matrix(final_feat)

        init = [3,2,4,5,6]
        k_means_int = kmeans(final_feat, initial_centers)
        k_means_int.process()
        clusters = k_means_int.get_clusters()
        
        re_clustered = [[item + 1 for item in list] for list in clusters]

        group_num = 0
        self.cluster_dict = {}
        for group in re_clustered:
            group_num += 1 
            for img in group:
                self.cluster_dict[img] = group_num


