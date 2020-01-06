#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:54:23 2020

@author: aurora
"""

import random

random.seed(1)

class Regression:
    
    def __init__(self,x,y,alpha = 0.01,epochs = 100):
        [x[i].append(1) for i in range(len(x))]
        self.x = x 
        self.y = y
        self.weight = [float("{0:2.2f}".format(random.random())) 
                        for i in range(len(x[0]))]
        self.ss = []
        self.alpha = alpha
        self.epochs = epochs
        
    def show(self):
        print(self.x)
        print(self.y)
        print(self.weight)
        
    def evaluate(self,x):
        for j in range(len(x)):
            s = 0
            for i in range(len(x)):
                s += self.weight[i] * x[j][i]
            self.ss.append(s)
        return self.ss
    
    def mse(self,y,y_real):
        s = 0
        for i in range(len(y)):
            s += (y[i] - y_real[i]) ** 2
        return s / len(y) / 2
    
    def predict(self,weight):
        a = []
        s = 0
        for j in range(len(self.x)):
            for i in range(len(weight)):
                s += weight[i] * self.x[j][i]
            a.append(s)
        return a 
    
    def sgd(self):
        for i in range(self.epochs):   
            ts = []
            for i in range(len(self.x)):
                n = 0
                for j in range(len(self.x[0])):
                    n += self.weight[j] * self.x[i][j]
                ts.append(n)
            tm = []
            for i in range(len(self.x)):
                s = []
                for j in range(len(self.x[0])):
                    s.append((ts[i] - self.y[i]) * self.x[i][j])
                tm.append(s)
            tt = []
            for i in range(len(self.x[0])):
                t = 0
                for j in range(len(self.x)):
                    t += tm[j][i]
                t /= len(self.x)
                tt.append(t)
            for j in range(len(self.weight)):
                self.weight[j] -= self.alpha * tt[j]
                    
        return self.weight
        
x = [[1,2,3,4],[5,6,7,8]]
y = [2,6]

reg = Regression(x,y)
reg.show()
weight = reg.sgd()
y_ = reg.predict(weight)
print(reg.mse(y_,y))
y_1 = reg.predict([0.13, 0.85, 0.76, 0.26, 0.5])
print(reg.mse(y_1,y))
print("*" * 10)
print(weight)
print()
print("*" * 10)