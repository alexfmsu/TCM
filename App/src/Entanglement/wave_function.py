from scipy.linalg import expm
from math import sqrt, sin, cos
import numpy as np
import src.TCM2.animator as animator

import src.config as config
import src.TCM.wave_function_err as wf_err

precision = config.precision

def get_w0(phA_count, init_phA_count, A2, phB_count, init_phB_count, B2, alpha):
	if init_phA_count + A2 > phA_count:
		print(123)
		return 0
	
	if init_phB_count + B2 > phB_count:
		print(123)
		return 0
	
	nA = np.zeros(shape=(phA_count+1, 1))
	nA[init_phA_count][0] = 1

	nB = np.zeros(shape=(phB_count+1, 1))
	nB[init_phB_count][0] = 1
	
	e1 = np.zeros(shape=(2, 1))
	e1[1][0] = 1

	g1 = np.zeros(shape=(2, 1))
	g1[0][0] = 1
	
	e2 = np.zeros(shape=(2, 1))
	e2[1][0] = 1

	g2 = np.zeros(shape=(2, 1))
	g2[0][0] = 1
	
	print(nA)
	print(nB)
	print('e1:')
	print(e1)
	print('g1:')
	print(g1)
	print('e2:')
	print(e2)
	print('g2:')
	print(g2)

	a1 = a2 = a3 = a4 = 0

	if A2 == 0 and B2 == 0:
		a4 = 1
	elif A2 == 0 and B2 == 1:
		a3 = 1
	elif A2 == 1 and B2 == 0:
		a2 = 1
	elif A2 == 1 and B2 == 1:
		a1 = 1
	
	e1e2 = np.kron(e1, e2) 	# |e1 e2>
	e1g2 = np.kron(e1, g2) 	# |e1 g2>
	g1e2 = np.kron(g1, e2) 	# |g1 e2>
	g1g2 = np.kron(g1, g2) 	# |g1 g2>
	
	w0 = []
	w0 = cos(alpha) * (a1 * np.kron( np.kron(e1e2, nA), np.kron(e1e2, nB) ) + a2 * np.kron( np.kron(e1e2, nA), np.kron(e1g2, nB) ) \
		+ a3 * np.kron( np.kron(e1g2, nA), np.kron(e1e2, nB) ) + a4 * np.kron( np.kron(e1g2, nA), np.kron(e1g2, nB) )\
		+ sin(alpha) * (a1 * np.kron( np.kron(g1e2, nA), np.kron(g1e2, nB) ) + a2 * np.kron( np.kron(g1e2, nA), np.kron(g1g2, nB) )\
		+ a3 * np.kron( np.kron(g1g2, nA), np.kron(g1e2, nB) ) + a4 * np.kron( np.kron(g1g2, nA), np.kron(g1g2, nB) ))\
	)
	return w0

def get_roAt(ro, nA, nB):
	ro_dim = ro.shape[0]
	ro_at = np.zeros([ro_dim, ro_dim])

	I_atA_bra = np.zeros(shape=(1, 4))
	I_atA_bra.fill(1)

	I_atB_bra = np.zeros(shape=(1, 4))
	I_atB_bra.fill(1)
	
	I_atA_ket = np.zeros(shape=(4, 1))
	I_atA_ket.fill(1)

	I_atB_ket = np.zeros(shape=(4, 1))
	I_atB_ket.fill(1)

	I_phB_ket = np.zeros(shape=(nB+1, 1))
	I_phB_ket.fill(1)

	I_phB_bra = np.zeros(shape=(1, nB+1))
	I_phB_bra.fill(1)

	for i in range(0, nA+1):
		na_bra = np.zeros(shape=(1, nA+1))
		na_bra[0][i] = 1
		
		na_bra = np.kron(na_bra, I_atA_bra)
		na_bra = np.kron(na_bra, I_phB_bra)
		na_bra = np.kron(na_bra, I_atB_bra)

		na_ket = np.zeros(shape=(nA+1, 1))
		na_ket[i][0] = 1

		na_ket = np.kron(na_ket, I_atA_ket)
		na_ket = np.kron(na_ket, I_phB_ket)
		na_ket = np.kron(na_ket, I_atB_ket)
		
		print(na_ket.shape, ro_dim)
		
		for j in range(0, nB+1):
			nb_bra = np.zeros(shape=(1, nB+1))
			nb_bra[0][i] = 1
			
			nb_bra = np.kron(I_atA_bra, nb_bra)
			nb_bra = np.kron(I_phB_bra, nb_bra)
			nb_bra = np.kron(nb_bra, I_atB_bra)

			nb_ket = np.zeros(shape=(nB+1, 1))
			nb_ket[i][0] = 1

			nb_ket = np.kron(I_atA_ket, nb_ket)
			nb_ket = np.kron(I_phB_ket, nb_ket)
			nb_ket = np.kron(nb_ket, I_atB_ket)
			# print(123)
			# tmp = ro

			# for i in range(0, ro_dim):
			# 	phB_i = (i >> 2) % 2
			# 	phA_i = int((i >> 2) / 2) >> 2
				
			# 	if phA_i == iA:
			# 		tmp.

			# 	for j in range(0, ro_dim):
			# 		phB_j = (j >> 2) % 2
			# 		phA_j = int((j >> 2) / 2) >> 2
			# 		print('(',i,' ',j,'):',phA_j, phB_j,)
			# nb_bra = np.zeros(shape=(1, nB+1))
			# nb_bra[0][i] = 1
			# na_bra = np.kron(np.identity(nA+1 + 4), na_bra)
			# na_bra = np.kron(na_bra, np.identity(4))

			# nb_ket = np.zeros(shape=(nB+1, 1))
			# nb_ket[i][0] = 1
			
			# print(na_ket)
			tmp = na_bra
			tmp = np.multiply(tmp, nb_bra)
			tmp = np.multiply(tmp, ro)
			tmp = np.multiply(tmp, nb_ket)
			tmp = np.multiply(tmp, na_ket)
			print('shape=',tmp.shape)
			ro_at += tmp
	return ro_at

