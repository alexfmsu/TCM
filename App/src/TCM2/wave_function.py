from scipy.linalg import expm
from math import sqrt, sin
import numpy as np
import src.TCM2.animator as animator

import src.config as config
import src.TCM.wave_function_err as wf_err

precision = config.precision

def get_w0(ph_count1, init_state1, ph_count2, init_state2):
	#------------------------------------------------------------------------------------------------------------------
	# wf_err.get_w0_err(ph_count, init_state)
	#------------------------------------------------------------------------------------------------------------------
	at1 = init_state1[1]
	at_count1 = len(at1)
	
	at2 = init_state2[1]
	at_count2 = len(at2)
	#------------------------------------------------------------------------------------------------------------------
	#------------------------------------------------------------------------------------------------------------------
	if init_state1[0] > ph_count1: return -1
	#------------------------------------------------------------------------------------------------------------------
	ph_state1 = np.zeros(shape=(ph_count1+1, 1))
	ph_state1[init_state1[0]][0] = 1 
	
	w0_1 = np.matrix(ph_state1)
	
	for i in  range(1, at_count1+1):
		at_state1 = np.zeros(shape=(2,1))
		if at1[i-1] in range(0, 2):
			at_state1[at1[i-1]][0] = 1 
		else: return -1

		w0_1 = np.kron(w0_1, at_state1)
	#------------------------------------------------------------------------------------------------------------------
	ph_state2 = np.zeros(shape=(ph_count2+1, 1))
	ph_state2[init_state2[0]][0] = 1 
	
	w0_2 = np.matrix(ph_state2)
	
	for i in  range(1, at_count2+1):
		at_state2 = np.zeros(shape=(2,1))
		if at2[i-1] in range(0, 2):
			at_state2[at2[i-1]][0] = 1 
		else: return -1

		w0_2 = np.kron(w0_2, at_state2)
	
	w0 = np.kron(w0_1, w0_2)
	
	w0 = np.matrix(w0)
	#------------------------------------------------------------------------------------------------------------------
	return w0

def get_wdt(wt, exp_iHdt):
	
	wt = np.dot(exp_iHdt, wt)
	
	return wt

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

def run(w0, H, t0, t1, initstate1, initstate2, ph_count1, ph_count2, nt = 200, not_empty = False, ymin=0, ymax=1, RWA=True, title='title', color='blue'):
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
	
	at1_count = len(initstate1[1])
	at2_count = len(initstate2[1])
	
	# for i in range(0, len(w0)):
	# 	t = i
	# 	t = t / pow(2, at2_count)
	# 	ph2_count = int(t / ph_count2)
	# 	t = t / ph_count2
	# 	t = t / pow(2, at2_count)
	# 	ph1_count = t
		
	# 	st2_number = at2_count
	# 	# st2_number = st2_number
	# 	# st2_number = (pow(2, ph1_count+at1_count) - i)% pow(2, at2_count)

		
	# 	at2_binary = bin(st2_number)[2:].zfill(at2_count)

	# 	state.append('[' + str(ph1_count)+ ' ' + str(ph2_count) + '|' + at2_binary + ']')
	# #------------------------------------------------------------------------------------------------------------------	
	# for i in range(0, len(w0)):
	# 	print(i, " ", state[i], i, '/', pow(2, ph2_count+at1_count+at2_count))
	# return
	w = []
	
	# print("w0:", w0.shape[0], w0.shape[1])
	# print("H:", H.shape[0], H.shape[1])

	# exp_iHdt = expm(np.array(H))
	exp_iHdt = expm(np.array(H) * complex(0,-1) * dt)
	# exp_iHdt = np.matrix(exp_iHdt)
	wt = w0
	# print(exp_iHdt)
	for i in range(0, nt+1):
		wt = get_wdt(wt, exp_iHdt)
		# wt = get_wt(w0, H, i*dt)
		if np.max(wt) > 1:
			sys.exit("Error\n") 
		w.append(np.abs(wt))
		
	w = np.array(w)
	#------------------------------------------------------------------------------------------------------------------
	# animator.make_plot3D(t, t0, t1, w, ymin=ymin, ymax=ymax, state=state, not_empty=not_empty, max_limit=max_limit)
	st = initstate2[0]*(pow(2, at2_count))
	
	for i in range(0, at2_count):
		st += pow(2, i) * initstate2[1][at2_count-i-1]
	
	for i in range(0, at1_count):
		st += (pow(2, i+at2_count) * (ph_count2+1)) * initstate1[1][at1_count-i-1]
	
	st += initstate1[0] * (pow(2, at1_count + at2_count) * (ph_count2+1))
	
	# print(st)
	#------------------------------------------------------------------------------------------------------------------
	# animator.make_plot3D(t, t0, t1, w, ymin=ymin, ymax=ymax, state=state, not_empty=not_empty, max_limit=max_limit)
	
	animator.make_plot(t, t0, t1, ymin, ymax, w[:,st], color, title=title)

	return

