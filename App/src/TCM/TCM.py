from PyQt4 import QtGui, QtCore
from src.config import at_count_max

from math import sqrt
import src.TCM.hamiltotian as H1
import src.TCM.wave_function as wf
import numpy as np
from scipy.linalg import expm
import src.TCM.animator as animator
atoms = []       
c_atoms = []
	   
RWA = False
EXACT = False

c_spinbox = None
at_c = 0
certain = False


def whichway():
	ph_count = 21
	at_count = 3

	wc = 0.4
	wa = [0.4, 0.4, 0.4]
	g = [0.05, 0.05, 0.05]

	init_state = [0, [0, 1, 0]]
	certain_state1 = [0, [0, 0, 1]]
	certain_state2 = [0, [1, 0, 0]]

	w0 = wf.get_w0(ph_count=ph_count, init_state=init_state)
	
	t1 = 200

	title = 'Whichway' + '\n'
	title += r'$w_c =  ' + str(wc) + '\ МГц,$   ' + r'$w_a = ' + str(wa) + '\ МГц,$   ' + r'$g = ' + str(g) + '\ МГЦ,\ \ \ t = ' + str(t1) + '\ мкс$\n'
	color = 'red'

	H = H1.get_Hfieldw(ph_count, at_count, wc, wa, g) + H1.get_Hatomsw(ph_count, at_count, wc, wa, g)
	H += H1.get_Hint_RWAd(ph_count, at_count, wc, wa, g)
	H = np.matrix(H)

	print(wf.is_hermitian(H))

	wf.run_RWAw(w0=w0, H=H, t0=0, t1=t1, initstate=init_state, certain_state1=certain_state1, certain_state2=certain_state2, nt=500, ymin=0, ymax=1.005, title=title, color=color)
	
	return

# whichway()

def Frob(ro):
	return np.sqrt(np.real(np.trace(np.multiply(ro.conjugate(), ro))))

def onDiffChk(obj):
	global RWA

	ph_count = int(obj.ph_count.text())
	at_count = int(obj.at_count.text())
		
	wc = float(obj.wc.text())
	wa = float(obj.wa.text())
	g = float(obj.g.text())

	certain_state = None

	if obj.chk_certain.isChecked():
		at_list = []

		for i in range(0, at_c+1):
			at_list.append(int(c_atoms[i].currentText()))

		certain_state = [int(c_spinbox.text()), at_list]

	at_list = []

	for i in range(0, at_c+1):
		at_list.append(int(atoms[i].currentText()))
		
		init_state = [int(obj.init_ph_count.text()), at_list]
	
	w0 = wf.get_w0(ph_count=ph_count, init_state=init_state)
	
	t1 = int(obj.t1.text())

	nt = 250
	t = np.linspace(0, t1, nt+1)
	dt = t[1] - t[0]

	color = ''
	title = ''

	title = r"$\max\ |\ ||\rho(t)||\ -\ ||\rho_{_{RWA}}(t)||\ |\ (g/w_c)$"+'\n'
	title += r'$w_c =  ' + str(wc) + '\ МГц,$   ' + r'$w_a = ' + str(wa) + '\ МГц,$   ' + r'$g = ' + str(g) + '\ МГЦ,$   ' + r'$t = ' + str(t1) + '\ мкс$'
	
	X = []
	Y = []

	G = np.linspace(0, wc, nt)

	# H_field = H1.get_Hfield(ph_count, at_count, wc, wa, g)
	# H_atoms = H1.get_Hatoms(ph_count, at_count, wc, wa, g)

	# H_field_atoms = H_field + H_atoms

	# exp_iHdt_EXACT_F_A = expm(np.array(H_field_atoms) * complex(0,-1) * dt)

	nT = 500
	
	t = np.linspace(0, t1, nT+1)
	
	dt = t[1] - t[0]

	for g in G:
		max_norm = 0

		H_RWA = H1.get_H_RWA(ph_count, at_count, wc, wa, g)
		H_EXACT = H1.get_H_EXACT(ph_count, at_count, wc, wa, g)

		exp_RWA = expm(np.array(H_RWA) * complex(0,-1) * dt)
		exp_EXACT = expm(np.array(H_EXACT) * complex(0,-1) * dt)
		
		wt_RWA = wt_EXACT = w0

		for i in range(0, nT+1):
			wt_RWA = wf.get_wdt(wt_RWA, exp_RWA)	
			wt_EXACT = wf.get_wdt(wt_EXACT, exp_EXACT)	
			
			# wt_RWA = wf.get_wt(w0, H_RWA, t1)	
			# wt_EXACT = wf.get_wt(w0, H_EXACT, t1)	
			ro_RWA = wf.get_ro(wt_RWA)
			ro_EXACT = wf.get_ro(wt_EXACT)
			
			if(Frob(ro_RWA) < 0):
				print(Frob(ro_RWA))

			if(Frob(ro_EXACT) < 0):
				print(Frob(ro_EXACT))
			
			# d_ro = ro_RWA - ro_EXACT
			norm = abs(Frob(ro_RWA) - Frob(ro_EXACT))
		
			if norm > max_norm:
				max_norm = norm
		# norm_roRWA = sqrt(np.real(np.trace(np.multiply(ro_RWA.conjugate(), ro_RWA))))
		# norm_roEXACT = sqrt(np.real(np.trace(np.multiply(ro_EXACT.conjugate(), ro_EXACT))))
		# norm = abs(norm_roEXACT - norm_roRWA)

		Y.append(max_norm)

	G /= wc

	animator.make_plotdiff(G, G[0], G[nt-1], 0, 2, Y, title=title, X=r'$g/w_{c}$', Y = r'$||\Delta\rho_t||$'+'    ', rotation=0)

	return

