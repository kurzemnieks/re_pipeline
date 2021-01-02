# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_manager.ui',
# licensing of 'project_manager.ui' applies.
#
# Created: Sat Jan  2 19:51:19 2021
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1528389443
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(363, 617)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(53, 53, 53);\n"
"color: rgb(220, 220, 220);")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setRootButton = QtWidgets.QPushButton(self.centralwidget)
        self.setRootButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.setRootButton.setObjectName("setRootButton")
        self.horizontalLayout.addWidget(self.setRootButton)
        self.projectRootLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.projectRootLabel.setFont(font)
        self.projectRootLabel.setObjectName("projectRootLabel")
        self.horizontalLayout.addWidget(self.projectRootLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.mainTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabs.setStyleSheet("")
        self.mainTabs.setObjectName("mainTabs")
        self.tab_Assets = QtWidgets.QWidget()
        self.tab_Assets.setObjectName("tab_Assets")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_Assets)
        self.verticalLayout.setObjectName("verticalLayout")
        self.assetList = QtWidgets.QListWidget(self.tab_Assets)
        self.assetList.setStyleSheet("background-color: rgb(80, 80, 80);")
        self.assetList.setObjectName("assetList")
        self.verticalLayout.addWidget(self.assetList)
        self.assetButtonsWidget = QtWidgets.QWidget(self.tab_Assets)
        self.assetButtonsWidget.setObjectName("assetButtonsWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.assetButtonsWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newAssetButton = QtWidgets.QPushButton(self.assetButtonsWidget)
        self.newAssetButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.newAssetButton.setObjectName("newAssetButton")
        self.horizontalLayout_2.addWidget(self.newAssetButton)
        self.updateAssetButton = QtWidgets.QPushButton(self.assetButtonsWidget)
        self.updateAssetButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.updateAssetButton.setObjectName("updateAssetButton")
        self.horizontalLayout_2.addWidget(self.updateAssetButton)
        self.loadAssetButton = QtWidgets.QPushButton(self.assetButtonsWidget)
        self.loadAssetButton.setEnabled(False)
        self.loadAssetButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.loadAssetButton.setObjectName("loadAssetButton")
        self.horizontalLayout_2.addWidget(self.loadAssetButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.assetButtonsWidget)
        self.mainTabs.addTab(self.tab_Assets, "")
        self.tab_Shots = QtWidgets.QWidget()
        self.tab_Shots.setObjectName("tab_Shots")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_Shots)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.shotsList = QtWidgets.QListWidget(self.tab_Shots)
        self.shotsList.setStyleSheet("background-color: rgb(80, 80, 80);")
        self.shotsList.setObjectName("shotsList")
        self.verticalLayout_3.addWidget(self.shotsList)
        self.assetButtonsWidget_2 = QtWidgets.QWidget(self.tab_Shots)
        self.assetButtonsWidget_2.setObjectName("assetButtonsWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.assetButtonsWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.newShotButton = QtWidgets.QPushButton(self.assetButtonsWidget_2)
        self.newShotButton.setMaximumSize(QtCore.QSize(120, 16777215))
        self.newShotButton.setObjectName("newShotButton")
        self.horizontalLayout_3.addWidget(self.newShotButton)
        self.updateShotButton = QtWidgets.QPushButton(self.assetButtonsWidget_2)
        self.updateShotButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.updateShotButton.setObjectName("updateShotButton")
        self.horizontalLayout_3.addWidget(self.updateShotButton)
        self.loadShotButton = QtWidgets.QPushButton(self.assetButtonsWidget_2)
        self.loadShotButton.setEnabled(False)
        self.loadShotButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.loadShotButton.setObjectName("loadShotButton")
        self.horizontalLayout_3.addWidget(self.loadShotButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.assetButtonsWidget_2)
        self.mainTabs.addTab(self.tab_Shots, "")
        self.tab_Project = QtWidgets.QWidget()
        self.tab_Project.setObjectName("tab_Project")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_Project)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_Project)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.labelResolution = QtWidgets.QLabel(self.groupBox_2)
        self.labelResolution.setObjectName("labelResolution")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelResolution)
        self.editHRes = QtWidgets.QLineEdit(self.groupBox_2)
        self.editHRes.setMaximumSize(QtCore.QSize(45, 16777215))
        self.editHRes.setInputMask("")
        self.editHRes.setMaxLength(5)
        self.editHRes.setAlignment(QtCore.Qt.AlignCenter)
        self.editHRes.setObjectName("editHRes")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editHRes)
        self.editVRes = QtWidgets.QLineEdit(self.groupBox_2)
        self.editVRes.setMaximumSize(QtCore.QSize(45, 16777215))
        self.editVRes.setInputMask("")
        self.editVRes.setMaxLength(5)
        self.editVRes.setAlignment(QtCore.Qt.AlignCenter)
        self.editVRes.setObjectName("editVRes")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editVRes)
        self.labelFps = QtWidgets.QLabel(self.groupBox_2)
        self.labelFps.setObjectName("labelFps")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelFps)
        self.editFPS = QtWidgets.QLineEdit(self.groupBox_2)
        self.editFPS.setMaximumSize(QtCore.QSize(45, 16777215))
        self.editFPS.setInputMask("")
        self.editFPS.setMaxLength(6)
        self.editFPS.setAlignment(QtCore.Qt.AlignCenter)
        self.editFPS.setObjectName("editFPS")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.editFPS)
        self.labelExtTexPath = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelExtTexPath.setFont(font)
        self.labelExtTexPath.setObjectName("labelExtTexPath")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.labelExtTexPath)
        self.buttonExtTextures = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonExtTextures.setObjectName("buttonExtTextures")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.buttonExtTextures)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab_Project)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.checkHoudini = QtWidgets.QCheckBox(self.groupBox)
        self.checkHoudini.setMaximumSize(QtCore.QSize(70, 16777215))
        self.checkHoudini.setChecked(True)
        self.checkHoudini.setObjectName("checkHoudini")
        self.gridLayout.addWidget(self.checkHoudini, 0, 0, 1, 1)
        self.checkBlender = QtWidgets.QCheckBox(self.groupBox)
        self.checkBlender.setChecked(True)
        self.checkBlender.setObjectName("checkBlender")
        self.gridLayout.addWidget(self.checkBlender, 0, 1, 1, 1)
        self.checkMaya = QtWidgets.QCheckBox(self.groupBox)
        self.checkMaya.setMaximumSize(QtCore.QSize(70, 16777215))
        self.checkMaya.setObjectName("checkMaya")
        self.gridLayout.addWidget(self.checkMaya, 1, 0, 1, 1)
        self.checkC4D = QtWidgets.QCheckBox(self.groupBox)
        self.checkC4D.setObjectName("checkC4D")
        self.gridLayout.addWidget(self.checkC4D, 1, 1, 1, 1)
        self.checkUSD = QtWidgets.QCheckBox(self.groupBox)
        self.checkUSD.setMaximumSize(QtCore.QSize(70, 16777215))
        self.checkUSD.setObjectName("checkUSD")
        self.gridLayout.addWidget(self.checkUSD, 2, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_Project)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.checkLivePlate = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkLivePlate.setObjectName("checkLivePlate")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkLivePlate)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.widget = QtWidgets.QWidget(self.tab_Project)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.archiveProjectButton = QtWidgets.QPushButton(self.widget)
        self.archiveProjectButton.setEnabled(False)
        self.archiveProjectButton.setObjectName("archiveProjectButton")
        self.verticalLayout_6.addWidget(self.archiveProjectButton)
        self.cleanProjectButton = QtWidgets.QPushButton(self.widget)
        self.cleanProjectButton.setEnabled(False)
        self.cleanProjectButton.setObjectName("cleanProjectButton")
        self.verticalLayout_6.addWidget(self.cleanProjectButton)
        self.createProjectButton = QtWidgets.QPushButton(self.widget)
        self.createProjectButton.setObjectName("createProjectButton")
        self.verticalLayout_6.addWidget(self.createProjectButton)
        self.verticalLayout_4.addWidget(self.widget)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.mainTabs.addTab(self.tab_Project, "")
        self.tab_Apps = QtWidgets.QWidget()
        self.tab_Apps.setObjectName("tab_Apps")
        self.formLayout_3 = QtWidgets.QFormLayout(self.tab_Apps)
        self.formLayout_3.setObjectName("formLayout_3")
        self.setHoudiniButton = QtWidgets.QPushButton(self.tab_Apps)
        self.setHoudiniButton.setObjectName("setHoudiniButton")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.setHoudiniButton)
        self.editHoudiniPath = QtWidgets.QLineEdit(self.tab_Apps)
        self.editHoudiniPath.setObjectName("editHoudiniPath")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editHoudiniPath)
        self.setBlenderButton = QtWidgets.QPushButton(self.tab_Apps)
        self.setBlenderButton.setObjectName("setBlenderButton")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.setBlenderButton)
        self.editBlenderPath = QtWidgets.QLineEdit(self.tab_Apps)
        self.editBlenderPath.setObjectName("editBlenderPath")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editBlenderPath)
        self.setC4DButton = QtWidgets.QPushButton(self.tab_Apps)
        self.setC4DButton.setEnabled(False)
        self.setC4DButton.setObjectName("setC4DButton")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.setC4DButton)
        self.setMayaButton = QtWidgets.QPushButton(self.tab_Apps)
        self.setMayaButton.setEnabled(False)
        self.setMayaButton.setObjectName("setMayaButton")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.setMayaButton)
        self.editC4DPath = QtWidgets.QLineEdit(self.tab_Apps)
        self.editC4DPath.setEnabled(False)
        self.editC4DPath.setObjectName("editC4DPath")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.editC4DPath)
        self.editMayaPath = QtWidgets.QLineEdit(self.tab_Apps)
        self.editMayaPath.setEnabled(False)
        self.editMayaPath.setObjectName("editMayaPath")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.editMayaPath)
        self.mainTabs.addTab(self.tab_Apps, "")
        self.verticalLayout_2.addWidget(self.mainTabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.mainTabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.setRootButton, self.mainTabs)
        MainWindow.setTabOrder(self.mainTabs, self.newAssetButton)
        MainWindow.setTabOrder(self.newAssetButton, self.updateAssetButton)
        MainWindow.setTabOrder(self.updateAssetButton, self.loadAssetButton)
        MainWindow.setTabOrder(self.loadAssetButton, self.newShotButton)
        MainWindow.setTabOrder(self.newShotButton, self.updateShotButton)
        MainWindow.setTabOrder(self.updateShotButton, self.loadShotButton)
        MainWindow.setTabOrder(self.loadShotButton, self.editHRes)
        MainWindow.setTabOrder(self.editHRes, self.editVRes)
        MainWindow.setTabOrder(self.editVRes, self.editFPS)
        MainWindow.setTabOrder(self.editFPS, self.checkHoudini)
        MainWindow.setTabOrder(self.checkHoudini, self.checkBlender)
        MainWindow.setTabOrder(self.checkBlender, self.checkMaya)
        MainWindow.setTabOrder(self.checkMaya, self.checkC4D)
        MainWindow.setTabOrder(self.checkC4D, self.checkUSD)
        MainWindow.setTabOrder(self.checkUSD, self.checkLivePlate)
        MainWindow.setTabOrder(self.checkLivePlate, self.archiveProjectButton)
        MainWindow.setTabOrder(self.archiveProjectButton, self.cleanProjectButton)
        MainWindow.setTabOrder(self.cleanProjectButton, self.createProjectButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Project Manager", None, -1))
        self.setRootButton.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.projectRootLabel.setText(QtWidgets.QApplication.translate("MainWindow", "C:/Projects/ProjectRoot", None, -1))
        self.newAssetButton.setText(QtWidgets.QApplication.translate("MainWindow", "Create New Asset", None, -1))
        self.updateAssetButton.setText(QtWidgets.QApplication.translate("MainWindow", "Update", None, -1))
        self.loadAssetButton.setText(QtWidgets.QApplication.translate("MainWindow", "Load", None, -1))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Assets), QtWidgets.QApplication.translate("MainWindow", "Assets", None, -1))
        self.newShotButton.setText(QtWidgets.QApplication.translate("MainWindow", "Create New Shot", None, -1))
        self.updateShotButton.setText(QtWidgets.QApplication.translate("MainWindow", "Update", None, -1))
        self.loadShotButton.setText(QtWidgets.QApplication.translate("MainWindow", "Load", None, -1))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Shots), QtWidgets.QApplication.translate("MainWindow", "Shots", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Defaults", None, -1))
        self.labelResolution.setText(QtWidgets.QApplication.translate("MainWindow", "Resolution", None, -1))
        self.editHRes.setText(QtWidgets.QApplication.translate("MainWindow", "1920", None, -1))
        self.editVRes.setText(QtWidgets.QApplication.translate("MainWindow", "1080", None, -1))
        self.labelFps.setText(QtWidgets.QApplication.translate("MainWindow", "FPS", None, -1))
        self.editFPS.setText(QtWidgets.QApplication.translate("MainWindow", "30", None, -1))
        self.labelExtTexPath.setText(QtWidgets.QApplication.translate("MainWindow", "C:/Drive/Assets/Textures", None, -1))
        self.buttonExtTextures.setText(QtWidgets.QApplication.translate("MainWindow", "External Texture Lib", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Used Applications", None, -1))
        self.checkHoudini.setText(QtWidgets.QApplication.translate("MainWindow", "Houdini", None, -1))
        self.checkBlender.setText(QtWidgets.QApplication.translate("MainWindow", "Blender", None, -1))
        self.checkMaya.setText(QtWidgets.QApplication.translate("MainWindow", "Maya", None, -1))
        self.checkC4D.setText(QtWidgets.QApplication.translate("MainWindow", "Cinema 4D", None, -1))
        self.checkUSD.setText(QtWidgets.QApplication.translate("MainWindow", "USD", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Additional settings", None, -1))
        self.checkLivePlate.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Generate folders for footage, roto, tracking", None, -1))
        self.checkLivePlate.setText(QtWidgets.QApplication.translate("MainWindow", "Live plate compositing", None, -1))
        self.archiveProjectButton.setText(QtWidgets.QApplication.translate("MainWindow", "Archive", None, -1))
        self.cleanProjectButton.setText(QtWidgets.QApplication.translate("MainWindow", "Clean", None, -1))
        self.createProjectButton.setText(QtWidgets.QApplication.translate("MainWindow", "Create / Update", None, -1))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Project), QtWidgets.QApplication.translate("MainWindow", "Project", None, -1))
        self.setHoudiniButton.setText(QtWidgets.QApplication.translate("MainWindow", "Set Houdini", None, -1))
        self.setBlenderButton.setText(QtWidgets.QApplication.translate("MainWindow", "Set Blender", None, -1))
        self.setC4DButton.setText(QtWidgets.QApplication.translate("MainWindow", "Set C4D", None, -1))
        self.setMayaButton.setText(QtWidgets.QApplication.translate("MainWindow", "Set Maya", None, -1))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Apps), QtWidgets.QApplication.translate("MainWindow", "App Config", None, -1))

