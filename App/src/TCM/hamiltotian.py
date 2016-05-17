import sys

import numpy as np
from math import exp
from src.TCM.hamiltonian_err import *

def get_Hfield(ph_count, at_count, wc, wa, g):
	#------------------------------------------------------------------------------------------------------------------
	adiag = np.sqrt(np.arange(1, ph_count+1))
	
	across = np.diagflat(adiag, -1)
	a = np.diagflat(adiag, 1)
	acrossa = np.dot(across, a)
	#------------------------------------------------------------------------------------------------------------------
	H_dim = (ph_count+1) * pow(2, at_count)
	#------------------------------------------------------------------------------------------------------------------
	at_dim = pow(2, at_count)
	
	I_at = np.identity(at_dim)
	#------------------------------------------------------------------------------------------------------------------
	H_field = wc * np.kron(acrossa, I_at)
	#------------------------------------------------------------------------------------------------------------------
	return H_field

def get_Hatoms(ph_count, at_count, wc, wa, g):
	#------------------------------------------------------------------------------------------------------------------
	sigmadiag = [1]

	sigmacross = np.diagflat(sigmadiag, -1)
	sigma = np.diagflat(sigmadiag, 1)
	sigmacrosssigma = np.dot(sigmacross, sigma)
	#------------------------------------------------------------------------------------------------------------------
	ph_dim = ph_count+1
	
	I_ph = np.identity(ph_dim)
	#------------------------------------------------------------------------------------------------------------------
	H_dim = (ph_count+1) * pow(2, at_count)
	
	H_atoms = np.zeros([H_dim, H_dim])
	#------------------------------------------------------------------------------------------------------------------
	for i in range(1, at_count+1):
		elem = sigmacrosssigma
		
		at_prev = np.identity(pow(2, i-1))
		elem = np.kron(at_prev, elem)
			
		at_next = np.identity( pow(2, at_count-i))
		elem = np.kron(elem, at_next)
		
		H_atoms += wa * np.kron(I_ph, elem)		
	#------------------------------------------------------------------------------------------------------------------
	return H_atoms

def get_Hint_RWA(ph_count, at_count, wc, wa, g):
	#------------------------------------------------------------------------------------------------------------------
	adiag = np.sqrt(np.arange(1, ph_count+1))
	
	across = np.diagflat(adiag, -1)
	a = np.diagflat(adiag, 1)
	acrossa = np.dot(across, a)
	#------------------------------------------------------------------------------------------------------------------
	sigmadiag = [1]

	sigmacross = np.diagflat(sigmadiag, -1)
	sigma = np.diagflat(sigmadiag, 1)
	sigmacrosssigma = np.dot(sigmacross, sigma)
	#------------------------------------------------------------------------------------------------------------------
	H_dim = (ph_count+1) * pow(2, at_count)
	
	H_int = np.zeros([H_dim, H_dim])
	#------------------------------------------------------------------------------------------------------------------
	for i in range(1, at_count+1):
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
	#------------------------------------------------------------------------------------------------------------------
	return H_int

def get_Hfieldw(ph_count, at_count, wc, wa, g):
	#------------------------------------------------------------------------------------------------------------------
	adiag = np.sqrt(np.arange(1, ph_count+1))
	
	across = np.diagflat(adiag, -1)
	a = np.diagflat(adiag, 1)
	acrossa = np.dot(across, a)
	#------------------------------------------------------------------------------------------------------------------
	H_dim = (ph_count+1) * pow(2, at_count)
	#------------------------------------------------------------------------------------------------------------------
	at_dim = pow(2, at_count)
	
	I_at = np.identity(at_dim)
	#------------------------------------------------------------------------------------------------------------------
	H_field = wc * np.kron(acrossa, I_at)
	#------------------------------------------------------------------------------------------------------------------
	return H_field

def get_Hatomsw(ph_count, at_count, wc, wa, g):
	#------------------------------------------------------------------------------------------------------------------
	sigmadiag = [1]

	sigmacross = np.diagflat(sigmadiag, -1)
	sigma = np.diagflat(sigmadiag, 1)
	sigmacrosssigma = np.dot(sigmacross, sigma)
	#------------------------------------------------------------------------------------------------------------------
	ph_dim = ph_count+1
	
	I_ph = np.identity(ph_dim)
	#------------------------------------------------------------------------------------------------------------------
	H_dim = (ph_count+1) * pow(2, at_count)
	
	H_atoms = np.zeros([H_dim, H_dim])
	#------------------------------------------------------------------------------------------------------------------
	for i in range(1, at_count+1):
		elem = sigmacrosssigma
		
		at_prev = np.identity(pow(2, i-1))
		elem = np.kron(at_prev, elem)
			
		at_next = np.identity( pow(2, at_count-i))
		elem = np.kron(elem, at_next)
		
		H_atoms += wa[i-1] * np.kron(I_ph, elem)		
	#------------------------------------------------------------------------------------------------------------------
	return H_atoms

