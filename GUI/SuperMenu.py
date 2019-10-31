# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SuperMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class SuperMenu(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(336, 281)
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 321, 251))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Workshop"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Status"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "Workshop 1"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("Form", "Clones Not Created"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
