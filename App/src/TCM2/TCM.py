from src.config import at_count2_max
from src.TCM2.hamiltotian import *
import src.TCM2.wave_function as wf2
from PyQt4 import QtGui, QtCore

import numpy as np
from scipy.linalg import expm

atoms2_1 = []       
atoms2_2 = []       
       
RWA = False
EXACT = False

def initAtoms2_1ComboBox(obj):
    for i in range(0, at_count2_max):
	   	combobox = QtGui.QComboBox(obj.tab_2)
	   	
	   	x = obj.init_ph_count.x() + int(obj.at_count.text()) * 75 * i
	   	y = obj.init_ph_count.y() + 40
	   	w = obj.init_ph_count.width() + 3
	   	h = obj.init_ph_count.height()
	   	
	   	combobox.addItem("     0")
	   	combobox.addItem("     1")
	   	combobox.setGeometry(x, y, w, h)
	    	
	   	if i != 0: combobox.hide()
	    	
	   	atoms2_1.append(combobox)

    return

def initAtoms2_2ComboBox(obj):
    for i in range(0, at_count2_max):
	   	combobox = QtGui.QComboBox(obj.tab_2)
	   	
	   	x = obj.init_ph_count.x() + int(obj.at_count.text()) * 75 * i + 520
	   	y = obj.init_ph_count.y() + 50
	   	w = obj.init_ph_count.width() + 3
	   	h = obj.init_ph_count.height()
	   	
	   	combobox.addItem("     0")
	   	combobox.addItem("     1")
	   	combobox.setGeometry(x, y, w, h)
	    	
	   	if i != 0: combobox.hide()
	    	
	   	atoms2_2.append(combobox)

    return

def onAtCount2_1Button(obj):
	if int(obj.at_count2_1.text()) > obj.at_c2_1:
		obj.at_c2_1 += 1
		atoms2_1[obj.at_c2_1].show()
	else:
		atoms2_2[obj.at_c2_1].hide()
		obj.at_c2_1 -= 1

	return

def onAtCount2_2Button(obj):
	if int(obj.at_count2_2.text()) > obj.at_c2_2:
		obj.at_c2_2 += 1
		atoms2_2[obj.at_c2_2].show()
	else:
		atoms2_2[obj.at_c2_2].hide()
		obj.at_c2_2 -= 1

	return
	
def onRunButton(obj):
	global RWA
	ph_count1 = int(obj.ph_count2_1.text())
	ph_count2 = int(obj.ph_count2_2.text())
	at_count1 = int(obj.at_count2_1.text())
	at_count2 = int(obj.at_count2_2.text())
	
	wc1 = float(obj.wc2_1.text())
	wc2 = float(obj.wc2_2.text())
	wa1 = float(obj.wa2_1.text())
	wa2 = float(obj.wa2_2.text())
	g1 = float(obj.g2_1.text())
	g2 = float(obj.g2_2.text())

	m = float(obj.m.text())

	at1_list = []
	at2_list = []

	for i in range(0, obj.at_c2_1 + 1):
		at1_list.append(int(atoms2_1[i].currentText()))

	for i in range(0, obj.at_c2_2 + 1):
		at2_list.append(int(atoms2_2[i].currentText()))
	
	init_state1 = [int(obj.init_ph_count1.text()), at1_list]
	init_state2 = [int(obj.init_ph_count2.text()), at2_list]

	# init_state1 = [2, [0]]
	# init_state2 = [0, [0]]

	w0 = wf2.get_w0(ph_count1=ph_count1, init_state1=init_state1, ph_count2=ph_count2, init_state2=init_state2)
	t = int(obj.t2.text())

	color = ''
	title = ''

	if RWA and not EXACT:
		color = 'blue'
		title = r'$RWA$'+'\n'
	elif not RWA and EXACT:
		color = 'red'
		title = r'$Exact$' + ' ' + r'$solution$'+'\n'
	elif RWA and EXACT:
		title += r'$RWA\ vs\ Exact$'+'\n'
    
	title += r'$Cavity\ 1:\ w_c =  ' + str(wc1) + '\ МГц,$   ' + r'$w_a = ' + str(wa1) + '\ МГц,$   ' + r'$g = ' + str(g1) + '\ МГц$' + '\n'
	title += r'$Cavity\ 2:\ w_c =  ' + str(wc2) + '\ МГц,$   ' + r'$w_a = ' + str(wa2) + '\ МГц,$   ' + r'$g = ' + str(g2) + '\ МГц$' + '\n'
	title += r'$\mu = ' + str(m) + '\ МГц$'

	if RWA and not EXACT:
		H = get_H(ph_count1, at_count1, wc1, wa1, g1, ph_count2, at_count2, wc2, wa2, g2, m, RWA=True)
		wf2.run(w0=w0, H=H, t0=0, t1=t, nt=500, initstate1=init_state1, initstate2=init_state2, ph_count1=ph_count1, ph_count2=ph_count2, ymin=0, ymax=1, RWA=RWA, title=title, color=color)
	elif not RWA and EXACT:
		H = get_H(ph_count1, at_count1, wc1, wa1, g1, ph_count2, at_count2, wc2, wa2, g2, m, RWA=False)
		wf2.run(w0=w0, H=H, t0=0, t1=t, nt=500, initstate1=init_state1, initstate2=init_state2, ph_count1=ph_count1, ph_count2=ph_count2, ymin=0, ymax=1, RWA=RWA, title=title, color=color)
	elif RWA and EXACT:
		H_RWA = get_H(ph_count1, at_count1, wc1, wa1, g1, ph_count2, at_count2, wc2, wa2, g2, m, RWA=True)
		H_EXACT = get_H(ph_count1, at_count1, wc1, wa1, g1, ph_count2, at_count2, wc2, wa2, g2, m, RWA=False)
		wf2.run2(w0=w0, H_RWA=H_RWA, H_EXACT=H_EXACT, t0=0, t1=t, nt=500, initstate1=init_state1, initstate2=init_state2, ph_count1=ph_count1, ph_count2=ph_count2, ymin=0, ymax=1, RWA=RWA, title=title, color=color)
	
	return

def onRWA2Button(obj):
	global RWA
	
	if not RWA:
		obj.RWA2_btn.setStyleSheet("background-color: #0095ff; color:white;")
		RWA = True
	else:
		obj.RWA2_btn.setStyleSheet("background-color: #FFFFFF; color:#555;")
		RWA = False
	
def onExact2Button(obj):
	global EXACT
	
	if not EXACT:
		obj.exact2_btn.setStyleSheet("background-color: #0095ff; color:white;")
		EXACT = True
	else:
		obj.exact2_btn.setStyleSheet("background-color: #FFFFFF; color:#555;")
		EXACT = False
	