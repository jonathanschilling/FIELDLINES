#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 19:59:28 2021

@author: jonathan
"""

import h5py
import os
import numpy as np

from netCDF4 import Dataset

from MinervaSettings import MinervaSettings
import matplotlib.pyplot as plt

#%%

# outFolder = os.path.join(MinervaSettings.getAppsResultPath(),
#                          "StellaratorOptimization",
#                          "Alan_QI",
#                          "Best")
# case = "Free"

outFolder = "."
case = "vmec"

fieldlines_filename = os.path.join(outFolder, "fieldlines_"+case+".h5")

f = h5py.File(fieldlines_filename, "r")
pLines = f["PHI_lines"][()]
rLines = f["R_lines"][()]
zLines = f["Z_lines"][()]
f.close()

#%%

#for i in range(3):
#   plt.figure()
#   plt.plot(pLines[:-1,i], rLines[:-1,i], label="R")
#   plt.plot(pLines[:-1,i], zLines[:-1,i], label="Z")
#   plt.legend()
#   plt.grid(True)
#   plt.title("line %d"%(i,))

#plt.show()

#%%
#
# # Fourier coeffs from DESCUR output
# xm = [0,  0,  0,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2]
# xn = [0,  1,  2, -2, -1,  0,  1,  2, -2, -1,  0,  1,  2]
# rbc = [ 9.845142E-01,
#         3.538540E-02,
#        -1.904323E-01,
#         4.460541E-02,
#        -2.521955E-02,
#         8.572083E-02,
#        -1.528670E-02,
#        -4.263108E-03,
#        -5.182797E-03,
#         2.516050E-03,
#        -7.187893E-03,
#         1.449150E-03,
#         6.080993E-04]
# zbs = [ 0.000000E+00,
#         3.938309E-01,
#        -1.214476E-01,
#        -4.878118E-02,
#         1.359456E-02,
#         1.537456E-01,
#         3.661707E-03,
#         8.733406E-05,
#         6.163942E-03,
#        -9.781185E-03,
#        -1.631337E-02,
#         5.817391E-04,
#        -4.769565E-04]
#
# # flux surface from DESCUR
# def evalFsDESCUR(phi, numTheta = 100):
#     allR = []
#     allZ = []
#
#     for i in range(numTheta):
#
#         theta = i * 2.0*np.pi/(numTheta - 1.0)
#
#         r = 0.0
#         z = 0.0
#
#         for mn, m in enumerate(xm):
#             n = xn[mn]
#
#             kernel = m * theta - n * phi
#
#             r += rbc[mn] * np.cos(kernel)
#             z += zbs[mn] * np.sin(kernel)
#
#         allR.append(r)
#         allZ.append(z)
#
#     return allR, allZ
#
# wout = Dataset("wout_Free.nc")
# ns = wout["ns"][()]
# print("ns=%d"%(ns,))
#
# xmVMEC = wout["xm"][()]
# xnVMEC = wout["xn"][()]
# rmnc = wout["rmnc"][()]
# zmns = wout["zmns"][()]
#
# wout.close()
#
# def evalFsVMEC(phi, numTheta=100):
#
#     allFsRZ = []
#
#     for js in range(ns):
#
#         allR = []
#         allZ = []
#
#         for i in range(numTheta):
#
#             theta = i * 2.0*np.pi/(numTheta - 1.0)
#
#             r = 0.0
#             z = 0.0
#
#             for mn, m in enumerate(xmVMEC):
#                 n = xnVMEC[mn]
#
#                 kernel = m * theta - n * phi
#
#                 r += rmnc[js, mn] * np.cos(kernel)
#                 z += zmns[js, mn] * np.sin(kernel)
#
#             allR.append(r)
#             allZ.append(z)
#
#         allFsRZ.append((allR, allZ))
#
#     return allFsRZ
#
#
#
#
#
#
#
#
# copied from FIELDLINES input
npoinc = 72
nturn = 100 # == floor(PHI_END/(2 pi))

#strt = 0
#for strt in range(npoinc):
for strt in range(1):
    plt.figure()
    # iterate over all fieldlines == flux surfaces
    for i in range(len(rLines[0,:])):
        plt.plot(rLines[strt::npoinc,i], zLines[strt::npoinc,i], '.')
#
#     phi = strt * 2.0*np.pi/npoinc
#
#     rDESCUR, zDESCUR = evalFsDESCUR(phi)
#     plt.plot(rDESCUR, zDESCUR, label="DESCUR")
#
#     allFsRZ = evalFsVMEC(phi)
#     for fs in allFsRZ:
#         rVMEC, zVMEC = fs
#         plt.plot(rVMEC, zVMEC, label="VMEC")
#
    plt.xlabel("R / m")
    plt.ylabel("Z / m")
    plt.axis("equal")
    plt.grid(True)
    plt.title("Poincare and flux surface at strt="+str(strt))
#    plt.legend(loc='upper right')

plt.show()

# # make DESCUR input
#
# numTheta = nturn
# numPhi = npoinc
# nfp = 1
#
# idxRadial = 0
#
# with open("surf.dat", "w") as f:
#     f.write("%d %d %d\n"%(numTheta, numPhi, nfp))
#
#     for idxPhi in range(numPhi):
#
#         for idxTheta in range(numTheta):
#
#             # in the linear-indexed FIELDLINES output,
#             # npoinc == numPhi is the fast index
#             # and numTheta is the slow index
#
#             lindx = idxTheta * numPhi + idxPhi
#
#             r = rLines[lindx, idxRadial]
#             p = pLines[lindx, idxRadial]
#             z = zLines[lindx, idxRadial]
#             f.write("%.6e %.6e %.6e\n"%(r, p, z))