def get_wdt(wt, exp_iHdt):
	wt = np.dot(exp_iHdt, wt)
	
	return wt

def get_ro(w):
	w = np.matrix(w)

	return np.multiply(w, w.getH())

# # !DONE
def is_hermitian(matrix):
	# wf_err.is_hermitian_err(matrix)

	diff = matrix - matrix.getH()
	
	return np.all(abs(diff) < precision)
# #----------------------------------------------------------------------------------------------------------------------
# # !DONE
# def is_unitary(matrix):
# 	wf_err.is_unitary_err(matrix)

# 	matrix_CT = matrix 
# 	diff = matrix * matrix_CT - matrix_CT * matrix
	
# 	return np.all(abs(diff) < precision)
# #######################################################################################################################

# def run(w0, H, t0, t1, initstate1, initstate2, ph_count1, ph_count2, nt = 200, not_empty = False, ymin=0, ymax=1, RWA=True, title='title', color='blue'):
# 	#------------------------------------------------------------------------------------------------------------------
# 	if not(nt in range(0, 501)): return -1
	
# 	if t0 < 0: return -1
# 	if t1 < 0: return -1
# 	if t0 >= t1: return -1

# 	if len(np.shape(H)) != 2: return -1
# 	if np.shape(H)[0] != np.shape(H)[1]: return -1 
# 	if np.shape(H)[0] != len(w0): return -1
# 	#------------------------------------------------------------------------------------------------------------------
# 	t = np.linspace(t0, t1, nt+1)
	
# 	dt = t[1] - t[0]
# 	#------------------------------------------------------------------------------------------------------------------
# 	state = []
	
# 	at1_count = len(initstate1[1])
# 	at2_count = len(initstate2[1])
	
# 	# for i in range(0, len(w0)):
# 	# 	t = i
# 	# 	t = t / pow(2, at2_count)
# 	# 	ph2_count = int(t / ph_count2)
# 	# 	t = t / ph_count2
# 	# 	t = t / pow(2, at2_count)
# 	# 	ph1_count = t
		
# 	# 	st2_number = at2_count
# 	# 	# st2_number = st2_number
# 	# 	# st2_number = (pow(2, ph1_count+at1_count) - i)% pow(2, at2_count)

		
# 	# 	at2_binary = bin(st2_number)[2:].zfill(at2_count)

# 	# 	state.append('[' + str(ph1_count)+ ' ' + str(ph2_count) + '|' + at2_binary + ']')
# 	# #------------------------------------------------------------------------------------------------------------------	
# 	# for i in range(0, len(w0)):
# 	# 	print(i, " ", state[i], i, '/', pow(2, ph2_count+at1_count+at2_count))
# 	# return
# 	w = []
	
# 	# print("w0:", w0.shape[0], w0.shape[1])
# 	# print("H:", H.shape[0], H.shape[1])

# 	# exp_iHdt = expm(np.array(H))
# 	exp_iHdt = expm(np.array(H) * complex(0,-1) * dt)
# 	# exp_iHdt = np.matrix(exp_iHdt)
# 	wt = w0
# 	# print(exp_iHdt)
# 	for i in range(0, nt+1):
# 		wt = get_wdt(wt, exp_iHdt)
# 		# wt = get_wt(w0, H, i*dt)
# 		if np.max(wt) > 1:
# 			sys.exit("Error\n") 
# 		w.append(np.abs(wt))
		
