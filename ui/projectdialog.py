# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_dialog.ui',
# licensing of 'project_dialog.ui' applies.
#
# Created: Sun Jan  3 21:01:59 2021
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1528389443
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ProjectDialog(object):
    def setupUi(self, ProjectDialog):
        ProjectDialog.setObjectName("ProjectDialog")
        ProjectDialog.resize(400, 120)
        ProjectDialog.setMinimumSize(QtCore.QSize(400, 120))
        ProjectDialog.setMaximumSize(QtCore.QSize(400, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        ProjectDialog.setFont(font)
        ProjectDialog.setStyleSheet("background-color: rgb(53, 53, 53);\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout = QtWidgets.QVBoxLayout(ProjectDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(ProjectDialog)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.editProjectName = QtWidgets.QLineEdit(self.widget)
        self.editProjectName.setObjectName("editProjectName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editProjectName)
        self.browseButton = QtWidgets.QPushButton(self.widget)
        self.browseButton.setObjectName("browseButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.browseButton)
        self.labelProjectRoot = QtWidgets.QLabel(self.widget)
        self.labelProjectRoot.setObjectName("labelProjectRoot")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelProjectRoot)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProjectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProjectDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ProjectDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ProjectDialog)

    def retranslateUi(self, ProjectDialog):
        ProjectDialog.setWindowTitle(QtWidgets.QApplication.translate("ProjectDialog", "Create New Project", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ProjectDialog", "Project name:", None, -1))
        self.browseButton.setText(QtWidgets.QApplication.translate("ProjectDialog", "Set Location", None, -1))
        self.labelProjectRoot.setText(QtWidgets.QApplication.translate("ProjectDialog", "F:/Projects/", None, -1))

