import time
import numpy as np
from scipy.linalg import expm

from hamiltotian import *
from wave_function import *
#----------------------------------------------------------------------------------------------------------------------
ph_count = 2	# total number of photons
at_count = 2	# total number of atoms 

wc = 0.2
wa = 0.4
g = 0.5

t0 = 0
t1 = 10
#######################################################################################################################
# time1 = time.time()
#######################################################################################################################
# init_state = [2, [0, 0]]
#----------------------------------------------------------------------------------------------------------------------
# H = get_H(ph_count=ph_count, at_count=at_count, wc=wc, wa=wa, g=g)
# H = get_H(ph_count=ph_count, at_count=at_count, wc=wc, wa=wa, g=g, RWA=False)

# write_to_file(H, 'H')
#----------------------------------------------------------------------------------------------------------------------
# w0 = get_w0(ph_count=ph_count, init_state=init_state)
# ro = get_ro(w0)

# wt = get_wt(w0=w0, H=H, t=1)
# rot = get_ro(wt)
# #----------------------------------------------------------------------------------------------------------------------
# print(is_hermitian(H))
# print(is_unitary(rot))
# print(H)
# # print(rot)
# print(wave.is_hermitian(ro))
# print(wave.is_hermitian(rot))
# print(np.matrix.getH(rot))

# print(np.matrix.getH())

# wt = wave.get_wtlist(w0=w0, H=H, t=t)
#######################################################################################################################
# run(w0=w0, H=H, t0=t0, t1=t1, nt=200, initstate=initstate, ymin=0, ymax=1, not_empty=False, max_limit=0)
#######################################################################################################################
# time2 = time.time()

# print('Time:', time2-time1)
#----------------------------------------------------------------------------------------------------------------------
