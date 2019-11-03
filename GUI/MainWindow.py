# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cit-gen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BaseWidget import BaseWidget
from VMWidget import VMWidget
from MaterialWidget import MaterialWidget
from SuperMenu import SuperMenu
from ManagerBox import ManagerBox

class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 590)#first was 768, 611
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 15, 668, 565))#third was 761, 571
        self.tabWidget.setObjectName("tabWidget")
        self.windowBox = QtWidgets.QWidget()
        self.windowBox.setObjectName("windowBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.windowBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 658, 521))#third was 751
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hLayout_windowBox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hLayout_windowBox.setContentsMargins(0, 0, 0, 0)
        self.hLayout_windowBox.setObjectName("hLayout_windowBox")
        self.workshopTree = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.workshopTree.itemClicked.connect(self.onItemSelected)
        self.workshopTree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.workshopTree.customContextMenuRequested.connect(self.showContextMenu)

        self.workshopTree.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.workshopTree.sizePolicy().hasHeightForWidth())
        self.workshopTree.setSizePolicy(sizePolicy)
        self.workshopTree.setMaximumSize(200,521)
        self.workshopTree.setObjectName("workshopTree")
        item_0 = QtWidgets.QTreeWidgetItem(self.workshopTree)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_0)
        item_3 = QtWidgets.QTreeWidgetItem(self.workshopTree)
        self.hLayout_windowBox.addWidget(self.workshopTree)
        self.actionEventBox = QtWidgets.QHBoxLayout()
        self.actionEventBox.setObjectName("actionEventBox")
        self.actionEventBox.addStretch(1)
        self.hLayout_windowBox.addLayout(self.actionEventBox)
        self.tabWidget.addTab(self.windowBox, "")
        
        
        # VBox Actions Tab
        self.superMenu = SuperMenu()
        self.superMenu_Form = QtWidgets.QWidget()
        self.superMenu.setupUi(self.superMenu_Form)
        self.superMenu_Form.setObjectName("superMenu")
        self.tabWidget.addTab(self.superMenu_Form, "")
        # self.superMenu = QtWidgets.QWidget()
        # self.superMenu.setObjectName("superMenu")
        # self.tabWidget.addTab(self.superMenu, "")
        

        # Frontend tab
        self.managerBox = ManagerBox()
        self.managerBox_Form = QtWidgets.QWidget()
        self.managerBox.setupUi(self.managerBox_Form)
        self.superMenu_Form.setObjectName("managerBox")
        self.tabWidget.addTab(self.managerBox_Form, "")
        # self.managerBox = QtWidgets.QWidget()
        # self.managerBox.setObjectName("managerBox")
        # self.tabWidget.addTab(self.managerBox, "")



        # MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 22))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Base Config Widget 
        self.baseWidget = BaseWidget()
        self.baseWidget_Form = QtWidgets.QWidget()
        self.baseWidget.setupUi(self.baseWidget_Form)
        # self.actionEventBox.addWidget(Form)

        # VM Config Widget
        self.vmWidget = VMWidget()
        self.vmWidget_Form = QtWidgets.QWidget()
        self.vmWidget.setupUi(self.vmWidget_Form)
        # self.actionEventBox.addWidget(Form)

        # Material Config Widget
        self.materialWidget = MaterialWidget()
        self.materialWidget_Form = QtWidgets.QWidget()
        self.materialWidget.setupUi(self.materialWidget_Form)
        # self.actionEventBox.addWidget(Form)

        # Context menu for blank space
        self.blankTreeContextMenu = QtWidgets.QMenu()
       	self.addWorkshop = self.blankTreeContextMenu.addAction("New Workshop")
       	self.addWorkshop.triggered.connect(self.addWorkshopActionEvent)
        self.importWorkshop = self.blankTreeContextMenu.addAction("Import Workshop from EBX archive")
        self.importWorkshop.triggered.connect(self.importActionEvent)
        self.downloadFromRepo = self.blankTreeContextMenu.addAction("Download Workshop From Repo")
        self.downloadFromRepo.triggered.connect(self.download)

        # Workshop context menu
        self.workshopContextMenu = QtWidgets.QMenu()
        self.addVM = self.workshopContextMenu.addAction("Add VM")
        self.addVM.triggered.connect(self.addVMActionEvent)
        self.addMaterial = self.workshopContextMenu.addAction("Add Material File")
        self.addMaterial.triggered.connect(self.addMaterialActionEvent)
        # Add line separator here
        self.createRDP = self.workshopContextMenu.addAction("Create RDP Files")
        self.createRDP.triggered.connect(self.createRDPActionEvent)
        # Add line separator here
        self.createGuac = self.workshopContextMenu.addAction("Create Guacamole Users")
        self.createGuac.triggered.connect(self.createGuacActionEvent)
        self.removeGuac = self.workshopContextMenu.addAction("Remove Guacamole Users")
        self.removeGuac.triggered.connect(self.removeGuacActionEvent)
        # Add line separator here
        self.removeWorkshop = self.workshopContextMenu.addAction("Remove Workshop")
        self.removeWorkshop.triggered.connect(self.removeWorkshopActionEvent)
        self.exportWorkshop = self.workshopContextMenu.addAction("Export Workshop")
        self.exportWorkshop.triggered.connect(self.exportWorkshopActionEvent)

       	# VM/Material context menu
        self.itemContextMenu = QtWidgets.QMenu()
        self.removeItem = self.itemContextMenu.addAction("Remove Workshop Item")
        self.removeItem.triggered.connect(self.removeVMActionEvent)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CIT-GEN"))
        self.workshopTree.headerItem().setText(0, _translate("MainWindow", "Workshops"))
        __sortingEnabled = self.workshopTree.isSortingEnabled()
        self.workshopTree.setSortingEnabled(False)
        self.workshopTree.topLevelItem(0).setText(0, _translate("MainWindow", "Workshop 1"))
        self.workshopTree.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "M: exercise.doc"))
        self.workshopTree.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "V: Kali"))
        self.workshopTree.topLevelItem(1).setText(0, "Workshop 2")
        self.workshopTree.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.windowBox), _translate("MainWindow", "Configuration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.superMenu_Form), _translate("MainWindow", "VBox Actions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.managerBox_Form), _translate("MainWindow", "Frontend"))

    def onItemSelected(self):
    	# Removes widget on the right side
    	rightPaneItem = self.actionEventBox.itemAt(0)
    	self.actionEventBox.removeItem(rightPaneItem)

    	# Set parent to none, if the removed widget wasn't a spacer item 
    	if(not isinstance(rightPaneItem, QtWidgets.QSpacerItem)):
    		rightPaneItem.widget().setParent(None)

    	# Places the widget on the right 
    	selectedItem = self.workshopTree.currentItem()
    	if(selectedItem.parent() == None):
    		self.actionEventBox.addWidget(self.baseWidget_Form)
    	elif(selectedItem.text(0)[0] == "V"):
    		self.actionEventBox.addWidget(self.vmWidget_Form)
    	elif(selectedItem.text(0)[0] == "M"):
    		self.actionEventBox.addWidget(self.materialWidget_Form)

    def showContextMenu(self, position):
    	
    	if(self.workshopTree.itemAt(position) == None):
    		self.blankTreeContextMenu.popup(self.workshopTree.mapToGlobal(position))
    	elif(self.workshopTree.itemAt(position).parent() == None):
    		self.workshopContextMenu.popup(self.workshopTree.mapToGlobal(position))
    	else:
    		self.itemContextMenu.popup(self.workshopTree.mapToGlobal(position))

    def addWorkshopActionEvent(self):
    	pass

    def importActionEvent(self):
    	pass

    def download(self):
    	pass

    def addVMActionEvent(self):
    	pass

    def addMaterialActionEvent(self):
    	pass

    def createRDPActionEvent(self):
    	pass

    def createGuacActionEvent(self):
    	pass

    def removeGuacActionEvent(self):
    	pass

    def removeWorkshopActionEvent(self):
    	pass

    def exportWorkshopActionEvent(self):
    	pass

    def removeVMActionEvent(self):
    	pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
