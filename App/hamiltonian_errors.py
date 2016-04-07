import sys
import numbers

from config import *

def error_handle(ph_count, at_count, wc, wa, g, RWA):
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	# except text
	if not isinstance(ph_count, int):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: type of \'ph_count\' isn\'t int\n'
		
		sys.exit(error)
	
	if not (ph_count in range(ph_count_min, ph_count_max+1)):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: \'ph_count\' isn\'t in range(' + str(ph_count_min) + ', ' + str(ph_count_max) + ')\n'
		
		sys.exit(error)
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	# except text
	if not isinstance(at_count, int):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: type of \'at_count\' isn\'t int\n'
		
		sys.exit(error)
	
	if not (at_count in range(at_count_min, at_count_max + 1)):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H: \'at_count\' isn\'t in range(' + str(at_count_min) + ', ' + str(at_count_max) + ')\n'
		
		sys.exit(error)
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	# except text
	if not isinstance(wc, numbers.Number):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H:\'wc\' isn\'t number\n'
		
		sys.exit(error)
	
	if wc <= 0:
		error =  '\n'
		error += 'Error:\nget_H: \'wc\' isn\'t negative or zero\n'
		
		sys.exit(error)
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	# except text
	if not isinstance(wa, numbers.Number):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H:\'wa\' isn\'t number\n'
		
		sys.exit(error)
	
	if wa <= 0:
		error =  '\n'
		error += 'Error:\nget_H: \'wa\' isn\'t negative or zero\n'
		
		sys.exit(error)
	#------------------------------------------------------------------------------------------------------------------
	# !DONE
	# except text
	if not isinstance(g, numbers.Number):
		error =  '\n'
		error += 'Error:\n'
		error += 'get_H:\'g\' isn\'t number\n'
		
		sys.exit(error)
	
	if g < 0:
		error =  '\n'
		error += 'Error:\nget_H: \'g\' isn\'t negative\n'
		
		sys.exit(error)
	#------------------------------------------------------------------------------------------------------------------
	