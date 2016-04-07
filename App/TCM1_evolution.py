import main as TCM

from config import at_count_max
from PyQt4 import QtGui, QtCore

atoms = []       
       
RWA = True

def initAtomsComboBoxX(obj):
    for i in range(0, at_count_max):
	   	combobox = QtGui.QComboBox(obj.tabWidget)
	   	combobox.addItem("0")
	   	combobox.addItem("1")

	   	x = obj.init_ph_count.x() + int(obj.at_count.text()) * 70 * i
	   	y = obj.init_ph_count.y() + 70
	   	w = obj.init_ph_count.width()
	   	h = obj.init_ph_count.height()
	   	# combobox.setEditable(True)
	   	# combobox.setSizeAdjustPolicy(3)
	   	# combobox.setButtonSymbols(QtGui..NoButtons)
	   	# combobox.setEditable(true);
	   	# combobox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
	   	# combobox.lineEdit().setReadOnly(rue);
	   	# combobox.setAlignment(QtCore.Qt.AlignCenter)
	   	# combobox.label.setAlignment(QtCore.Qt.AlignCenter)
	   	# combobox.setItemData(0, QtCore.Qt.AlignRight, QtCore.Qt.TextAlignmentRole);
	   	combobox.setStyleSheet ("QComboBox::drop-down{border: 0;}")
	   	# combobox.setEditable(False)
	   	combobox.setGeometry(x, y, w, h)
	    	
	   	if i != 0: combobox.hide()
	    	
	   	atoms.append(combobox)

    return

def onAtCountButton(obj):
	if int(obj.at_count.text()) > obj.at_c:
		obj.at_c+=1
		atoms[obj.at_c].show()
	else:
		atoms[obj.at_c].hide()
		obj.at_c-=1

def onRunButton(obj):
    global RWA
    ph_count = int(obj.ph_count.text())
    at_count = int(obj.at_count.text())
    wc = float(obj.wc.text())
    wa = float(obj.wa.text())
    g = float(obj.g.text())
    	
    H = TCM.get_H(ph_count, at_count, wc, wa, g, RWA)
    print(H)
    print("RWA = ", RWA)
    at_list = []

    for i in range(0, obj.at_c+1):
    	at_list.append(int(atoms[i].currentText()))
    
    init_state = [int(obj.init_ph_count.text()), at_list]
    	
    w0 = TCM.get_w0(ph_count=ph_count, init_state=init_state)
    	
    t0 = int(obj.t0.text())
    t1 = int(obj.t1.text())
    	
    TCM.run(w0=w0, H=H, t0=t0, t1=t1, nt=500, initstate=init_state, ymin=0, ymax=1, not_empty=False)
    	
    return

def onRWAButton(obj):
	global RWA
	RWA = True
	obj.RWA_btn.setStyleSheet("background-color: #0095ff; color:white;")
	obj.exact_btn.setStyleSheet("background-color: #FFFFFF; color:#555;")
   
def onExactButton(obj):
	global RWA
	RWA = False
	obj.RWA_btn.setStyleSheet("background-color: #FFFFFF; color:#555;")
	obj.exact_btn.setStyleSheet("background-color: #0095ff; color:white;")