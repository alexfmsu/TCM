from src.config import at_count_max
from PyQt4 import QtGui, QtCore

import numpy as np
from scipy.linalg import expm

import src.TCM2.hamiltotian as H2
import src.Entanglement.wave_function as wf

atoms = []       
       
RWA = False
EXACT = False


def onRunButton(obj):
	alpha = float(obj.alpha.text())
	
	init_phA_count = int(obj.init_phA_count.text())
	A2 = int(obj.atA2.text())
	
	B2 = int(obj.atB2.text())
	init_phB_count = int(obj.init_phB_count.text())
	
	phA_count = int(obj.phA_count.text())
	wcA = float(obj.wcA.text())
	waA = float(obj.waA.text())
	gA = float(obj.gA.text())
	
	phB_count = int(obj.phB_count.text())
	wcB = float(obj.wcB.text())
	waB = float(obj.waB.text())
	gB = float(obj.gB.text())
	init_phA_count = int(obj.init_phA_count.text())
	
	m = float(obj.m_ent.text())
	
	t = float(obj.t_ent.text())
	
	print('alpha = ', alpha)
	print('')
	print('init_phA_count = ', init_phA_count)
	print('A2 = ', A2)
	print('')
	print('init_phB_count = ', init_phB_count)
	print('B2 = ', B2)
	print('')
	print('phA_count = ', phA_count)
	print('wcA = ', wcA)
	print('waA = ', waA)
	print('gA = ', gA)
	print('')
	print('phB_count = ', phB_count)
	print('wcB = ', wcB)
	print('waB = ', waB)
	print('gB = ', gB)
	print('')
	print('m = ', m)
	print('')
	print('t = ', t)
	
	H = H2.get_H(phA_count, 2, wcA, waA, gA, phB_count, 2, wcB, waB, gB, m, RWA=True)

	w0 = wf.get_w0(phA_count, init_phA_count, A2, phB_count, init_phB_count, B2, alpha)
	ro0 = wf.get_ro(w0)

	ro_at = wf.get_roAt(ro0, phA_count, phB_count)
	print(ro_at.shape)
	# print(w0)
	# print(ro_at)

	# print(H)
		
	
	
	
