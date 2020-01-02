"""
reads csv file to store all shape features
"""
import csv


class Features:
    def __init__(self):
        with open('shape_features.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            self.feature_dict = {}
            for row in csv_reader:
                #print(row)
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    line_count += 1
                    self.feature_dict[row[0]] = row[1:]

            #print(self.feature_dict)