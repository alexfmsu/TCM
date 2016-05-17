from PyQt4 import QtCore, QtGui, uic

import sys

from src.supercomputer.ssh import *
import src.supercomputer.lomonosov.lomonosov_panel as lomonosov_panel

import src.TCM.TCM as TC
import src.TCM2.TCM as TC2
import src.Entanglement.Entanglement as Ent
 
qtCreatorFile = "Main.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        #--------------------------------------------------------------------------------------------------------------
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #--------------------------------------------------------------------------------------------------------------
        self.lomonosov_group.hide()
        
        self.pc_btn.clicked.connect(self.onPCBtn)
        self.lomonosov_btn.clicked.connect(self.onLomonosovBtn)
        
        self.pc_btn.hide()
        self.lomonosov_btn.hide()
        #--------------------------------------------------------------------------------------------------------------
        
        #BEGIN---------------------------------------------LOMONOSOV---------------------------------------------------
        init_ssh(self)   
        
        self.connect_btn.clicked.connect(self.onConnectBtn)
        self.disconnect_btn.clicked.connect(self.onDisconnectBtn)

        self.test_btn.clicked.connect(self.onTestBtn)
        self.regular4_btn.clicked.connect(self.onRegular4Btn)
        self.regular6_btn.clicked.connect(self.onRegular6Btn)
        #END-----------------------------------------------LOMONOSOV---------------------------------------------------
        
        #BEGIN---------------------------------------------TCM---------------------------------------------------------
        self.onRWABtn()
        self.exact_btn.setStyleSheet("background-color: #FFFFFF; color:#555;")
        
        self.RWA_btn.clicked.connect(self.onRWABtn)
        self.exact_btn.clicked.connect(self.onExactBtn)
        
        self.initAtomsComboBox()
        self.at_count.valueChanged.connect(self.onAtCountBtn) 
        
        self.run_btn.clicked.connect(self.onRunBtn)
        
        self.chk_init.clicked.connect(self.onInitChk)
        self.chk_certain.clicked.connect(self.onCertainChk)
        self.chk_3D.clicked.connect(self.on3DChk)
        #END-----------------------------------------------TCM---------------------------------------------------------
        
        #BEGIN---------------------------------------------TCM-2-------------------------------------------------------
        self.at_c2_1 = 0
        self.at_c2_2 = 0
        
        self.onRWA2Btn()
        self.RWA2_btn.setStyleSheet("background-color: #0095ff; color:white;")
        
        self.RWA2_btn.clicked.connect(self.onRWA2Btn)
        self.exact2_btn.clicked.connect(self.onExact2Btn)
        
        self.initAtoms2_1ComboBox()
        self.initAtoms2_2ComboBox()
        self.at_count2_1.valueChanged.connect(self.onAtCount2_1Btn) 
        self.at_count2_2.valueChanged.connect(self.onAtCount2_2Btn) 
        
        self.run2_btn.clicked.connect(self.onRun2Btn)
        #END-----------------------------------------------TCM-2-------------------------------------------------------
        
        #BEGIN---------------------------------------------ENTANGLEMENT------------------------------------------------
        #self.runEnt_btn.clicked.connect(self.onRunEntBtn)
        #END-----------------------------------------------ENTANGLEMENT------------------------------------------------
        
        return

    #BEGIN-------------------------------------------------TCM---------------------------------------------------------    
    def onRWABtn(self):
        TC.onRWA(self)
    
    def onExactBtn(self):
        TC.onExactButton(self)
    #------------------------------------------------------------------------------------------------------------------
    def initAtomsComboBox(self):
        TC.initAtomsComboBoxX(self)

    def onAtCountBtn(self):
        TC.onAtCountButton(self)
    #------------------------------------------------------------------------------------------------------------------
    def onRunBtn(self):
        TC.onRunButton(self)
    #------------------------------------------------------------------------------------------------------------------
    def onInitChk(self):
        TC.onInitChk(self)
    
    def onCertainChk(self):
        TC.onCertainChk(self)
    
    def on3DChk(self):
        TC.on3DChk(self)
    #END---------------------------------------------------TCM---------------------------------------------------------    
    
    #BEGIN-------------------------------------------------TCM-2-------------------------------------------------------    
    def onRWA2Btn(self):
        TC2.onRWA2Button(self)
    
    def onExact2Btn(self):
        TC2.onExact2Button(self)
    #------------------------------------------------------------------------------------------------------------------
    def initAtoms2_1ComboBox(self):
        TC2.initAtoms2_1ComboBox(self)

    def initAtoms2_2ComboBox(self):
        TC2.initAtoms2_2ComboBox(self)

    def onAtCount2_1Btn(self):
        TC2.onAtCount2_1Button(self)
    
    def onAtCount2_2Btn(self):
        TC2.onAtCount2_2Button(self)
    #------------------------------------------------------------------------------------------------------------------
    def onRun2Btn(self):
        TC2.onRunButton(self)
    #END---------------------------------------------------TCM-2-------------------------------------------------------    
    
    #BEGIN-------------------------------------------------ENTANGLEMENT------------------------------------------------    
    #def onRunEntBtn(self):
    #    Ent.onRunButton(self)
    #END---------------------------------------------------ENTANGLEMENT------------------------------------------------    
    
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
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    window = MyApp()
    window.show()
    
    sys.exit(app.exec_())