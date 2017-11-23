# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:12:01 2017

@author: Niko
"""
import numpy as np
import scipy.spatial


def main():
    xyz = np.random.random((100, 3))
    area_underneath = trapezoidal_area(xyz)
    print (area_underneath)

def trapezoidal_area(xyz):
    """Calculate volume under a surface defined by irregularly spaced points
    using delaunay triangulation. "x,y,z" is a <numpoints x 3> shaped ndarray."""
    d = scipy.spatial.Delaunay(xyz[:,:2])
    tri = xyz[d.vertices]

    a = tri[:,0,:2] - tri[:,1,:2]
    b = tri[:,0,:2] - tri[:,2,:2]
    proj_area = np.cross(a, b).sum(axis=-1)
    zavg = tri[:,:,2].sum(axis=1)
    vol = zavg * np.abs(proj_area) / 6.0
    return vol.sum()