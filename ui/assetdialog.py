# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asset_dialog.ui',
# licensing of 'asset_dialog.ui' applies.
#
# Created: Sun Nov 22 00:15:23 2020
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1528389443
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 120)
        Dialog.setMinimumSize(QtCore.QSize(300, 120))
        Dialog.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color: rgb(53, 53, 53);\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.editAssetName = QtWidgets.QLineEdit(self.widget)
        self.editAssetName.setObjectName("editAssetName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editAssetName)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "New Asset", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Asset name:", None, -1))

