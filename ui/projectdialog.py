# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ProjectDialog(object):
    def setupUi(self, ProjectDialog):
        if not ProjectDialog.objectName():
            ProjectDialog.setObjectName(u"ProjectDialog")
        ProjectDialog.resize(400, 120)
        ProjectDialog.setMinimumSize(QSize(400, 120))
        ProjectDialog.setMaximumSize(QSize(400, 120))
        font = QFont()
        font.setFamily(u"Segoe UI")
        ProjectDialog.setFont(font)
        ProjectDialog.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout = QVBoxLayout(ProjectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ProjectDialog)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.editProjectName = QLineEdit(self.widget)
        self.editProjectName.setObjectName(u"editProjectName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editProjectName)

        self.browseButton = QPushButton(self.widget)
        self.browseButton.setObjectName(u"browseButton")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.browseButton)

        self.labelProjectRoot = QLabel(self.widget)
        self.labelProjectRoot.setObjectName(u"labelProjectRoot")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.labelProjectRoot)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(ProjectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ProjectDialog)
        self.buttonBox.accepted.connect(ProjectDialog.accept)
        self.buttonBox.rejected.connect(ProjectDialog.reject)

        QMetaObject.connectSlotsByName(ProjectDialog)
    # setupUi

    def retranslateUi(self, ProjectDialog):
        ProjectDialog.setWindowTitle(QCoreApplication.translate("ProjectDialog", u"Create New Project", None))
        self.label_2.setText(QCoreApplication.translate("ProjectDialog", u"Project name:", None))
        self.browseButton.setText(QCoreApplication.translate("ProjectDialog", u"Set Location", None))
        self.labelProjectRoot.setText(QCoreApplication.translate("ProjectDialog", u"F:/Projects/", None))
    # retranslateUi

