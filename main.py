"""
Main File to perform the following: 
 - read csv shapes and load 50 images
 - get distance matrix for each matrix
 - perform clustering and save results onto csv

 TODO: Obtain behavioral data to perform measured comparison of all clusters
"""
import read_csv
import image_numpy
import allmetrics
import k_medoids
import k_means
import write_csv


class Main:
    def __init__(self):
        features = read_csv.Features().feature_dict
   
        img_numpy = image_numpy.ConvertNumpy("all_shapes").image_dict   
        dist_object = allmetrics.DistanceMatrix(img_numpy)
        l2_dist_matrix = dist_object.L2Distance()
        haurdoff_dist_matrix = dist_object.Hausdorff_dist()

        moments_inertia = dist_object.Moments_inertia()

        l2_clusters = k_medoids.Cluster(l2_dist_matrix).cluster_dict
        hauss_clusters = k_medoids.Cluster(haurdoff_dist_matrix).cluster_dict
        
        minertia_clusters = k_medoids.Cluster(moments_inertia).cluster_dict
        kmeans_clusters = k_means.Cluster(features).cluster_dict

        write_csv.Write(features, l2_clusters, hauss_clusters, minertia_clusters, kmeans_clusters)

     
  

Main()
