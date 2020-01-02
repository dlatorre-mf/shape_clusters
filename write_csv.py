"""
writes cluster results onto csv file
"""

import csv

"""
args: all cluster results
"""
class Write:
    def __init__(self, feat, l2clusters, hclusters, inertiaclusters, kmeans):
        final_dict = {}
        for k,v in l2clusters.items():
            newl = feat[str(k)]
            newl.append(v)
            newl.append(hclusters[k])
            newl.append(inertiaclusters[k])
            newl.append(kmeans[k])
            final_dict[str(k)] = newl

        with open('final_shapes.csv', 'w') as f:
            fwriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for key in final_dict.keys():
                rowl = [key, final_dict[key]]
                fwriter.writerow(rowl)

