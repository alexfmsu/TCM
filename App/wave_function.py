from scipy.linalg import expm
from math import sqrt, sin
import numpy as np
import animator
import config

import wave_function_err as wf_err

precision = config.precision

def get_w0(ph_count, init_state):
	#------------------------------------------------------------------------------------------------------------------
	wf_err.get_w0_err(ph_count, init_state)
	#------------------------------------------------------------------------------------------------------------------
	at = init_state[1]
	at_count = len(at)
	#------------------------------------------------------------------------------------------------------------------
	#------------------------------------------------------------------------------------------------------------------
	if init_state[0] > ph_count: return -1
	#------------------------------------------------------------------------------------------------------------------
	ph_state = np.zeros(shape=(ph_count+1, 1))
	ph_state[init_state[0]][0] = 1 
	
	w0 = np.matrix(ph_state)
	
	for i in  range(1, at_count+1):
		at_state = np.zeros(shape=(2,1))
		if at[i-1] in range(0, 2):
			at_state[at[i-1]][0] = 1 
		else: return -1

		w0 = np.kron(w0, at_state)
	
	w0 = np.matrix(w0)
	#------------------------------------------------------------------------------------------------------------------
	
	return w0

def get_wtlist(w0, H, t):
	# if len(w0) <= 0: return -1
	# if sqrt(np.size(H)) != len(w0): return -1
	H = np.array(H)
	# print(H)
	Ht=H.dot(t)
	# exp = expm(np.dot(H,t))
	
	# wt = np.dot(exp, w0)
	
	# return wt

def get_wt(w0, H, t):
	wf_err.get_wt_err(w0, H, t)
	
	exp = expm(H * complex(0,-1) * t)
	
	wt = np.dot(exp, w0)
	
	return wt

def get_ro(w):
	return np.multiply(w, w.getH())
#######################################################################################################################
# !DONE
def is_hermitian(matrix):
	wf_err.is_hermitian_err(matrix)

	diff = matrix - matrix.getH()
	
	return np.all(abs(diff) < precision)
#----------------------------------------------------------------------------------------------------------------------
# !DONE
def is_unitary(matrix):
	wf_err.is_unitary_err(matrix)

	matrix_CT = matrix 
	diff = matrix * matrix_CT - matrix_CT * matrix
	
	return np.all(abs(diff) < precision)
#######################################################################################################################

def run(w0, H, t0, t1, initstate, nt = 25, not_empty = False, ymin=0, ymax=1, max_limit = 1e-3):
	#------------------------------------------------------------------------------------------------------------------
	if not(nt in range(0, 501)): return -1
	
	if t0 < 0: return -1
	if t1 < 0: return -1
	if t0 >= t1: return -1

	if len(np.shape(H)) != 2: return -1
	if np.shape(H)[0] != np.shape(H)[1]: return -1 
	if np.shape(H)[0] != len(w0): return -1
	#------------------------------------------------------------------------------------------------------------------
	t = np.linspace(t0, t1, nt+1)
	
	dt = t[1] - t[0]
	#------------------------------------------------------------------------------------------------------------------
	state = []
	
	at_count = len(initstate[1])
	
	for i in range(0, len(w0)):
		ph_count = int(i / pow(2, at_count))
		st_number = i % pow(2, at_count)

		at_binary = bin(st_number)[2:].zfill(at_count)

		state.append('[' + str(ph_count) + '|' + at_binary + ']')
	#------------------------------------------------------------------------------------------------------------------	
	w = []
	
	for i in range(0, nt+1):
		wt = get_wt(w0, H, i*dt)
		if np.max(wt) > 1:
			sys.exit("Error\n") 
		w.append(np.abs(wt))
		
	w = np.array(w)
	#------------------------------------------------------------------------------------------------------------------
	# animator.make_plot3D(t, t0, t1, w, ymin=ymin, ymax=ymax, state=state, not_empty=not_empty, max_limit=max_limit)
	st = initstate[0]*(pow(2, at_count))
	at = 0
	for i in range(0, at_count):
		print(i, i, pow(2, i), initstate[1][at_count-i-1])
		at+=pow(2, i)*initstate[1][at_count-i-1]
	
	print(at, st)
	#------------------------------------------------------------------------------------------------------------------
	# animator.make_plot3D(t, t0, t1, w, ymin=ymin, ymax=ymax, state=state, not_empty=not_empty, max_limit=max_limit)
	animator.make_plot(t, t0, t1, ymin, ymax, w[:,st+at])

	return