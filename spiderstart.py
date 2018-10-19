# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:57:57 2018

@author: johnh
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from scipy import spatial

def blob(u1,sig1,u2,sig2,n,c):
    x=np.random.normal(u1,sig1,n)
    y=np.random.normal(u2,sig2,n)
    z=np.ones(n)
    z=c*z
    w=np.append(x,y)
    w=np.append(w,z)
    w.shape=(3,n)
    w=w.T
    return w

def centroid(z):
    cx=np.average(z[:,0])
    cy=np.average(z[:,1])
    return cx,cy

blob1=blob(5,.5,5,.5,100,1)
blob2=blob(2,1,2,1,100,2)

cx1=np.amax(blob1[:,0])
cy1=np.amax(blob1[:,1])
cx2=np.amin(blob2[:,0])
cy2=np.amin(blob2[:,1])
cent1=np.array([cx1,cy1])
cent2=np.array([cx2,cy2])

mass=np.append(blob1,blob2)

mass.shape=(200,3)

plt.plot(mass[:,0],mass[:,1],'bo',cent1[0],cent1[1],'rd',cent2[0],cent2[1],'gd')


