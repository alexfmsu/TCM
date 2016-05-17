import sys
import numpy as np

# from src.TCM.hamiltonian_err import *   # !DONE except err_msg
import src.TCM.hamiltotian as H1 

def get_H(ph_count1, at_count1, wc1, wa1, g1, ph_count2, at_count2, wc2, wa2, g2, m = 0.4, RWA=True):
	#------------------------------------------------------------------------------------------------------------------
	# get_H_err(ph_count, at_count, wc, wa, g, RWA)
	#------------------------------------------------------------------------------------------------------------------
	adiag1 = np.sqrt(np.arange(1, ph_count1+1))
	
	across1 = np.diagflat(adiag1, -1)
	a1 = np.diagflat(adiag1, 1)
	acrossa1 = np.dot(across1, a1)

	adiag2 = np.sqrt(np.arange(1, ph_count2+1))
	
	across2 = np.diagflat(adiag2, -1)
	a2 = np.diagflat(adiag2, 1)
	acrossa2 = np.dot(across2, a2)
	#------------------------------------------------------------------------------------------------------------------
	sigmadiag = [1]

	sigmacross = np.diagflat(sigmadiag, -1)
	sigma = np.diagflat(sigmadiag, 1)
	sigmacrosssigma = np.dot(sigmacross, sigma)
	#------------------------------------------------------------------------------------------------------------------
	ph1_dim = ph_count1+1
	I_ph1 = np.identity(ph1_dim)

	at1_dim = pow(2, at_count1)
	I_at1 = np.identity(at1_dim)
	
	ph2_dim = ph_count2+1
	I_ph2 = np.identity(ph2_dim)

	at2_dim = pow(2, at_count2)
	I_at2 = np.identity(at2_dim)
	#------------------------------------------------------------------------------------------------------------------
	if RWA:
		h1 = H1.get_H_RWA(ph_count1, at_count1, wc1, wa1, g1, RWA)
		h2 = H1.get_H_RWA(ph_count2, at_count2, wc2, wa2, g2, RWA)
	else:
		h1 = H1.get_H_EXACT(ph_count1, at_count1, wc1, wa1, g1)
		h2 = H1.get_H_EXACT(ph_count2, at_count2, wc2, wa2, g2)
		
	H = np.kron(h1, np.identity(h2.shape[0])) + np.kron(np.identity(h1.shape[0]), h2) 

	H1_m = np.kron(across1, np.identity(at1_dim))
	H1_m = np.kron(H1_m, a2)
	H1_m = np.kron(H1_m, np.identity(at2_dim))
	
	H2_m = np.kron(a1, np.identity(at1_dim))
	H2_m = np.kron(H2_m, across2)
	H2_m = np.kron(H2_m, np.identity(at2_dim))
	
	H_m = m * (H1_m + H2_m)
	#------------------------------------------------------------------------------------------------------------------
	H = np.matrix(H + H_m)
	H_size = np.shape(H)
	
	# print('H:\n', H, '\n')
	# # # print('H_size:', H_size, '\n')
	#------------------------------------------------------------------------------------------------------------------
	return H

def write_to_file(H, filename):
	#------------------------------------------------------------------------------------------------------------------
	write_to_file_err(H, filename)
	#------------------------------------------------------------------------------------------------------------------
	fh = open(filename, 'w')
	#------------------------------------------------------------------------------------------------------------------
	fh.write(str(np.shape(H)[0]) + ' ')
	fh.write(str(np.shape(H)[1]) + ' ')
	fh.write('\n')
	
	for i in range(0, H.shape[0]):
		for j in range(0, H.shape[0]):
			elem = H.item(i, j)

			fh.write(str(elem) + ' ')
			
		fh.write('\n')
	#------------------------------------------------------------------------------------------------------------------
	return