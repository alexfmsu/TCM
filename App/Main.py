from PyQt4 import QtCore, QtGui, uic
import os
import sys
import Main

from ssh import *
import lomonosov_panel
from TCM1_evolution import *
 
qtCreatorFile = "Main.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

connection = 0
        

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        init_ssh(self)   
        
        self.status = 0
        
        #--------------------------------------------------------------------------------------------------------------
        self.pc_btn.clicked.connect(self.onPCBtn)
        self.lomonosov_btn.clicked.connect(self.onLomonosovBtn)
        #--------------------------------------------------------------------------------------------------------------
        self.connect_btn.clicked.connect(self.onConnectBtn)
        self.disconnect_btn.clicked.connect(self.onDisconnectBtn)

        self.test_btn.clicked.connect(self.onTestBtn)
        self.regular4_btn.clicked.connect(self.onRegular4Btn)
        self.regular6_btn.clicked.connect(self.onRegular6Btn)
        #--------------------------------------------------------------------------------------------------------------
        self.initAtomsComboBox()
        self.at_count.valueChanged.connect(self.onAtCountBtn) 
        
        self.run_btn.clicked.connect(self.onRunBtn)
        #--------------------------------------------------------------------------------------------------------------
        self.lomonosov_group.hide()
        
        self.pc_btn.clicked.connect(self.onPCBtn)

        #--------------------------------------------------------------------------------------------------------------
        self.RWA_btn.clicked.connect(self.onRWABtn)
        self.onRWABtn()
        self.exact_btn.clicked.connect(self.onExactBtn)
        #--------------------------------------------------------------------------------------------------------------
        
        self.at_c = 0
        
    def onRWABtn(self):
        onRWAButton(self)
    def onExactBtn(self):
        onExactButton(self)
    #BEGIN-------------------------------------------------SWITCH-PANELS-----------------------------------------------
    def onPCBtn(self):
        self.pc_group.show()
        self.lomonosov_group.hide()
    
    def onLomonosovBtn(self):
    	self.pc_group.hide()
    	self.lomonosov_group.show()
   	#END---------------------------------------------------SWITCH-PANELS-----------------------------------------------
    
    #BEGIN-------------------------------------------------LOMONOSOV-PANEL---------------------------------------------
    def onConnectBtn(self):
    	lomonosov_panel.onConnectButton(self)
    
    def onDisconnectBtn(self):
    	lomonosov_panel.onDisconnectButton(self)
    #------------------------------------------------------------------------------------------------------------------
    def onTestBtn(self):
    	lomonosov_panel.onTestButton(self)

    def onRegular4Btn(self):
    	lomonosov_panel.onRegular4Button(self)

    def onRegular6Btn(self):
    	lomonosov_panel.onRegular6Button(self)
    #END---------------------------------------------------LOMONOSOV-PANEL---------------------------------------------
    
    #BEGIN-------------------------------------------------TCM1-EVOLUTION----------------------------------------------
    def initAtomsComboBox(self):
    	initAtomsComboBoxX(self)

    def onAtCountBtn(self):
    	onAtCountButton(self)
	    
    def onRunBtn(self):
    	onRunButton(self)
	#END---------------------------------------------------TCM1-EVOLUTION----------------------------------------------

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())