# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 22:02:29 2021

@author: Adarsh
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans


iris = pd.read_csv('D:\\Internship\\Iris.csv')
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris)
iris_df.head()





