# 	w = np.array(w)
# 	#------------------------------------------------------------------------------------------------------------------
# 	# animator.make_plot3D(t, t0, t1, w, ymin=ymin, ymax=ymax, state=state, not_empty=not_empty, max_limit=max_limit)
# 	st = initstate2[0]*(pow(2, at2_count))
	
# 	for i in range(0, at2_count):
# 		st += pow(2, i) * initstate2[1][at2_count-i-1]
	
# 	for i in range(0, at1_count):
# 		st += (pow(2, i+at2_count) * (ph_count2+1)) * initstate1[1][at1_count-i-1]
	
# 	st += initstate1[0] * (pow(2, at1_count + at2_count) * (ph_count2+1))
	
# 	# print(st)
# 	#------------------------------------------------------------------------------------------------------------------
# 	# animator.make_plot3D(t, t0, t1, w, ymin=ymin, ymax=ymax, state=state, not_empty=not_empty, max_limit=max_limit)
	
# 	animator.make_plot(t, t0, t1, ymin, ymax, w[:,st], color, title=title)

# 	return

# def run2(w0, H_RWA, H_EXACT, t0, t1, initstate1, initstate2, ph_count1, ph_count2, nt = 200, not_empty = False, ymin=0, ymax=1, RWA=True, title='title', color='blue'):
# 	#------------------------------------------------------------------------------------------------------------------
# 	if not(nt in range(0, 501)): return -1
	
# 	if t0 < 0: return -1
# 	if t1 < 0: return -1
# 	if t0 >= t1: return -1

# 	if len(np.shape(H_RWA)) != 2: return -1
# 	if np.shape(H_RWA)[0] != np.shape(H_RWA)[1]: return -1 
# 	if np.shape(H_RWA)[0] != len(w0): return -1
	
# 	if len(np.shape(H_EXACT)) != 2: return -1
# 	if np.shape(H_EXACT)[0] != np.shape(H_EXACT)[1]: return -1 
# 	if np.shape(H_EXACT)[0] != len(w0): return -1
# 	#------------------------------------------------------------------------------------------------------------------
# 	t = np.linspace(t0, t1, nt+1)
	
# 	dt = t[1] - t[0]
# 	#------------------------------------------------------------------------------------------------------------------
# 	state = []
	
# 	at1_count = len(initstate1[1])
# 	at2_count = len(initstate2[1])
	
# 	w_RWA = []
# 	w_EXACT = []
	
# 	exp_iH_RWAdt = expm(np.array(H_RWA) * complex(0,-1) * dt)
# 	exp_iH_EXACTdt = expm(np.array(H_EXACT) * complex(0,-1) * dt)
	
# 	wt_RWA = w0
# 	wt_EXACT = w0
	
# 	for i in range(0, nt+1):
# 		wt_RWA = get_wdt(wt_RWA, exp_iH_RWAdt)
# 		wt_EXACT = get_wdt(wt_EXACT, exp_iH_EXACTdt)
		
# 		if np.max(wt_RWA) > 1 or np.max(wt_EXACT) > 1:
# 			sys.exit("Error\n") 
		
# 		w_RWA.append(np.abs(wt_RWA))
# 		w_EXACT.append(np.abs(wt_EXACT))
		
# 	w_RWA = np.array(w_RWA)
# 	w_EXACT = np.array(w_EXACT)
# 	#------------------------------------------------------------------------------------------------------------------
# 	# animator.make_plot3D(t, t0, t1, w, ymin=ymin, ymax=ymax, state=state, not_empty=not_empty, max_limit=max_limit)
# 	st = initstate2[0]*(pow(2, at2_count))
	
# 	for i in range(0, at2_count):
# 		st += pow(2, i) * initstate2[1][at2_count-i-1]
	
# 	for i in range(0, at1_count):
# 		st += (pow(2, i+at2_count) * (ph_count2+1)) * initstate1[1][at1_count-i-1]
	
# 	st += initstate1[0] * (pow(2, at1_count + at2_count) * (ph_count2+1))
	
# 	# print(st)
# 	#------------------------------------------------------------------------------------------------------------------
# 	# animator.make_plot3D(t, t0, t1, w, ymin=ymin, ymax=ymax, state=state, not_empty=not_empty, max_limit=max_limit)
	
# 	animator.make_plot2(t, t0, t1, ymin, ymax, w_RWA[:,st], w_EXACT[:,st])

# 	return