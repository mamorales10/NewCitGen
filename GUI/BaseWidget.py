# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BaseWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class BaseWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(444, 387)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 445, 372))
        self.layoutWidget.setObjectName("layoutWidget")
        self.outerVertBox = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.outerVertBox.setContentsMargins(0, 0, 0, 0)
        self.outerVertBox.setObjectName("outerVertBox")
        self.vBoxManageHorBox = QtWidgets.QHBoxLayout()
        self.vBoxManageHorBox.setObjectName("vBoxManageHorBox")
        self.vBoxManageLabel = QtWidgets.QLabel(self.layoutWidget)
        self.vBoxManageLabel.setObjectName("vBoxManageLabel")
        self.vBoxManageHorBox.addWidget(self.vBoxManageLabel)
        self.chooseVBoxPathButton = QtWidgets.QToolButton(self.layoutWidget)
        self.chooseVBoxPathButton.setObjectName("chooseVBoxPathButton")
        self.vBoxManageHorBox.addWidget(self.chooseVBoxPathButton)
        self.vBoxMangeLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.vBoxMangeLineEdit.setObjectName("vBoxMangeLineEdit")
        self.vBoxManageHorBox.addWidget(self.vBoxMangeLineEdit)
        self.outerVertBox.addLayout(self.vBoxManageHorBox)
        self.ipAddressHorBox = QtWidgets.QHBoxLayout()
        self.ipAddressHorBox.setObjectName("ipAddressHorBox")
        self.ipAddressLabel = QtWidgets.QLabel(self.layoutWidget)
        self.ipAddressLabel.setObjectName("ipAddressLabel")
        self.ipAddressHorBox.addWidget(self.ipAddressLabel)
        self.ipAddressLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.ipAddressLineEdit.setText("127.0.0.1")
        self.ipAddressLineEdit.setObjectName("ipAddressLineEdit")
        self.ipAddressHorBox.addWidget(self.ipAddressLineEdit)
        self.outerVertBox.addLayout(self.ipAddressHorBox)
        self.baseGroupNameHorBox = QtWidgets.QHBoxLayout()
        self.baseGroupNameHorBox.setObjectName("baseGroupNameHorBox")
        self.baseGroupNameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.baseGroupNameLabel.setObjectName("baseGroupNameLabel")
        self.baseGroupNameHorBox.addWidget(self.baseGroupNameLabel)
        self.baseGroupNameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.baseGroupNameLineEdit.setText("")
        self.baseGroupNameLineEdit.setReadOnly(True)
        self.baseGroupNameLineEdit.setObjectName("baseGroupNameLineEdit")
        self.baseGroupNameHorBox.addWidget(self.baseGroupNameLineEdit)
        self.outerVertBox.addLayout(self.baseGroupNameHorBox)
        self.numClonesHorBox = QtWidgets.QHBoxLayout()
        self.numClonesHorBox.setObjectName("numClonesHorBox")
        self.numClonesLabel = QtWidgets.QLabel(self.layoutWidget)
        self.numClonesLabel.setObjectName("numClonesLabel")
        self.numClonesHorBox.addWidget(self.numClonesLabel)
        self.numClonesEntry = QtWidgets.QSpinBox()
        self.numClonesEntry.setRange(1, 50)
        self.numClonesEntry.setValue(1)
        self.numClonesHorBox.addWidget(self.numClonesEntry)
        self.outerVertBox.addLayout(self.numClonesHorBox)
        self.linkedClonesHorBox = QtWidgets.QHBoxLayout()
        self.linkedClonesHorBox.setObjectName("linkedClonesHorBox")
        self.linkedClonesLabel = QtWidgets.QLabel(self.layoutWidget)
        self.linkedClonesLabel.setObjectName("linkedClonesLabel")
        self.linkedClonesHorBox.addWidget(self.linkedClonesLabel)
        self.linkedClonesComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.linkedClonesComboBox.setObjectName("linkedClonesComboBox")
        self.linkedClonesComboBox.addItem("")
        self.linkedClonesComboBox.addItem("")
        self.linkedClonesHorBox.addWidget(self.linkedClonesComboBox)
        self.outerVertBox.addLayout(self.linkedClonesHorBox)
        self.cloneSnapshotsHorBox = QtWidgets.QHBoxLayout()
        self.cloneSnapshotsHorBox.setObjectName("cloneSnapshotsHorBox")
        self.cloneSnapshotsLabel = QtWidgets.QLabel(self.layoutWidget)
        self.cloneSnapshotsLabel.setObjectName("cloneSnapshotsLabel")
        self.cloneSnapshotsHorBox.addWidget(self.cloneSnapshotsLabel)
        self.cloneSnapshotComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.cloneSnapshotComboBox.setObjectName("cloneSnapshotComboBox")
        self.cloneSnapshotComboBox.addItem("")
        self.cloneSnapshotComboBox.addItem("")
        self.cloneSnapshotsHorBox.addWidget(self.cloneSnapshotComboBox)
        self.outerVertBox.addLayout(self.cloneSnapshotsHorBox)
        self.baseOutnameHorBox = QtWidgets.QHBoxLayout()
        self.baseOutnameHorBox.setObjectName("baseOutnameHorBox")
        self.baseOutnameLabel = QtWidgets.QLabel(self.layoutWidget)
        self.baseOutnameLabel.setObjectName("baseOutnameLabel")
        self.baseOutnameHorBox.addWidget(self.baseOutnameLabel)
        self.baseOutnameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.baseOutnameLineEdit.setObjectName("baseOutnameLineEdit")
        self.baseOutnameHorBox.addWidget(self.baseOutnameLineEdit)
        self.outerVertBox.addLayout(self.baseOutnameHorBox)
        self.vrdpBaseportHorBox = QtWidgets.QHBoxLayout()
        self.vrdpBaseportHorBox.setObjectName("vrdpBaseportHorBox")
        self.vrdpBaseportLabel = QtWidgets.QLabel(self.layoutWidget)
        self.vrdpBaseportLabel.setObjectName("vrdpBaseportLabel")
        self.vrdpBaseportHorBox.addWidget(self.vrdpBaseportLabel)
        self.vrdpBaseportLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.vrdpBaseportLineEdit.setObjectName("vrdpBaseportLineEdit")
        self.vrdpBaseportHorBox.addWidget(self.vrdpBaseportLineEdit)
        self.outerVertBox.addLayout(self.vrdpBaseportHorBox)
        self.baseAddressHorBox = QtWidgets.QHBoxLayout()
        self.baseAddressHorBox.setObjectName("baseAddressHorBox")
        self.baseAddressLabel = QtWidgets.QLabel(self.layoutWidget)
        self.baseAddressLabel.setObjectName("baseAddressLabel")
        self.baseAddressHorBox.addWidget(self.baseAddressLabel)
        self.baseAddressLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.baseAddressLineEdit.setObjectName("baseAddressLineEdit")
        self.baseAddressHorBox.addWidget(self.baseAddressLineEdit)
        self.outerVertBox.addLayout(self.baseAddressHorBox)
        self.paddingWidget1 = QtWidgets.QWidget(self.layoutWidget)
        self.paddingWidget1.setObjectName("paddingWidget1")
        self.outerVertBox.addWidget(self.paddingWidget1)
        self.paddingWidget2 = QtWidgets.QWidget(self.layoutWidget)
        self.paddingWidget2.setObjectName("paddingWidget2")
        self.outerVertBox.addWidget(self.paddingWidget2)
        self.paddingWidget3 = QtWidgets.QWidget(self.layoutWidget)
        self.paddingWidget3.setObjectName("paddingWidget3")
        self.outerVertBox.addWidget(self.paddingWidget3)
        self.saveButton = QtWidgets.QPushButton(self.layoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.outerVertBox.addWidget(self.saveButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.vBoxManageLabel.setText(_translate("Form", "Path to VBox Manager:"))
        self.chooseVBoxPathButton.setText(_translate("Form", "..."))
        self.ipAddressLabel.setText(_translate("Form", "IP Address:"))
        self.baseGroupNameLabel.setText(_translate("Form", "Base Group Name:"))
        self.numClonesLabel.setText(_translate("Form", "Number of Clones:")
        self.linkedClonesLabel.setText(_translate("Form", "Linked Clones:"))
        self.linkedClonesComboBox.setItemText(0, _translate("Form", "True"))
        self.linkedClonesComboBox.setItemText(1, _translate("Form", "False"))
        self.cloneSnapshotsLabel.setText(_translate("Form", "Clone Snapshots:"))
        self.cloneSnapshotComboBox.setItemText(0, _translate("Form", "True"))
        self.cloneSnapshotComboBox.setItemText(1, _translate("Form", "False"))
        self.baseOutnameLabel.setText(_translate("Form", "Base Outname:"))
        self.baseOutnameLineEdit.setText(_translate("Form", "101"))
        self.vrdpBaseportLabel.setText(_translate("Form", "VRDP Baseport:"))
        self.vrdpBaseportLineEdit.setText(_translate("Form", "1011"))
        self.baseAddressLabel.setText(_translate("Form", "Base Address:"))
        self.baseAddressLineEdit.setText(_translate("Form", "128"))
        self.saveButton.setText(_translate("Form", "Save Changes"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = BaseWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
