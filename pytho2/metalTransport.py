# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:26:44 2017

@author: Niko
"""
#%%
def yht(arr, dim = 2):
    tulos = [0 for i in range(dim)]
    for coords in arr:
        for i,v in enumerate(coords):
            tulos[i] += v
    return tulos

#%%
def hypot(x):
    total = 0
    for i in x:
        total += i**2
    return total**len(x)
#%%
class asia:
    def __init__(self, name, mass, pos = (0,0), vel = (0,0)):
        self.name = name
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.momentum = mass* hypot(vel)
3