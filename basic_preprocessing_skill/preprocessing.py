#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:24:14 2020

@author: aurora
"""



class preprocessing_scale_slist:
    def __init__(self,x):
        self.x = x 
    
    def __Basic_information_of_Normalization(self):
        s = 0
        for i in self.x:
            s += i
        x_mean = s / len(self.x)        
        x_var = 0
        for j in self.x:
            x_var += (j - x_mean) ** 2
        return x_mean,x_var
        
    def fit_transform_standardization(self):            
        x_mean,x_var = preprocessing_scale_slist.__Basic_information_of_Normalization(self)
        x_new = []
        for i in self.x:
            new_i = (i - x_mean) / (x_var ** 0.5)
            x_new.append(new_i)
        return x_new
    
    def fit_transform_Normalizatoin(self):
        x_max = max(self.x)
        x_min = min(self.x)
        new_x = []
        for i in self.x:
            new_i = (i - x_min) / (x_max - x_min)
            new_x.append(new_i)
        return new_x  
    
class preprocessing_label:
    
    def __init__(self,y):
        self.y = y
    def __assert(self):
        for i in range(len(self.y)):
            assert type(self.y[i]) == type(1)
            
    def onehot(self):
        preprocessing_label.__assert(self)
        y_ = []
        for y_e in self.y:
            y__= [0] * (1 + max(self.y))
            y__[y_e] = 1
            y_.append(y__)

        return y_
    
def train_test_split(x,test_ratio):
    test_length = int(len(x) * test_ratio)
    return x[:test_length],x[test_length:]

import numpy as np

a = np.random.random((10,10))
print(len(a))

a_test,a_train = train_test_split(a,0.2)
print(len(a_train))