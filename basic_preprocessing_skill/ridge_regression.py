#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:08:35 2020

@author: aurora
"""

from lasso_regression import LassoRegression

class RidgeRegression(LassoRegression):
    
    def __init__(self,x,y):
        
        super(RidgeRegression,self).__init__(x,y)
        
    
    def cost_function(self):
        
        ss = []
        for i in range(len(self.x)):
            s = 0
            for j in range(len(self.x[0])):
                s += self.x[i][j] * self.w[j]
            ss.append(s + self.b)
            s = 0
        print(ss)
        js = 0   
        for j in self.w:
            js += pow(j,2)
        
        mse = 0
        
        for i in range(len(self.x)):
            mse += pow((ss[i] - self.y[i]),2)
        mse /= (len(self.x) * 2)
        
        return mse + self.alpha * js / 2 
        
    def show(self):
        print(self.x)
        print(self.y)
        print(self.w)
        
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
                    ws.append((ts[i] - self.y[i]) * self.x[i][j] + self.w[j])
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