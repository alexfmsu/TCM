import main as TCM

from src.TCM.config import at_count_max
from src.TCM2.hamiltotian import *
from PyQt4 import QtGui, QtCore

atoms = []       
       
RWA = False
EXACT = False

def initAtomsComboBoxX2(obj):
    for i in range(0, at_count_max):
	   	combobox = QtGui.QComboBox(obj.tab_2)
	   	
	   	x = obj.init_ph_count.x() + int(obj.at_count.text()) * 75 * i
	   	y = obj.init_ph_count.y() + 70
	   	w = obj.init_ph_count.width() + 3
	   	h = obj.init_ph_count.height()
	   	
	   	combobox.addItem("     0")
	   	combobox.addItem("     1")
	   	combobox.setGeometry(x, y, w, h)
	    	
	   	if i != 0: combobox.hide()
	    	
	   	atoms.append(combobox)

    return

def onAtCount2Button(obj):
	print(obj.at_c2)
	if int(obj.at_count2.text()) > obj.at_c2:
		obj.at_c2 += 1
		atoms[obj.at_c2].show()
	else:
		atoms[obj.at_c2].hide()
		obj.at_c2 -= 1

	return
	
def onRunButton(obj):
	global RWA
	return
    # ph_count = int(obj.ph_count.text())
    # at_count = int(obj.at_count.text())
    
    # wc = float(obj.wc.text())
    # wa = float(obj.wa.text())
    # g = float(obj.g.text())
    	
    # at_list = []

    # for i in range(0, obj.at_c + 1):
    # 	at_list.append(int(atoms[i].currentText()))
    
    # init_state = [int(obj.init_ph_count.text()), at_list]
    	
    # w0 = TCM.get_w0(ph_count=ph_count, init_state=init_state)
    	
    # t = int(obj.t1.text())

    # if RWA:
    # 	color = 'blue'
    # 	title = r'$RWA$'+'\n'
    # 	title += r'$w_c =  ' + str(wc) + ',$   ' + r'$w_a = ' + str(wa) + ',$   ' + r'$g = ' + str(g) + '$'
    # else:
    # 	color = 'red'
    # 	title = r'$Exact solution$'+'\n'

    # if RWA and not EXACT: 
    # 	H = TCM.get_H(ph_count, at_count, wc, wa, g, RWA=True)
    # 	print(H)
    # 	TCM.run(w0=w0, H=H, t0=0, t1=t, nt=500, initstate=init_state, ymin=0, ymax=1, RWA=RWA, title=title, color=color)
    # elif not RWA and EXACT:
    # 	H = TCM.get_H(ph_count, at_count, wc, wa, g, RWA=False)
    # 	TCM.run(w0=w0, H=H, t0=0, t1=t, nt=500, initstate=init_state, ymin=0, ymax=1, RWA=RWA, title=title, color=color)
    # elif RWA and EXACT:
    # 	H_RWA = TCM.get_H(ph_count, at_count, wc, wa, g, RWA=True)
    # 	H_EXACT = TCM.get_H(ph_count, at_count, wc, wa, g, RWA=False)
    # 	TCM.run2(w0=w0, H_RWA=H_RWA, H_EXACT=H_EXACT, t0=0, t1=t, nt=500, initstate=init_state, ymin=0, ymax=1)
    

def onRWA2Button(obj):
	global RWA
	
	# if not RWA:
	# 	obj.RWA_btn.setStyleSheet("background-color: #0095ff; color:white;")
	# 	RWA = True
	# else:
	# 	obj.RWA_btn.setStyleSheet("background-color: #FFFFFF; color:#555;")
	# 	RWA = False
	
def onExact2Button(obj):
	global EXACT
	
	# if not EXACT:
	# 	obj.exact_btn.setStyleSheet("background-color: #0095ff; color:white;")
	# 	EXACT = True
	# else:
	# 	obj.exact_btn.setStyleSheet("background-color: #FFFFFF; color:#555;")
	# 	EXACT = False
	# # obj.RWA_btn.setStyleSheet("background-color: #FFFFFF; color:#555;")
	