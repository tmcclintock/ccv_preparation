"""
Use the M-lambda relation from SV to make guesses at M200m to use to make the covariance matrices in ccv.
"""
import numpy as np
path = "/home/tom/Desktop/DES_data/Y1_files/"
zs = np.loadtxt(path+"Y1_meanz.txt")
lams = np.loadtxt(path+"Y1_meanl.txt")
number = np.loadtxt(path+"Y1_number.txt")
Nz = len(zs)
Nl = len(zs[0])
masses = np.zeros_like(zs)
print lams
h = 0.7

def get_mass(z, lam): #Msun/h
    lMp = 14.371 #Msun
    Fl = 1.12
    Gz = 0.18
    return h*10**(lMp + Fl*np.log10(lam/30.) + Gz*np.log10((1+z)/1.5))

for i in range(Nz):
    for j in range(Nl):
        masses[i,j] = get_mass(zs[i, j], lams[i, j])
np.savetxt("masses.txt", masses)
print masses
print np.log10(masses)