def get_Hint_RWAd(ph_count, at_count, wc, wa, g):
	#------------------------------------------------------------------------------------------------------------------
	adiag = np.sqrt(np.arange(1, ph_count+1))
	
	across = np.diagflat(adiag, -1)
	a = np.diagflat(adiag, 1)
	acrossa = np.dot(across, a)
	#------------------------------------------------------------------------------------------------------------------
	sigmadiag = [1]

	sigmacross = np.diagflat(sigmadiag, -1)
	sigma = np.diagflat(sigmadiag, 1)
	sigmacrosssigma = np.dot(sigmacross, sigma)
	#------------------------------------------------------------------------------------------------------------------
	H_dim = (ph_count+1) * pow(2, at_count)
	
	H_int = np.zeros([H_dim, H_dim])
	#------------------------------------------------------------------------------------------------------------------
	for i in range(1, at_count+1):
		#------------------------------------------------
		elem = across
		
		before = np.identity(pow(2, i-1))
		elem = np.kron(elem, before)
		
		elem = np.kron(elem, sigma)
		
		after = np.identity(pow(2, at_count-i))
		elem = np.kron(elem, after)
		
		H_int += g[i-1] * elem	
		#------------------------------------------------
		elem = a
		
		before = np.identity(pow(2, i-1))
		elem = np.kron(elem, before)
		
		elem = np.kron(elem, sigmacross)
		
		after = np.identity(pow(2, at_count-i))
		elem = np.kron(elem, after)
		
		H_int += g[i-1] * elem	
		#------------------------------------------------
	#------------------------------------------------------------------------------------------------------------------
	return H_int

def get_Hint_EXACT(ph_count, at_count, wc, wa, g):
	#------------------------------------------------------------------------------------------------------------------
	adiag = np.sqrt(np.arange(1, ph_count+1))
	
	across = np.diagflat(adiag, -1)
	a = np.diagflat(adiag, 1)
	acrossa = np.dot(across, a)
	#------------------------------------------------------------------------------------------------------------------
	sigmadiag = [1]

	sigmacross = np.diagflat(sigmadiag, -1)
	sigma = np.diagflat(sigmadiag, 1)
	sigmacrosssigma = np.dot(sigmacross, sigma)
	#------------------------------------------------------------------------------------------------------------------
	H_dim = (ph_count+1) * pow(2, at_count)
	
	H_int = np.zeros([H_dim, H_dim], dtype=complex)
	#------------------------------------------------------------------------------------------------------------------
	for i in range(1, at_count+1):
		#------------------------------------------------
		elem = (across + a)
		
		before = np.identity(pow(2, i-1))
		elem = np.kron(elem, before)
		
		elem = np.kron(elem, sigmacross + sigma)
		
		after = np.identity(pow(2, at_count-i))
		elem = np.kron(elem, after)
		
		H_int += g * elem	
		#------------------------------------------------
	#------------------------------------------------------------------------------------------------------------------
	return H_int

def get_H_RWA(ph_count, at_count, wc, wa, g, RWA=True):
	#------------------------------------------------------------------------------------------------------------------
	get_H_err(ph_count, at_count, wc, wa, g, RWA)
	#------------------------------------------------------------------------------------------------------------------
	H_field = get_Hfield(ph_count, at_count, wc, wa, g)
	H_field_size = np.shape(H_field)

	# print('H_field:\n', H_field, '\n')
	# print('H_field_size:', H_field_size, '\n')
	#------------------------------------------------------------------------------------------------------------------
	H_atoms = get_Hatoms(ph_count, at_count, wc, wa, g)
	H_atoms_size = np.shape(H_atoms)
	
	# print('H_atoms_size:', H_atoms_size, '\n')
	# print('H_atoms:\n', H_atoms, '\n')
	#------------------------------------------------------------------------------------------------------------------
	H_int_RWA = get_Hint_RWA(ph_count, at_count, wc, wa, g)
	H_int_size = np.shape(H_int_RWA)

	# print('H_int:\n', H_int, '\n')
	# print('H_int_size:', H_int_size, '\n')
	#------------------------------------------------------------------------------------------------------------------
	H = np.matrix(H_field + H_atoms + H_int_RWA)
	H_size = np.shape(H)

	# print('H:\n', H, '\n')
	# print('H_size:', H_size, '\n')
	
	# H_diag = np.diag(H)
	# print('H_diag:\n', H_diag, '\n')
	#------------------------------------------------------------------------------------------------------------------
	# write_to_file(H, "H2")
	#------------------------------------------------------------------------------------------------------------------
	return H

def get_H_EXACT(ph_count, at_count, wc, wa, g):
	#------------------------------------------------------------------------------------------------------------------
	get_H_err(ph_count, at_count, wc, wa, g, RWA=False)
	#------------------------------------------------------------------------------------------------------------------
	H_field = get_Hfield(ph_count, at_count, wc, wa, g)
	H_field_size = np.shape(H_field)

	# print('H_field:\n', H_field, '\n')
	# print('H_field_size:', H_field_size, '\n')
	#------------------------------------------------------------------------------------------------------------------
	H_atoms = get_Hatoms(ph_count, at_count, wc, wa, g)
	H_atoms_size = np.shape(H_atoms)
	
	# print('H_atoms_size:', H_atoms_size, '\n')
	# print('H_atoms:\n', H_atoms, '\n')
	#------------------------------------------------------------------------------------------------------------------
	H_int = get_Hint_EXACT(ph_count, at_count, wc, wa, g)
	H_int_size = np.shape(H_int)

	# print('H_int:\n', H_int, '\n')
	# print('H_int_size:', H_int_size, '\n')
	#------------------------------------------------------------------------------------------------------------------
	H = np.matrix(H_field + H_atoms + H_int)
	H_size = np.shape(H)

	# print('H:\n', H, '\n')
	# print('H_size:', H_size, '\n')
	
	# H_diag = np.diag(H)
	# print('H_diag:\n', H_diag, '\n')
	#------------------------------------------------------------------------------------------------------------------
	# write_to_file(H, "H2")
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