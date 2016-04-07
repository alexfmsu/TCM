#-------------------------------
# !DONE
# except err_msg
# except if not(H.shape[0] > 0)
#-------------------------------
import sys
import numpy as np

from config import *

def get_w0_err(ph_count, init_state):
	#------------------------------------------------------------------------------------------------------------------
	error = ''
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	if not isinstance(ph_count, int):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_w0: type of \'ph_count\' isn\'t int\n'
	
		is_error(error)

	if not (ph_count in range(ph_count_min, ph_count_max+1)):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_w0: \'ph_count\' isn\'t in range(' + str(ph_count_min) + ', ' + str(ph_count_max) + ')\n'
	
		is_error(error)
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	if not isinstance(init_state, list):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_w0: type of \'init_state\' isn\'t list\n'
	
		is_error(error)	
	
	if len(init_state) != 2:
		error =  '\n'
		error += 'Error:\n'
		error += 'get_w0: \'init_state\' isn\'t [ph_count, [...]]\n'
	
		is_error(error)	
	
	if not(isinstance(init_state[0], int)):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_w0: type of \'init_state[0]\' isn\'t int\n'
	
		is_error(error)	
	
	if not(init_state[0] in range(0, ph_count+1)):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_w0: \'init_state[0]\' isn\'t in range(' + str(0) + ', ' + str(ph_count) + ')\n'
	
		is_error(error)	
	
	if not(isinstance(init_state[1], list)):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_w0: type of \'init_state[1]\' isn\'t list\n'
	
		is_error(error)	
	
	if not(len(init_state[1]) in range(1, at_count_max+1)):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_w0: at_count isn\'t in range(' + str(1) + ', ' + str(at_count_max) + ')\n'
	
		is_error(error)	
	
	for at in init_state[1]:
		if not (isinstance(at, int)):
			error =  '\n'
			error += 'Error:\n'
			error += 'get_w0: init_state[1] isn\'t numeric list\n'
		
		if not at in range(0, 2):
			error =  '\n'
			error += 'Error:\n'
			error += 'get_w0: init_state[1] isn\'t in range(0, 1)\n'
		
			is_error(error)	
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	if init_state[0] + np.sum(init_state[1]) > ph_count:
		error =  '\n'
		error += 'Error:\n'
		error += 'get_w0: init_state[0] + init_state[1] <= ph_count\n'
	
		is_error(error)	
	#------------------------------------------------------------------------------------------------------------------
	return

def is_unitary_err(matrix):
	if not isinstance(matrix, np.matrix):
		error =  '\n'
		error += 'Error:\n'
		error += 'is_unitary: matrix isn\'t np.matrix\n'
	
	if len(matrix.shape) != 2:
		error =  '\n'
		error += 'Error:\n'
		error += 'is_unitary: isn\'t matrix\n'

	if matrix.shape[0] != matrix.shape[1]:
		error =  '\n'
		error += 'Error:\n'
		error += 'is_unitary: matrix isn\'t squarematrix\n'
		
	if matrix.shape[0] <=0:
		error =  '\n'
		error += 'Error:\n'
		error += 'is_unitary: matrix size < 0\n'
	
def is_hermitian_err(matrix):
	if not isinstance(matrix, np.matrix):
		error =  '\n'
		error += 'Error:\n'
		error += 'is_hermitian: matrix isn\'t np.matrix\n'
	
	if len(matrix.shape) != 2:
		error =  '\n'
		error += 'Error:\n'
		error += 'is_hermitian: isn\'t matrix\n'

	if matrix.shape[0] != matrix.shape[1]:
		error =  '\n'
		error += 'Error:\n'
		error += 'is_hermitian: matrix isn\'t squarematrix\n'
		
	if matrix.shape[0] <=0:
		error =  '\n'
		error += 'Error:\n'
		error += 'is_hermitian: matrix size < 0\n'

def get_wt_err(w0, H, t):
	error = ''

	if len(w0.shape) <= 0:
		error =  '\n'
		error += 'Error:\n'
		error += 'get_wt: w0 isn\'t (n, 1)\n'

	if w0.shape[0] <= 0: return -1
	
	if w0.shape[1] != 1: return -1
	
	if H.shape[0] != w0.shape[0]: return -2
	if t < 0: return -3
	
	if error:
		sys.exit(error)
	
def is_error(error):
	if error: sys.exit(error)

	return