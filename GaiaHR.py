# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:00:44 2021

@author: Anthony
"""
import numpy as np
import matplotlib.pyplot as plt

rawdata = np.genfromtxt('HRData.txt', skip_header = 3, delimiter="\t")
nanfilter = rawdata[~np.isnan(rawdata).any(axis=1)]

Gmag = nanfilter[:,0]
BPmag = nanfilter[:,1]
RPmag = nanfilter[:,2]
Dist = nanfilter[:,3]

DistPc = Dist*1000

AbsMag = Gmag - 5*np.log10(DistPc / 10)
colorIndex = BPmag - RPmag

plt.figure(figsize = (6, 7))
plt.title("Hertzsprung-Russel Diagram")
plt.xlabel("Color Index $G_{BP}-G_{RP}$ [mag]")
plt.ylabel("Absolute Magnitude [mag]")
plt.scatter(colorIndex, AbsMag, s = 0.1, c = 'k')
plt.gca().invert_yaxis()

#plt.savefig("Gaia5.png", dpi=300)