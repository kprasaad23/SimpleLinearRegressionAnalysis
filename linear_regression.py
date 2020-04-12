from linear_regression import BasicStats as stats
from math import sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SimpleLr(object):

    def __init__(self,dataset):
        self.dataset=dataset
        self.x=dataset['X'].tolist()
        self.y=dataset['Y'].tolist()


    # def stats_cal(self):
    #     print("Getting Stats for variables")
    #     stats_obj = stats.BasicStats(self.x, self.y)
    #     print("Mean Value for X : ", stats_obj.mean(self.x))
    #     print("Mean Value for Y : ", stats_obj.mean(self.y))
    #     print("Variance for X : ", stats_obj.variance(self.x))
    #     print("Variance for Y : ", stats_obj.variance(self.y))
    #     print("Covariance for X and Y : ", stats_obj.covariance())

    def coefficients(self):
        b1 = stats.BasicStats(self.x, self.y).covariance() / stats.BasicStats(self.x, self.y).variance(self.x)
        b0 = (stats.BasicStats(self.x, self.y).mean(self.y)) - (b1 * stats.BasicStats(self.x, self.y).mean(self.x))
        return [b1, b0]

    def simple_linear_regression(self):
        prediction=list()
        b1, b0 = self.coefficients()
        for i in range(len(self.x)):
            y_pred = b0 + b1 * self.x[i]
            prediction.append(y_pred)
        return prediction

    def rms_error(self,y_pred):
        sum_error = 0.0
        for i in range(len(self.y)):
            pred_error = y_pred[i] - self.y[i]
            sum_error += (pred_error ** 2)
        mean_error = sum_error / float(len(self.y))
        return sqrt(mean_error)


dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
dataset=pd.read_csv("/insurance.csv")
dataset.columns=['X','Y']
#print(dataset)
#print(dataset['X'].tolist())
lr = SimpleLr(dataset)
print(lr.rms_error(lr.simple_linear_regression()))
