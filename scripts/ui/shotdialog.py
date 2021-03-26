# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shot_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ShotDialog(object):
    def setupUi(self, ShotDialog):
        if not ShotDialog.objectName():
            ShotDialog.setObjectName(u"ShotDialog")
        ShotDialog.resize(220, 120)
        ShotDialog.setMinimumSize(QSize(220, 120))
        ShotDialog.setMaximumSize(QSize(220, 120))
        font = QFont()
        font.setFamily(u"Segoe UI")
        ShotDialog.setFont(font)
        ShotDialog.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout = QVBoxLayout(ShotDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ShotDialog)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.spinSequence = QSpinBox(self.widget)
        self.spinSequence.setObjectName(u"spinSequence")
        self.spinSequence.setMaximumSize(QSize(50, 16777215))
        self.spinSequence.setMinimum(1)
        self.spinSequence.setMaximum(500)
        self.spinSequence.setValue(1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinSequence)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.spinShot = QSpinBox(self.widget)
        self.spinShot.setObjectName(u"spinShot")
        self.spinShot.setMaximumSize(QSize(50, 16777215))
        self.spinShot.setMinimum(1)
        self.spinShot.setMaximum(500)
        self.spinShot.setValue(1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinShot)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(ShotDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ShotDialog)
        self.buttonBox.accepted.connect(ShotDialog.accept)
        self.buttonBox.rejected.connect(ShotDialog.reject)

        QMetaObject.connectSlotsByName(ShotDialog)
    # setupUi

    def retranslateUi(self, ShotDialog):
        ShotDialog.setWindowTitle(QCoreApplication.translate("ShotDialog", u"New Shot", None))
        self.label.setText(QCoreApplication.translate("ShotDialog", u"Sequence number:", None))
        self.label_2.setText(QCoreApplication.translate("ShotDialog", u"Shot number:", None))
    # retranslateUi

