#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:31:22 2020

@author: aurora
"""


def mse(y_real,y_pred):
    s = 0
    for i in range(len(y_real)):
        s += pow((y_real[i] - y_pred[i]),2)
    return s / 2 / len(y_real)

def recall(y_real,y_pred):
    true_positive = 0
    true_positives = []
    """
    the label of the y_real is ture and we predict it ture
    """
    true_negative = 0
    true_negatives =[]
    """
    the label of the y_real is false and we predict it false
    """
    false_positive = 0
    false_positives = []
    """
    the label of the y_real is false and we perdicy it ture
    """
    false_negative = 0
    false_negatives = []
    """
    the label of the y_real is true and we predict it false
    """
    labels_of_y_real = list(pre_recall(y_real))
    for j in labels_of_y_real: 
        for i in range(len(y_real)):
            if y_real[i] == j and y_pred[i] == j:
                true_positive += 1
            elif y_real[i] == j and y_pred[i] != j:
                false_negative += 1
            elif y_real[i] != j and y_pred[i] == j:
                false_positive += 1
            elif y_real[i] != j and y_pred[i] != j:
                true_negative += 1
        true_positives.append(true_positive)
        true_negatives.append(true_negative)
        false_negatives.append(false_negative)
        false_positives.append(false_positive)
        true_positive = 0
        true_negative = 0
        false_positive = 0
        false_negative = 0
    recall = []
    precision = []
    for i in range(len(labels_of_y_real)):
        recall.append(true_positives[i] / (false_negatives[i] + true_positives[i]))
        precision.append(true_positives[i] / (false_positives[i] + true_positives[i]))
        
        
    return recall,precision

def f1_score(recall,precision):
    f1 = []
    
    for i in range(len(recall)):
        
        assert recall[i] != 0
        assert precision[i] != 0
        f1_ = 2 * (precision[i] * recall[i]) / (precision[i] + recall[i])
        f1.append(f1_)
    return f1

def pre_recall(y_real):
    dict_element = dict()
    for i in range(len(y_real)):
        dict_element[y_real[i]] = dict_element.get(y_real[i],0) + 1
    return dict_element
