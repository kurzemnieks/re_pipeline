# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_manager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(363, 617)
        font = QFont()
        font.setFamily(u"Segoe UI")
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setStyleSheet(u"background-color: rgb(53, 53, 53);\n"
"color: rgb(220, 220, 220);")
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.setRootButton = QPushButton(self.centralwidget)
        self.setRootButton.setObjectName(u"setRootButton")
        self.setRootButton.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.setRootButton)

        self.projectRootLabel = QLabel(self.centralwidget)
        self.projectRootLabel.setObjectName(u"projectRootLabel")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.projectRootLabel.setFont(font1)

        self.horizontalLayout.addWidget(self.projectRootLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.mainTabs = QTabWidget(self.centralwidget)
        self.mainTabs.setObjectName(u"mainTabs")
        self.mainTabs.setStyleSheet(u"")
        self.tab_Assets = QWidget()
        self.tab_Assets.setObjectName(u"tab_Assets")
        self.verticalLayout = QVBoxLayout(self.tab_Assets)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.assetList = QListWidget(self.tab_Assets)
        self.assetList.setObjectName(u"assetList")
        self.assetList.setStyleSheet(u"background-color: rgb(80, 80, 80);")

        self.verticalLayout.addWidget(self.assetList)

        self.assetButtonsWidget = QWidget(self.tab_Assets)
        self.assetButtonsWidget.setObjectName(u"assetButtonsWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.assetButtonsWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.newAssetButton = QPushButton(self.assetButtonsWidget)
        self.newAssetButton.setObjectName(u"newAssetButton")
        self.newAssetButton.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_2.addWidget(self.newAssetButton)

        self.updateAssetButton = QPushButton(self.assetButtonsWidget)
        self.updateAssetButton.setObjectName(u"updateAssetButton")
        self.updateAssetButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.updateAssetButton)

        self.loadAssetButton = QPushButton(self.assetButtonsWidget)
        self.loadAssetButton.setObjectName(u"loadAssetButton")
        self.loadAssetButton.setEnabled(False)
        self.loadAssetButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_2.addWidget(self.loadAssetButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.assetButtonsWidget)

        self.mainTabs.addTab(self.tab_Assets, "")
        self.tab_Shots = QWidget()
        self.tab_Shots.setObjectName(u"tab_Shots")
        self.verticalLayout_3 = QVBoxLayout(self.tab_Shots)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.shotsList = QListWidget(self.tab_Shots)
        self.shotsList.setObjectName(u"shotsList")
        self.shotsList.setStyleSheet(u"background-color: rgb(80, 80, 80);")

        self.verticalLayout_3.addWidget(self.shotsList)

        self.assetButtonsWidget_2 = QWidget(self.tab_Shots)
        self.assetButtonsWidget_2.setObjectName(u"assetButtonsWidget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.assetButtonsWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.newShotButton = QPushButton(self.assetButtonsWidget_2)
        self.newShotButton.setObjectName(u"newShotButton")
        self.newShotButton.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.newShotButton)

        self.updateShotButton = QPushButton(self.assetButtonsWidget_2)
        self.updateShotButton.setObjectName(u"updateShotButton")
        self.updateShotButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.updateShotButton)

        self.loadShotButton = QPushButton(self.assetButtonsWidget_2)
        self.loadShotButton.setObjectName(u"loadShotButton")
        self.loadShotButton.setEnabled(False)
        self.loadShotButton.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.loadShotButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.assetButtonsWidget_2)

        self.mainTabs.addTab(self.tab_Shots, "")
        self.tab_Project = QWidget()
        self.tab_Project.setObjectName(u"tab_Project")
        self.verticalLayout_4 = QVBoxLayout(self.tab_Project)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.tab_Project)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.labelResolution = QLabel(self.groupBox_2)
        self.labelResolution.setObjectName(u"labelResolution")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelResolution)

        self.editHRes = QLineEdit(self.groupBox_2)
        self.editHRes.setObjectName(u"editHRes")
        self.editHRes.setMaximumSize(QSize(45, 16777215))
        self.editHRes.setMaxLength(5)
        self.editHRes.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.editHRes)

        self.editVRes = QLineEdit(self.groupBox_2)
        self.editVRes.setObjectName(u"editVRes")
        self.editVRes.setMaximumSize(QSize(45, 16777215))
        self.editVRes.setMaxLength(5)
        self.editVRes.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.editVRes)

        self.labelFps = QLabel(self.groupBox_2)
        self.labelFps.setObjectName(u"labelFps")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelFps)

        self.editFPS = QLineEdit(self.groupBox_2)
        self.editFPS.setObjectName(u"editFPS")
        self.editFPS.setMaximumSize(QSize(45, 16777215))
        self.editFPS.setMaxLength(6)
        self.editFPS.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.editFPS)

        self.labelExtTexPath = QLabel(self.groupBox_2)
        self.labelExtTexPath.setObjectName(u"labelExtTexPath")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        font2.setKerning(True)
        self.labelExtTexPath.setFont(font2)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.labelExtTexPath)

        self.buttonExtTextures = QPushButton(self.groupBox_2)
        self.buttonExtTextures.setObjectName(u"buttonExtTextures")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.buttonExtTextures)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.tab_Project)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkHoudini = QCheckBox(self.groupBox)
        self.checkHoudini.setObjectName(u"checkHoudini")
        self.checkHoudini.setMaximumSize(QSize(70, 16777215))
        self.checkHoudini.setChecked(True)

        self.gridLayout.addWidget(self.checkHoudini, 0, 0, 1, 1)

        self.checkBlender = QCheckBox(self.groupBox)
        self.checkBlender.setObjectName(u"checkBlender")
        self.checkBlender.setChecked(True)

        self.gridLayout.addWidget(self.checkBlender, 0, 1, 1, 1)

        self.checkMaya = QCheckBox(self.groupBox)
        self.checkMaya.setObjectName(u"checkMaya")
        self.checkMaya.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.checkMaya, 1, 0, 1, 1)

        self.checkC4D = QCheckBox(self.groupBox)
        self.checkC4D.setObjectName(u"checkC4D")

        self.gridLayout.addWidget(self.checkC4D, 1, 1, 1, 1)

        self.checkUSD = QCheckBox(self.groupBox)
        self.checkUSD.setObjectName(u"checkUSD")
        self.checkUSD.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.checkUSD, 2, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.tab_Project)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.checkLivePlate = QCheckBox(self.groupBox_3)
        self.checkLivePlate.setObjectName(u"checkLivePlate")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.checkLivePlate)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.widget = QWidget(self.tab_Project)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.archiveProjectButton = QPushButton(self.widget)
        self.archiveProjectButton.setObjectName(u"archiveProjectButton")
        self.archiveProjectButton.setEnabled(False)

        self.verticalLayout_6.addWidget(self.archiveProjectButton)

        self.cleanProjectButton = QPushButton(self.widget)
        self.cleanProjectButton.setObjectName(u"cleanProjectButton")
        self.cleanProjectButton.setEnabled(False)

        self.verticalLayout_6.addWidget(self.cleanProjectButton)

        self.updateProjectButton = QPushButton(self.widget)
        self.updateProjectButton.setObjectName(u"updateProjectButton")

        self.verticalLayout_6.addWidget(self.updateProjectButton)

        self.newProjectButton = QPushButton(self.widget)
        self.newProjectButton.setObjectName(u"newProjectButton")

        self.verticalLayout_6.addWidget(self.newProjectButton)


        self.verticalLayout_4.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.mainTabs.addTab(self.tab_Project, "")
        self.tab_Apps = QWidget()
        self.tab_Apps.setObjectName(u"tab_Apps")
        self.formLayout_3 = QFormLayout(self.tab_Apps)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.setHoudiniButton = QPushButton(self.tab_Apps)
        self.setHoudiniButton.setObjectName(u"setHoudiniButton")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.setHoudiniButton)

        self.editHoudiniPath = QLineEdit(self.tab_Apps)
        self.editHoudiniPath.setObjectName(u"editHoudiniPath")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.editHoudiniPath)

        self.setBlenderButton = QPushButton(self.tab_Apps)
        self.setBlenderButton.setObjectName(u"setBlenderButton")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.setBlenderButton)

        self.editBlenderPath = QLineEdit(self.tab_Apps)
        self.editBlenderPath.setObjectName(u"editBlenderPath")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.editBlenderPath)

        self.setC4DButton = QPushButton(self.tab_Apps)
        self.setC4DButton.setObjectName(u"setC4DButton")
        self.setC4DButton.setEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.setC4DButton)

        self.setMayaButton = QPushButton(self.tab_Apps)
        self.setMayaButton.setObjectName(u"setMayaButton")
        self.setMayaButton.setEnabled(False)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.setMayaButton)

        self.editC4DPath = QLineEdit(self.tab_Apps)
        self.editC4DPath.setObjectName(u"editC4DPath")
        self.editC4DPath.setEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.editC4DPath)

        self.editMayaPath = QLineEdit(self.tab_Apps)
        self.editMayaPath.setObjectName(u"editMayaPath")
        self.editMayaPath.setEnabled(False)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.editMayaPath)

        self.mainTabs.addTab(self.tab_Apps, "")

        self.verticalLayout_2.addWidget(self.mainTabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.setRootButton, self.mainTabs)
        QWidget.setTabOrder(self.mainTabs, self.newAssetButton)
        QWidget.setTabOrder(self.newAssetButton, self.updateAssetButton)
        QWidget.setTabOrder(self.updateAssetButton, self.loadAssetButton)
        QWidget.setTabOrder(self.loadAssetButton, self.newShotButton)
        QWidget.setTabOrder(self.newShotButton, self.updateShotButton)
        QWidget.setTabOrder(self.updateShotButton, self.loadShotButton)
        QWidget.setTabOrder(self.loadShotButton, self.editHRes)
        QWidget.setTabOrder(self.editHRes, self.editVRes)
        QWidget.setTabOrder(self.editVRes, self.editFPS)
        QWidget.setTabOrder(self.editFPS, self.checkHoudini)
        QWidget.setTabOrder(self.checkHoudini, self.checkBlender)
        QWidget.setTabOrder(self.checkBlender, self.checkMaya)
        QWidget.setTabOrder(self.checkMaya, self.checkC4D)
        QWidget.setTabOrder(self.checkC4D, self.checkUSD)
        QWidget.setTabOrder(self.checkUSD, self.checkLivePlate)
        QWidget.setTabOrder(self.checkLivePlate, self.archiveProjectButton)
        QWidget.setTabOrder(self.archiveProjectButton, self.cleanProjectButton)
        QWidget.setTabOrder(self.cleanProjectButton, self.updateProjectButton)

        self.retranslateUi(MainWindow)

        self.mainTabs.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Project Manager", None))
        self.setRootButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.projectRootLabel.setText(QCoreApplication.translate("MainWindow", u"C:/Projects/ProjectRoot", None))
        self.newAssetButton.setText(QCoreApplication.translate("MainWindow", u"Create New Asset", None))
        self.updateAssetButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.loadAssetButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Assets), QCoreApplication.translate("MainWindow", u"Assets", None))
        self.newShotButton.setText(QCoreApplication.translate("MainWindow", u"Create New Shot", None))
        self.updateShotButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.loadShotButton.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Shots), QCoreApplication.translate("MainWindow", u"Shots", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Defaults", None))
        self.labelResolution.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.editHRes.setInputMask("")
        self.editHRes.setText(QCoreApplication.translate("MainWindow", u"1920", None))
        self.editVRes.setInputMask("")
        self.editVRes.setText(QCoreApplication.translate("MainWindow", u"1080", None))
        self.labelFps.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.editFPS.setInputMask("")
        self.editFPS.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.labelExtTexPath.setText(QCoreApplication.translate("MainWindow", u"C:/Drive/Assets/Textures", None))
        self.buttonExtTextures.setText(QCoreApplication.translate("MainWindow", u"External Texture Lib", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Used Applications", None))
        self.checkHoudini.setText(QCoreApplication.translate("MainWindow", u"Houdini", None))
        self.checkBlender.setText(QCoreApplication.translate("MainWindow", u"Blender", None))
        self.checkMaya.setText(QCoreApplication.translate("MainWindow", u"Maya", None))
        self.checkC4D.setText(QCoreApplication.translate("MainWindow", u"Cinema 4D", None))
        self.checkUSD.setText(QCoreApplication.translate("MainWindow", u"USD", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Additional settings", None))
#if QT_CONFIG(tooltip)
        self.checkLivePlate.setToolTip(QCoreApplication.translate("MainWindow", u"Generate folders for footage, roto, tracking", None))
#endif // QT_CONFIG(tooltip)
        self.checkLivePlate.setText(QCoreApplication.translate("MainWindow", u"Live plate compositing", None))
        self.archiveProjectButton.setText(QCoreApplication.translate("MainWindow", u"Archive Current Project", None))
        self.cleanProjectButton.setText(QCoreApplication.translate("MainWindow", u"Clean Current Project", None))
        self.updateProjectButton.setText(QCoreApplication.translate("MainWindow", u"Update Current Project", None))
        self.newProjectButton.setText(QCoreApplication.translate("MainWindow", u"Create New Project", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Project), QCoreApplication.translate("MainWindow", u"Project", None))
        self.setHoudiniButton.setText(QCoreApplication.translate("MainWindow", u"Set Houdini", None))
        self.setBlenderButton.setText(QCoreApplication.translate("MainWindow", u"Set Blender", None))
        self.setC4DButton.setText(QCoreApplication.translate("MainWindow", u"Set C4D", None))
        self.setMayaButton.setText(QCoreApplication.translate("MainWindow", u"Set Maya", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Apps), QCoreApplication.translate("MainWindow", u"App Config", None))
    # retranslateUi