def initAtomsComboBoxX(obj):
	global c_spinbox

	c_spinbox = QtGui.QSpinBox(obj.tab)

	x = obj.chk_certain.x()
	y = obj.chk_certain.y() + 40
	w = obj.init_ph_count.width() + 3
	h = obj.init_ph_count.height()

	
	c_spinbox.setAlignment(QtCore.Qt.AlignHCenter)
	c_spinbox.setAlignment(QtCore.Qt.AlignHCenter)
	c_spinbox.setGeometry(x, y, w, h)

	c_spinbox.hide()

	for i in range(0, at_count_max):
		combobox = QtGui.QComboBox(obj.tab)
		
		x = obj.init_ph_count.x() + 75 * int(obj.at_count.text()) * i
		y = obj.init_ph_count.y() + 40
		w = obj.init_ph_count.width() + 3
		h = obj.init_ph_count.height()
		
		combobox.addItem("     0")
		combobox.addItem("     1")
		combobox.setGeometry(x, y, w, h)
			
		if i != 0: combobox.hide()
			
		atoms.append(combobox)
		#------------------------
		combobox = QtGui.QComboBox(obj.tab)

		x = obj.chk_certain.x() + 75 * int(obj.at_count.text()) * i
		y = obj.chk_certain.y() + 80
		w = obj.init_ph_count.width() + 3
		h = obj.init_ph_count.height()

		combobox.addItem("     0")
		combobox.addItem("     1")
		combobox.setGeometry(x, y, w, h)

		combobox.hide()

		c_atoms.append(combobox)
	
	return

def onAtCountButton(obj):
	global at_c

	if int(obj.at_count.text()) > at_c:
		at_c += 1
	
		atoms[at_c].show()
		if obj.chk_certain.isChecked(): c_atoms[at_c].show()
	else:
		atoms[at_c].hide()
		if obj.chk_certain.isChecked(): c_atoms[at_c].hide()
		
		at_c -= 1

	return

def onInitChk(obj):
	c_spinbox.hide()
	
	for i in range(0, len(c_atoms)):
		c_atoms[i].hide()
	
	return

def on3DChk(obj):
	c_spinbox.hide()
	
	for i in range(0, len(c_atoms)):
		c_atoms[i].hide()
	
	return

def onCertainChk(obj):
	c_spinbox.show()
	c_spinbox.setValue(int(obj.ph_count.text()))
	
	for i in range(0, int(obj.at_count.text())):
		c_atoms[i].show()
	
	return

