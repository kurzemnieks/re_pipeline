# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asset_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AssetDialog(object):
    def setupUi(self, AssetDialog):
        if not AssetDialog.objectName():
            AssetDialog.setObjectName(u"AssetDialog")
        AssetDialog.resize(300, 120)
        AssetDialog.setMinimumSize(QSize(300, 120))
        AssetDialog.setMaximumSize(QSize(300, 120))
        font = QFont()
        font.setFamily(u"Segoe UI")
        AssetDialog.setFont(font)
        AssetDialog.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"color: rgb(220, 220, 220);")
        self.verticalLayout = QVBoxLayout(AssetDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(AssetDialog)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.editAssetName = QLineEdit(self.widget)
        self.editAssetName.setObjectName(u"editAssetName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editAssetName)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(AssetDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AssetDialog)
        self.buttonBox.accepted.connect(AssetDialog.accept)
        self.buttonBox.rejected.connect(AssetDialog.reject)

        QMetaObject.connectSlotsByName(AssetDialog)
    # setupUi

    def retranslateUi(self, AssetDialog):
        AssetDialog.setWindowTitle(QCoreApplication.translate("AssetDialog", u"New Asset", None))
        self.label_2.setText(QCoreApplication.translate("AssetDialog", u"Asset name:", None))
    # retranslateUi

