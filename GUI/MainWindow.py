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
# from ManagerBox import ManagerBox

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
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.hLayout_windowBox.addWidget(self.workshopTree)
        self.actionEventBox = QtWidgets.QHBoxLayout()
        self.actionEventBox.setObjectName("actionEventBox")
        self.hLayout_windowBox.addLayout(self.actionEventBox)
        self.tabWidget.addTab(self.windowBox, "")
        # self.superMenu = QtWidgets.QWidget()
        self.superMenu = SuperMenu()
        self.superMenu_Form = QtWidgets.QWidget()

        

        self.superMenu.setupUi(superMenu_Form)
        self.superMenu_Form.setObjectName("superMenu")

        # self.superMenu.setObjectName("superMenu")
        # self.tabWidget.addTab(self.superMenu, "")
        self.tabWidget.addTab(self.superMenu_Form, "")

        self.managerBox = QtWidgets.QWidget()
        self.managerBox.setObjectName("managerBox")
        self.tabWidget.addTab(self.managerBox, "")
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
        # self.baseWidget = BaseWidget()
        # Form = QtWidgets.QWidget()
        # self.baseWidget.setupUi(Form)
        # self.actionEventBox.addWidget(Form)

        # VM Config Widget
        # self.vmWidget = VMWidget()
        # Form = QtWidgets.QWidget()
        # self.vmWidget.setupUi(Form)
        # self.actionEventBox.addWidget(Form)

        # Material Config Widget
        self.materialWidget = MaterialWidget()
        Form = QtWidgets.QWidget()
        self.materialWidget.setupUi(Form)
        self.actionEventBox.addWidget(Form)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CIT-GEN"))
        self.workshopTree.headerItem().setText(0, _translate("MainWindow", "Workshops"))
        __sortingEnabled = self.workshopTree.isSortingEnabled()
        self.workshopTree.setSortingEnabled(False)
        self.workshopTree.topLevelItem(0).setText(0, _translate("MainWindow", "Workshop 1"))
        self.workshopTree.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "M: exercise.doc"))
        self.workshopTree.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "V: Kali"))
        self.workshopTree.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.windowBox), _translate("MainWindow", "Configuration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.superMenu), _translate("MainWindow", "VBox Actions"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.managerBox), _translate("MainWindow", "Frontend"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())