def onRunButton(obj):
	if obj.chk_diff.isChecked():
		onDiffChk(obj)
		return

	global RWA

	ph_count = int(obj.ph_count.text())
	at_count = int(obj.at_count.text())
		
	wc = float(obj.wc.text())
	wa = float(obj.wa.text())
	g = float(obj.g.text())

	certain_state = None

	if obj.chk_certain.isChecked():
		at_list = []

		for i in range(0, at_c+1):
			at_list.append(int(c_atoms[i].currentText()))

		certain_state = [int(c_spinbox.text()), at_list]

	at_list = []

	for i in range(0, at_c+1):
		at_list.append(int(atoms[i].currentText()))
		
		init_state = [int(obj.init_ph_count.text()), at_list]
	
	w0 = wf.get_w0(ph_count=ph_count, init_state=init_state)
	
	t = int(obj.t1.text())

	color = ''
	title = ''

	if RWA and not EXACT:
		color = 'blue'
		title += r'$RWA$'+'\n'
	elif not RWA and EXACT:
		color = 'red'
		title += r'$Exact$' + ' ' + r'$solution$'+'\n'
	elif RWA and EXACT:
		title += r'$RWA\ vs\ Exact$'+'\n'
	
	title += r'$w_c =  ' + str(wc) + '\ МГц,$   ' + r'$w_a = ' + str(wa) + '\ МГц,$   ' + r'$g = ' + str(g) + '\ МГц$'
	
	if RWA and not EXACT: 
		H = H1.get_H_RWA(ph_count, at_count, wc, wa, g)
		
		if obj.chk_init.isChecked():
			wf.run_RWA(w0=w0, H=H, t0=0, t1=t, nt=500, initstate=init_state, certain_state=init_state, ymin=0, ymax=1.005, title=title, color=color)
		elif obj.chk_certain.isChecked():
			wf.run_RWA(w0=w0, H=H, t0=0, t1=t, nt=500, initstate=init_state, certain_state=certain_state, ymin=0, ymax=1.005, title=title, color=color)
		elif obj.chk_3D.isChecked():
			wf.run_RWA_3D(w0=w0, H=H, t0=0, t1=t, nt=500, initstate=init_state, ymin=0, ymax=1.005, title=title, color=color)
	elif not RWA and EXACT:
		H = H1.get_H_EXACT(ph_count, at_count, wc, wa, g)
		
		if obj.chk_init.isChecked():
			wf.run_EXACT(w0=w0, H=H, t0=0, t1=t, nt=500, initstate=init_state, certain_state=init_state, ymin=0, ymax=1.005, title=title, color=color)
		elif obj.chk_certain.isChecked():
			wf.run_EXACT(w0=w0, H=H, t0=0, t1=t, nt=500, initstate=init_state, certain_state=certain_state, ymin=0, ymax=1.005, title=title, color=color)
		elif obj.chk_3D.isChecked():
			wf.run_EXACT_3D(w0=w0, H=H, t0=0, t1=t, nt=500, initstate=init_state, ymin=0, ymax=1.005, title=title, color=color)
	elif RWA and EXACT:
		H_RWA = H1.get_H_RWA(ph_count, at_count, wc, wa, g)
		
		H_EXACT = H1.get_H_EXACT(ph_count, at_count, wc, wa, g)
		
		if obj.chk_init.isChecked():
			wf.run2(w0=w0, H_RWA=H_RWA, H_EXACT=H_EXACT, t0=0, t1=t, nt=500, initstate=init_state, certain_state=init_state, ymin=0, ymax=1.005, title=title)
		elif obj.chk_certain.isChecked():
			wf.run2(w0=w0, H_RWA=H_RWA, H_EXACT=H_EXACT, t0=0, t1=t, nt=500, initstate=init_state, certain_state=certain_state, ymin=0, ymax=1.005, title=title)
	return

def onRWA(obj):
	global RWA
	
	if not RWA:
		obj.RWA_btn.setStyleSheet("background-color: #0095ff; color:white;")
		RWA = True
	else:
		obj.RWA_btn.setStyleSheet("background-color: #FFFFFF; color:#555;")
		RWA = False
	
	return

def onExactButton(obj):
	global EXACT
	
	if not EXACT:
		obj.exact_btn.setStyleSheet("background-color: #0095ff; color:white;")
		EXACT = True
	else:
		obj.exact_btn.setStyleSheet("background-color: #FFFFFF; color:#555;")
		EXACT = False
	
	return