#-----------------------
# !DONE
# except err_msg
# except if not(H.shape[0] > 0)
#-----------------------
import sys
import numbers
import numpy as np

from src.TCM.config import *

def get_H_err(ph_count, at_count, wc, wa, g, RWA):
	#------------------------------------------------------------------------------------------------------------------
	error = ''
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	if not isinstance(ph_count, int):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: type of \'ph_count\' isn\'t int\n'
		
		is_error(error)
		
	if not (ph_count in range(ph_count_min, ph_count_max + 1)):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: \'ph_count\' isn\'t in range(' + str(ph_count_min) + ', ' + str(ph_count_max) + ')\n'
		
		is_error(error)
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	if not isinstance(at_count, int):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: type of \'at_count\' isn\'t int\n'
		
		is_error(error)
		
	if not (at_count in range(at_count_min, at_count_max + 1)):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: \'at_count\' isn\'t in range(' + str(at_count_min) + ', ' + str(at_count_max) + ')\n'
		
		is_error(error)
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	if not isinstance(wc, numbers.Number):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: \'wc\' isn\'t number\n'
	
		is_error(error)
	
	if wc <= 0:
		error =  '\n'
		error += 'Error:\nget_H: \'wc\' isn\'t negative or zero\n'
	
		is_error(error)
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	if not isinstance(wa, numbers.Number):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: \'wa\' isn\'t number\n'
	
		is_error(error)
	
	if wa <= 0:
		error =  '\n'
		error += 'Error:\nget_H: \'wa\' isn\'t negative or zero\n'	
	
		is_error(error)
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	if not isinstance(g, numbers.Number):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: \'g\' isn\'t number\n'
	
		is_error(error)
		
	if g < 0:
		error =  '\n'
		error += 'Error:\nget_H: \'g\' isn\'t negative\n'
	
		is_error(error)
	#------------------------------------------------------------------------------------------------------------------
	return

def write_to_file_err(H, filename):
	#------------------------------------------------------------------------------------------------------------------
	if not isinstance(H, np.matrix):
		error =  '\n'
		error += 'Error:\n'
		error += 'write_to_file: \'H\' isn\'t matrix\n'
	
		is_error(error)
	
	if (len(H.shape) != 2) or (H.shape[0] != H.shape[1]):
		error =  '\n'
		error += 'Error:\n'
		error += 'write_to_file: \'matrix H\' isn\'t square\n'
	
		is_error(error)
	
	# if not(H.shape[0] > 0):
	# 	error =  '\n'
	# 	error += 'Error:\n'
	# 	error += 'write_to_file: \'matrix H\' isn\'t 0x0\n'
	
	# 	is_error(error)
	#------------------------------------------------------------------------------------------------------------------
	if not isinstance(filename, str):
		error =  '\n'
		error += 'Error:\n'
		error += 'write_to_file: \'filename\' isn\'t string\n'
	
		is_error(error)
	#------------------------------------------------------------------------------------------------------------------
	return

def is_error(error):
	# if error: sys.exit(error)
	if error: return 0

	return 1