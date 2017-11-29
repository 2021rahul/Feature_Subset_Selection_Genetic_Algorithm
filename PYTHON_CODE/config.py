#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:13:38 2017

@author: rahul
"""

VERSION = 'GERMAN'

DATASET_FILEPATH = "DATASETS/GERMAN/german.csv"

OUTPUT_FILEPATH = DATASET_FILEPATH[:-4] + "_output.txt"

NUM_FEATURES = 20
POPULATION_SIZE = 30
EQDE_MAXITER = 200
ELITISM = 75

F = 0.4
CR = 0.6

TEST_SIZE = 0.3