def run2(w0, H_RWA, H_EXACT, t0, t1, initstate1, initstate2, ph_count1, ph_count2, nt = 200, not_empty = False, ymin=0, ymax=1, RWA=True, title='title', color='blue'):
	#------------------------------------------------------------------------------------------------------------------
	if not(nt in range(0, 501)): return -1
	
	if t0 < 0: return -1
	if t1 < 0: return -1
	if t0 >= t1: return -1

	if len(np.shape(H_RWA)) != 2: return -1
	if np.shape(H_RWA)[0] != np.shape(H_RWA)[1]: return -1 
	if np.shape(H_RWA)[0] != len(w0): return -1
	
	if len(np.shape(H_EXACT)) != 2: return -1
	if np.shape(H_EXACT)[0] != np.shape(H_EXACT)[1]: return -1 
	if np.shape(H_EXACT)[0] != len(w0): return -1
	#------------------------------------------------------------------------------------------------------------------
	t = np.linspace(t0, t1, nt+1)
	
	dt = t[1] - t[0]
	#------------------------------------------------------------------------------------------------------------------
	state = []
	
	at1_count = len(initstate1[1])
	at2_count = len(initstate2[1])
	
	w_RWA = []
	w_EXACT = []
	
	exp_iH_RWAdt = expm(np.array(H_RWA) * complex(0,-1) * dt)
	exp_iH_EXACTdt = expm(np.array(H_EXACT) * complex(0,-1) * dt)
	
	wt_RWA = w0
	wt_EXACT = w0
	
	for i in range(0, nt+1):
		wt_RWA = get_wdt(wt_RWA, exp_iH_RWAdt)
		wt_EXACT = get_wdt(wt_EXACT, exp_iH_EXACTdt)
		
		if np.max(wt_RWA) > 1 or np.max(wt_EXACT) > 1:
			sys.exit("Error\n") 
		
		w_RWA.append(np.abs(wt_RWA))
		w_EXACT.append(np.abs(wt_EXACT))
		
	w_RWA = np.array(w_RWA)
	w_EXACT = np.array(w_EXACT)
	#------------------------------------------------------------------------------------------------------------------
	# animator.make_plot3D(t, t0, t1, w, ymin=ymin, ymax=ymax, state=state, not_empty=not_empty, max_limit=max_limit)
	st = initstate2[0]*(pow(2, at2_count))
	
	for i in range(0, at2_count):
		st += pow(2, i) * initstate2[1][at2_count-i-1]
	
	for i in range(0, at1_count):
		st += (pow(2, i+at2_count) * (ph_count2+1)) * initstate1[1][at1_count-i-1]
	
	st += initstate1[0] * (pow(2, at1_count + at2_count) * (ph_count2+1))
	
	# print(st)
	#------------------------------------------------------------------------------------------------------------------
	# animator.make_plot3D(t, t0, t1, w, ymin=ymin, ymax=ymax, state=state, not_empty=not_empty, max_limit=max_limit)
	
	animator.make_plot2(t, t0, t1, ymin, ymax, w_RWA[:,st], w_EXACT[:,st], title, X=r'$t,\ мкс$', Y=r'$Amplitude$   ')

	return