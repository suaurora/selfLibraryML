#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:26:03 2020

@author: aurora
"""
import random

random.seed(1)

class LassoRegression:
    
    
    def __init__(self,x,y,alpha = 0.01,epochs = 100000):
        self.x = x
        self.y = y
        self.w = [float("{:02.2f}".format(random.random())) for i in range(len(self.x[0]))]
        self.b = 1
        self.alpha = alpha 
        self.epochs = epochs
    
    def show_parameters(self):
        print("weight: ")
        print(self.w)
        
    def check_input(self):
        assert len(self.x) == len(self.y)
        
    def cost_function(self):
        y_pred = []
        y_element = 0
        for i in range(len(self.x)):
            for j in range(len(self.x[0])):
                y_element += self.w[j] * self.x[i][j]
            y_pred.append(y_element + self.b)
            y_element = 0
        print(y_pred)
            
        mse = 0
        for i in range(len(y_pred)):
            mse += pow((y_pred[i] - self.y[i]),2)
        mse = mse / (2 * len(y_pred))
        l1_norm = 0
        for i in range(len(self.w)):
            l1_norm += abs(self.w[i])
        return mse + self.alpha * l1_norm
    
    def mse(self,y,y_real):
        s = 0
        for i in range(len(y)):
            s += (y[i] - y_real[i]) ** 2
        return s / len(y) / 2
    
    def predict(self,weight,bais):
        pred = []
        for j in range(len(self.x)):
            s = 0
            for i in range(len(self.x[0])):
                s += weight[i] * self.x[j][i]
            pred.append(s + bais)
        return pred
    
    def sgd(self):
        for i in range(self.epochs):   
            ts = []
            for i in range(len(self.x)):
                n = 0
                for j in range(len(self.x[0])):
                    n += self.w[j] * self.x[i][j] + self.b
                ts.append(n)
            tm = []
            bs = []
            for i in range(len(self.x)):
                ws = []
                for j in range(len(self.x[0])):
                    if self.w[j] >= 0 :
                        ws.append((ts[i] - self.y[i]) * self.x[i][j] + self.alpha)
                    else:
                        ws.append((ts[i] - self.y[i]) * self.x[i][j] - self.alpha)
                bs.append((ts[i] - self.y[i]))
                tm.append(ws)
            tt = []
            tb = 0
            for i in range(len(self.x)):
                tb += bs[i]
            mtb = tb / len(self.x)
            self.b -= self.alpha * mtb
            for i in range(len(self.x[0])):
                t = 0
                for j in range(len(self.x)):
                    t += tm[j][i]
                t /= len(self.x)
                tt.append(t)
            for j in range(len(self.w)):
                self.w[j] -= self.alpha * tt[j]
                    
        return self.w,self.b