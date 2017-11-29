#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:10:14 2017

@author: rahul
"""


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score


def train_LR(trainX, trainY):
    model = LogisticRegression(penalty='l2', C=1.0, fit_intercept=True, random_state=None, solver='liblinear', max_iter=1000, verbose=0, warm_start=True)
    model.fit(trainX, trainY)
    print("Training Score", model.score(trainX, trainY))
    return model


def test_LR(model, testX, testY):
    score = model.score(testX, testY)
    print("Test Score", score)
    return score


def cross_validation_score(model, dataX, dataY, k):
    scores = cross_val_score(model, dataX, dataY, cv=k)
    print("Cross-validated scores:", scores)
    return scores
