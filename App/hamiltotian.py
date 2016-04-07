import sys
import numpy as np

from hamiltonian_err import *   # !DONE except err_msg

def get_H(ph_count, at_count, wc, wa, g, RWA=True):
	#------------------------------------------------------------------------------------------------------------------
	get_H_err(ph_count, at_count, wc, wa, g, RWA)
	#------------------------------------------------------------------------------------------------------------------
	adiag = np.sqrt(np.arange(1, ph_count+1))
	
	across = np.diagflat(adiag, -1)
	a = np.diagflat(adiag, 1)
	acrossa = np.dot(across, a)

	# print('adiag:\n', adiag, '\n')
	# print('across:\n', across, '\n')
	# print('a:\n', a, '\n')
	# print('acrossa:\n', acrossa, '\n')
	#------------------------------------------------------------------------------------------------------------------
	sigmadiag = [1]

	sigmacross = np.diagflat(sigmadiag, -1)
	sigma = np.diagflat(sigmadiag, 1)
	sigmacrosssigma = np.dot(sigmacross, sigma)

	# print('sigma_diag:\n', sigmadiag, '\n')
	# print('sigmacross:\n', sigmacross, '\n')
	# print('sigma:\n', sigma, '\n')
	# print('sigmacrosssigma:\n', sigmacrosssigma, '\n')
	#------------------------------------------------------------------------------------------------------------------
	H = []

	H_dim = (ph_count+1) * pow(2, at_count)
	#------------------------------------------------------------------------------------------------------------------
	ph_dim = ph_count+1
	I_ph = np.identity(ph_dim)

	at_dim = pow(2, at_count)
	I_at = np.identity(at_dim)
	#------------------------------------------------------------------------------------------------------------------
	H_field = wc * np.kron(acrossa, I_at)

	H_field_size = np.shape(H_field)

	# print('H_field:\n', H_field, '\n')
	# print('H_field_size:', H_field_size, '\n')
	#------------------------------------------------------------------------------------------------------------------
	H_atoms = np.zeros([H_dim, H_dim])

	for i in range(1, at_count+1):
		elem = sigmacrosssigma
		
		at_prev = np.identity(pow(2, i-1))
		elem = np.kron(at_prev, elem)
			
		at_next = np.identity( pow(2, at_count-i))
		elem = np.kron(elem, at_next)
		
		H_atoms += wa * np.kron(I_ph, elem)	
		
	H_atoms_size = np.shape(H_atoms)

	# print('H_atoms_size:', H_atoms_size, '\n')
	# print('H_atoms:\n', H_atoms, '\n')
	#------------------------------------------------------------------------------------------------------------------
	H_int = np.zeros([H_dim, H_dim])

	for i in range(1, at_count+1):
		if RWA:
			#------------------------------------------------
			elem = across
			
			before = np.identity(pow(2, i-1))
			elem = np.kron(elem, before)
			
			elem = np.kron(elem, sigma)
			
			after = np.identity(pow(2, at_count-i))
			elem = np.kron(elem, after)
			
			H_int += g * elem	
			#------------------------------------------------
			elem = a
			
			before = np.identity(pow(2, i-1))
			elem = np.kron(elem, before)
			
			elem = np.kron(elem, sigmacross)
			
			after = np.identity(pow(2, at_count-i))
			elem = np.kron(elem, after)
			
			H_int += g * elem	
			#------------------------------------------------	
		else:
			#------------------------------------------------
			elem = across + a
			
			before = np.identity(pow(2, i-1))
			elem = np.kron(elem, before)
			
			elem = np.kron(elem, sigmacross + sigma)
			
			after = np.identity(pow(2, at_count-i))
			elem = np.kron(elem, after)
			
			H_int = g * elem	
			#------------------------------------------------
		
	H_int_size = np.shape(H_int)

	# print('H_int:\n', H_int, '\n')
	# print('H_int_size:', H_int_size, '\n')
	#------------------------------------------------------------------------------------------------------------------
	H = H_field + H_atoms + H_int
	H = np.matrix(H)

	H_size = np.shape(H)

	H_diag = np.diag(H)
	# print('H_diag:\n', H_diag, '\n')
	# print('H:\n', H, '\n')
	# print('H_size:', H_size, '\n')
	#------------------------------------------------------------------------------------------------------------------
	return H

def write_to_file(H, filename):
	#------------------------------------------------------------------------------------------------------------------
	write_to_file_err(H, filename)
	#------------------------------------------------------------------------------------------------------------------
	fh = open(filename, 'w')
	#------------------------------------------------------------------------------------------------------------------
	for i in range(0, H.shape[0]):
		for j in range(0, H.shape[0]):
			elem = H.item(i, j)

			fh.write(str(elem) + ' ')
			
		fh.write('\n')
	#------------------------------------------------------------------------------------------------------------------
	return