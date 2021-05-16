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
        MainWindow.resize(418, 813)
        font = QFont()
        font.setFamily(u"Segoe UI")
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u"icons/re_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.top_stuff = QWidget(self.centralwidget)
        self.top_stuff.setObjectName(u"top_stuff")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.top_stuff.sizePolicy().hasHeightForWidth())
        self.top_stuff.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.top_stuff)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 6)
        self.setRootButton = QPushButton(self.top_stuff)
        self.setRootButton.setObjectName(u"setRootButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.setRootButton.sizePolicy().hasHeightForWidth())
        self.setRootButton.setSizePolicy(sizePolicy2)
        self.setRootButton.setMinimumSize(QSize(80, 0))
        self.setRootButton.setMaximumSize(QSize(120, 16777215))
        icon1 = QIcon()
        icon1.addFile(u"icons/link_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setRootButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.setRootButton)

        self.projectRootLabel = QLabel(self.top_stuff)
        self.projectRootLabel.setObjectName(u"projectRootLabel")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.projectRootLabel.setFont(font1)

        self.horizontalLayout.addWidget(self.projectRootLabel)


        self.verticalLayout_2.addWidget(self.top_stuff)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.mainTabs = QTabWidget(self.centralwidget)
        self.mainTabs.setObjectName(u"mainTabs")
        self.mainTabs.setStyleSheet(u"")
        self.tab_Assets = QWidget()
        self.tab_Assets.setObjectName(u"tab_Assets")
        self.verticalLayout = QVBoxLayout(self.tab_Assets)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.assetLayout = QVBoxLayout()
        self.assetLayout.setObjectName(u"assetLayout")
        self.assetList = QListWidget(self.tab_Assets)
        self.assetList.setObjectName(u"assetList")
        self.assetList.setStyleSheet(u"background-color: rgb(80, 80, 80);")

        self.assetLayout.addWidget(self.assetList)

        self.assetActions = QWidget(self.tab_Assets)
        self.assetActions.setObjectName(u"assetActions")
        self.assetActionLayout = QHBoxLayout(self.assetActions)
        self.assetActionLayout.setObjectName(u"assetActionLayout")
        self.newAssetButton = QPushButton(self.assetActions)
        self.newAssetButton.setObjectName(u"newAssetButton")
        icon2 = QIcon()
        icon2.addFile(u"icons/new_object.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newAssetButton.setIcon(icon2)

        self.assetActionLayout.addWidget(self.newAssetButton)

        self.loadAssetButton = QPushButton(self.assetActions)
        self.loadAssetButton.setObjectName(u"loadAssetButton")
        self.loadAssetButton.setEnabled(True)

        self.assetActionLayout.addWidget(self.loadAssetButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.assetActionLayout.addItem(self.horizontalSpacer)


        self.assetLayout.addWidget(self.assetActions)

        self.assetFileList = QTreeWidget(self.tab_Assets)
        self.assetFileList.setObjectName(u"assetFileList")
        self.assetFileList.setStyleSheet(u"background-color: rgb(80, 80, 80);")

        self.assetLayout.addWidget(self.assetFileList)

        self.assetFileActionGroup = QHBoxLayout()
        self.assetFileActionGroup.setObjectName(u"assetFileActionGroup")
        self.openAssetFileButton = QPushButton(self.tab_Assets)
        self.openAssetFileButton.setObjectName(u"openAssetFileButton")
        self.openAssetFileButton.setIcon(icon1)

        self.assetFileActionGroup.addWidget(self.openAssetFileButton)

        self.newAssetFileButton = QPushButton(self.tab_Assets)
        self.newAssetFileButton.setObjectName(u"newAssetFileButton")
        icon3 = QIcon()
        icon3.addFile(u"icons/new_file_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newAssetFileButton.setIcon(icon3)

        self.assetFileActionGroup.addWidget(self.newAssetFileButton)


        self.assetLayout.addLayout(self.assetFileActionGroup)


        self.verticalLayout.addLayout(self.assetLayout)

        self.mainTabs.addTab(self.tab_Assets, icon2, "")
        self.tab_Shots = QWidget()
        self.tab_Shots.setObjectName(u"tab_Shots")
        self.verticalLayout_3 = QVBoxLayout(self.tab_Shots)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.shotLayout = QVBoxLayout()
        self.shotLayout.setObjectName(u"shotLayout")
        self.shotsList = QListWidget(self.tab_Shots)
        self.shotsList.setObjectName(u"shotsList")
        self.shotsList.setStyleSheet(u"background-color: rgb(80, 80, 80);")

        self.shotLayout.addWidget(self.shotsList)

        self.shotActions = QWidget(self.tab_Shots)
        self.shotActions.setObjectName(u"shotActions")
        self.shotActionLayout = QHBoxLayout(self.shotActions)
        self.shotActionLayout.setObjectName(u"shotActionLayout")
        self.newShotButton = QPushButton(self.shotActions)
        self.newShotButton.setObjectName(u"newShotButton")
        icon4 = QIcon()
        icon4.addFile(u"icons/new_scene_shot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newShotButton.setIcon(icon4)

        self.shotActionLayout.addWidget(self.newShotButton)

        self.loadShotButton = QPushButton(self.shotActions)
        self.loadShotButton.setObjectName(u"loadShotButton")
        self.loadShotButton.setEnabled(True)

        self.shotActionLayout.addWidget(self.loadShotButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.shotActionLayout.addItem(self.horizontalSpacer_2)


        self.shotLayout.addWidget(self.shotActions)

        self.shotFileList = QTreeWidget(self.tab_Shots)
        self.shotFileList.setObjectName(u"shotFileList")
        self.shotFileList.setStyleSheet(u"background-color: rgb(80, 80, 80);")

        self.shotLayout.addWidget(self.shotFileList)

        self.shotFileActionGroup = QHBoxLayout()
        self.shotFileActionGroup.setObjectName(u"shotFileActionGroup")
        self.openShotFileButton = QPushButton(self.tab_Shots)
        self.openShotFileButton.setObjectName(u"openShotFileButton")
        self.openShotFileButton.setIcon(icon1)

        self.shotFileActionGroup.addWidget(self.openShotFileButton)

        self.newShotFileButton = QPushButton(self.tab_Shots)
        self.newShotFileButton.setObjectName(u"newShotFileButton")
        self.newShotFileButton.setIcon(icon3)

        self.shotFileActionGroup.addWidget(self.newShotFileButton)


        self.shotLayout.addLayout(self.shotFileActionGroup)


        self.verticalLayout_3.addLayout(self.shotLayout)

        self.mainTabs.addTab(self.tab_Shots, icon4, "")
        self.tab_Project = QWidget()
        self.tab_Project.setObjectName(u"tab_Project")
        self.verticalLayout_4 = QVBoxLayout(self.tab_Project)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.tab_Project)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.labelResolution = QLabel(self.groupBox_2)
        self.labelResolution.setObjectName(u"labelResolution")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelResolution)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.editHRes = QLineEdit(self.groupBox_2)
        self.editHRes.setObjectName(u"editHRes")
        self.editHRes.setMaximumSize(QSize(45, 16777215))
        self.editHRes.setMaxLength(5)
        self.editHRes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.editHRes)

        self.editVRes = QLineEdit(self.groupBox_2)
        self.editVRes.setObjectName(u"editVRes")
        self.editVRes.setMaximumSize(QSize(45, 16777215))
        self.editVRes.setMaxLength(5)
        self.editVRes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.editVRes)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.labelFps = QLabel(self.groupBox_2)
        self.labelFps.setObjectName(u"labelFps")

        self.horizontalLayout_3.addWidget(self.labelFps)

        self.editFPS = QLineEdit(self.groupBox_2)
        self.editFPS.setObjectName(u"editFPS")
        self.editFPS.setMaximumSize(QSize(45, 16777215))
        self.editFPS.setMaxLength(6)
        self.editFPS.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.editFPS)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.extLibsGroupBox = QGroupBox(self.tab_Project)
        self.extLibsGroupBox.setObjectName(u"extLibsGroupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.extLibsGroupBox.sizePolicy().hasHeightForWidth())
        self.extLibsGroupBox.setSizePolicy(sizePolicy3)
        self.extLibsGroupBox.setMinimumSize(QSize(0, 50))
        self.verticalLayout_5 = QVBoxLayout(self.extLibsGroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.extLibsList = QTreeWidget(self.extLibsGroupBox)
        self.extLibsList.setObjectName(u"extLibsList")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.extLibsList.sizePolicy().hasHeightForWidth())
        self.extLibsList.setSizePolicy(sizePolicy4)
        self.extLibsList.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.extLibsList.setItemsExpandable(False)
        self.extLibsList.setExpandsOnDoubleClick(False)

        self.verticalLayout_5.addWidget(self.extLibsList)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.extLibFolderName = QLineEdit(self.extLibsGroupBox)
        self.extLibFolderName.setObjectName(u"extLibFolderName")
        sizePolicy1.setHeightForWidth(self.extLibFolderName.sizePolicy().hasHeightForWidth())
        self.extLibFolderName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.extLibFolderName)

        self.extLibBaseDropdown = QComboBox(self.extLibsGroupBox)
        self.extLibBaseDropdown.addItem("")
        self.extLibBaseDropdown.addItem("")
        self.extLibBaseDropdown.setObjectName(u"extLibBaseDropdown")

        self.horizontalLayout_2.addWidget(self.extLibBaseDropdown)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.hlayout_20 = QHBoxLayout()
        self.hlayout_20.setObjectName(u"hlayout_20")
        self.extLibTargetPath = QLineEdit(self.extLibsGroupBox)
        self.extLibTargetPath.setObjectName(u"extLibTargetPath")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.extLibTargetPath.sizePolicy().hasHeightForWidth())
        self.extLibTargetPath.setSizePolicy(sizePolicy5)

        self.hlayout_20.addWidget(self.extLibTargetPath)

        self.browseExtLibTargetButton = QPushButton(self.extLibsGroupBox)
        self.browseExtLibTargetButton.setObjectName(u"browseExtLibTargetButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.browseExtLibTargetButton.sizePolicy().hasHeightForWidth())
        self.browseExtLibTargetButton.setSizePolicy(sizePolicy6)

        self.hlayout_20.addWidget(self.browseExtLibTargetButton)


        self.verticalLayout_7.addLayout(self.hlayout_20)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.addNewExtLibButton = QPushButton(self.extLibsGroupBox)
        self.addNewExtLibButton.setObjectName(u"addNewExtLibButton")
        icon5 = QIcon()
        icon5.addFile(u"icons/link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addNewExtLibButton.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.addNewExtLibButton)


        self.verticalLayout_4.addWidget(self.extLibsGroupBox)

        self.groupBox = QGroupBox(self.tab_Project)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkC4D = QCheckBox(self.groupBox)
        self.checkC4D.setObjectName(u"checkC4D")

        self.gridLayout.addWidget(self.checkC4D, 1, 0, 1, 1)

        self.checkMaya = QCheckBox(self.groupBox)
        self.checkMaya.setObjectName(u"checkMaya")
        self.checkMaya.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.checkMaya, 0, 2, 1, 1)

        self.checkHoudini = QCheckBox(self.groupBox)
        self.checkHoudini.setObjectName(u"checkHoudini")
        self.checkHoudini.setMaximumSize(QSize(70, 16777215))
        self.checkHoudini.setChecked(True)

        self.gridLayout.addWidget(self.checkHoudini, 0, 0, 1, 1)

        self.checkBlender = QCheckBox(self.groupBox)
        self.checkBlender.setObjectName(u"checkBlender")
        self.checkBlender.setChecked(True)

        self.gridLayout.addWidget(self.checkBlender, 0, 1, 1, 1)

        self.checkUSD = QCheckBox(self.groupBox)
        self.checkUSD.setObjectName(u"checkUSD")
        self.checkUSD.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.checkUSD, 1, 1, 1, 1)

        self.checkOther = QCheckBox(self.groupBox)
        self.checkOther.setObjectName(u"checkOther")
        self.checkOther.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.checkOther, 1, 2, 1, 1)

        self.checkUnreal = QCheckBox(self.groupBox)
        self.checkUnreal.setObjectName(u"checkUnreal")
        self.checkUnreal.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.checkUnreal, 0, 3, 1, 1)

        self.checkLivePlate = QCheckBox(self.groupBox)
        self.checkLivePlate.setObjectName(u"checkLivePlate")

        self.gridLayout.addWidget(self.checkLivePlate, 1, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.tab_Project)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 10)
        self.setUnrealButton = QPushButton(self.groupBox_4)
        self.setUnrealButton.setObjectName(u"setUnrealButton")
        self.setUnrealButton.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.setUnrealButton)

        self.unrealProjectPathEdit = QLineEdit(self.groupBox_4)
        self.unrealProjectPathEdit.setObjectName(u"unrealProjectPathEdit")
        self.unrealProjectPathEdit.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.unrealProjectPathEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addWidget(self.groupBox_4)

        self.widget = QWidget(self.tab_Project)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.dropProjectButton = QPushButton(self.widget)
        self.dropProjectButton.setObjectName(u"dropProjectButton")
        self.dropProjectButton.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u"icons/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dropProjectButton.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.dropProjectButton)

        self.newProjectButton = QPushButton(self.widget)
        self.newProjectButton.setObjectName(u"newProjectButton")
        icon7 = QIcon()
        icon7.addFile(u"icons/new_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newProjectButton.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.newProjectButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.archiveProjectButton = QPushButton(self.widget)
        self.archiveProjectButton.setObjectName(u"archiveProjectButton")
        self.archiveProjectButton.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.archiveProjectButton.sizePolicy().hasHeightForWidth())
        self.archiveProjectButton.setSizePolicy(sizePolicy6)
        icon8 = QIcon()
        icon8.addFile(u"icons/archive.png", QSize(), QIcon.Normal, QIcon.Off)
        self.archiveProjectButton.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.archiveProjectButton)

        self.updateProjectButton = QPushButton(self.widget)
        self.updateProjectButton.setObjectName(u"updateProjectButton")
        self.updateProjectButton.setEnabled(False)
        icon9 = QIcon()
        icon9.addFile(u"icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateProjectButton.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.updateProjectButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.mainTabs.addTab(self.tab_Project, icon9, "")
        self.tab_Apps = QWidget()
        self.tab_Apps.setObjectName(u"tab_Apps")
        self.verticalLayout_20 = QVBoxLayout(self.tab_Apps)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.setHoudiniButton = QPushButton(self.tab_Apps)
        self.setHoudiniButton.setObjectName(u"setHoudiniButton")

        self.horizontalLayout_4.addWidget(self.setHoudiniButton)

        self.houdiniPathEdit = QLineEdit(self.tab_Apps)
        self.houdiniPathEdit.setObjectName(u"houdiniPathEdit")
        self.houdiniPathEdit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.houdiniPathEdit)

        self.runHoudiniButton = QPushButton(self.tab_Apps)
        self.runHoudiniButton.setObjectName(u"runHoudiniButton")
        self.runHoudiniButton.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u"icons/baseline_play_circle_filled_white_18.png", QSize(), QIcon.Normal, QIcon.Off)
        self.runHoudiniButton.setIcon(icon10)

        self.horizontalLayout_4.addWidget(self.runHoudiniButton)


        self.verticalLayout_20.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.setBlenderButton = QPushButton(self.tab_Apps)
        self.setBlenderButton.setObjectName(u"setBlenderButton")

        self.horizontalLayout_21.addWidget(self.setBlenderButton)

        self.blenderPathEdit = QLineEdit(self.tab_Apps)
        self.blenderPathEdit.setObjectName(u"blenderPathEdit")
        self.blenderPathEdit.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.blenderPathEdit)

        self.runBlenderButton = QPushButton(self.tab_Apps)
        self.runBlenderButton.setObjectName(u"runBlenderButton")
        self.runBlenderButton.setFont(font1)
        self.runBlenderButton.setIcon(icon10)

        self.horizontalLayout_21.addWidget(self.runBlenderButton)


        self.verticalLayout_20.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.setBlenderButton_2 = QPushButton(self.tab_Apps)
        self.setBlenderButton_2.setObjectName(u"setBlenderButton_2")
        self.setBlenderButton_2.setEnabled(False)

        self.horizontalLayout_22.addWidget(self.setBlenderButton_2)

        self.blenderPathEdit_2 = QLineEdit(self.tab_Apps)
        self.blenderPathEdit_2.setObjectName(u"blenderPathEdit_2")
        self.blenderPathEdit_2.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.blenderPathEdit_2)

        self.runMayaButton = QPushButton(self.tab_Apps)
        self.runMayaButton.setObjectName(u"runMayaButton")
        self.runMayaButton.setEnabled(False)
        self.runMayaButton.setFont(font1)
        self.runMayaButton.setIcon(icon10)

        self.horizontalLayout_22.addWidget(self.runMayaButton)


        self.verticalLayout_20.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.setBlenderButton_3 = QPushButton(self.tab_Apps)
        self.setBlenderButton_3.setObjectName(u"setBlenderButton_3")
        self.setBlenderButton_3.setEnabled(False)

        self.horizontalLayout_23.addWidget(self.setBlenderButton_3)

        self.blenderPathEdit_3 = QLineEdit(self.tab_Apps)
        self.blenderPathEdit_3.setObjectName(u"blenderPathEdit_3")
        self.blenderPathEdit_3.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.blenderPathEdit_3)

        self.runC4DButton = QPushButton(self.tab_Apps)
        self.runC4DButton.setObjectName(u"runC4DButton")
        self.runC4DButton.setFont(font1)
        self.runC4DButton.setIcon(icon10)

        self.horizontalLayout_23.addWidget(self.runC4DButton)


        self.verticalLayout_20.addLayout(self.horizontalLayout_23)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_3)

        self.mainTabs.addTab(self.tab_Apps, icon10, "")

        self.verticalLayout_2.addWidget(self.mainTabs)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.setRootButton, self.mainTabs)
        QWidget.setTabOrder(self.mainTabs, self.newAssetButton)
        QWidget.setTabOrder(self.newAssetButton, self.loadAssetButton)
        QWidget.setTabOrder(self.loadAssetButton, self.newShotButton)
        QWidget.setTabOrder(self.newShotButton, self.loadShotButton)

        self.retranslateUi(MainWindow)
        self.checkUnreal.toggled.connect(self.unrealProjectPathEdit.setEnabled)
        self.checkUnreal.toggled.connect(self.setUnrealButton.setEnabled)
        self.dropProjectButton.clicked.connect(self.unrealProjectPathEdit.clear)

        self.mainTabs.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Project Manager", None))
        self.setRootButton.setText(QCoreApplication.translate("MainWindow", u"Set Project", None))
        self.projectRootLabel.setText(QCoreApplication.translate("MainWindow", u"C:/Projects/ProjectRoot", None))
        self.newAssetButton.setText(QCoreApplication.translate("MainWindow", u"Create New Asset", None))
        self.loadAssetButton.setText(QCoreApplication.translate("MainWindow", u"Set Active", None))
        ___qtreewidgetitem = self.assetFileList.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Last Modified", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"File Name", None));
        self.openAssetFileButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.newAssetFileButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Assets), QCoreApplication.translate("MainWindow", u"Assets", None))
        self.newShotButton.setText(QCoreApplication.translate("MainWindow", u"Create New Shot", None))
        self.loadShotButton.setText(QCoreApplication.translate("MainWindow", u"Set Active", None))
        ___qtreewidgetitem1 = self.shotFileList.headerItem()
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Size", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Last Modified", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"File Name", None));
        self.openShotFileButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.newShotFileButton.setText(QCoreApplication.translate("MainWindow", u"New", None))
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
        self.extLibsGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"External Asset Libraries", None))
        ___qtreewidgetitem2 = self.extLibsList.headerItem()
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Target", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Base Folder", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Folder Name", None));
        self.extLibFolderName.setText(QCoreApplication.translate("MainWindow", u"library", None))
        self.extLibBaseDropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"assets/textures", None))
        self.extLibBaseDropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"assets/3d/fbx", None))

        self.extLibTargetPath.setText(QCoreApplication.translate("MainWindow", u"F:/Drive/Assets/Textures", None))
        self.browseExtLibTargetButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.addNewExtLibButton.setText(QCoreApplication.translate("MainWindow", u"Add New Library", None))
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("MainWindow", u"Create work folders for these apps", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Project Features", None))
#if QT_CONFIG(tooltip)
        self.checkC4D.setToolTip(QCoreApplication.translate("MainWindow", u"C4D project folders", None))
#endif // QT_CONFIG(tooltip)
        self.checkC4D.setText(QCoreApplication.translate("MainWindow", u"Cinema 4D", None))
#if QT_CONFIG(tooltip)
        self.checkMaya.setToolTip(QCoreApplication.translate("MainWindow", u"Maya project structure", None))
#endif // QT_CONFIG(tooltip)
        self.checkMaya.setText(QCoreApplication.translate("MainWindow", u"Maya", None))
#if QT_CONFIG(tooltip)
        self.checkHoudini.setToolTip(QCoreApplication.translate("MainWindow", u"Houdini project folders", None))
#endif // QT_CONFIG(tooltip)
        self.checkHoudini.setText(QCoreApplication.translate("MainWindow", u"Houdini", None))
#if QT_CONFIG(tooltip)
        self.checkBlender.setToolTip(QCoreApplication.translate("MainWindow", u"Blender project folders", None))
#endif // QT_CONFIG(tooltip)
        self.checkBlender.setText(QCoreApplication.translate("MainWindow", u"Blender", None))
#if QT_CONFIG(tooltip)
        self.checkUSD.setToolTip(QCoreApplication.translate("MainWindow", u"USD folders", None))
#endif // QT_CONFIG(tooltip)
        self.checkUSD.setText(QCoreApplication.translate("MainWindow", u"USD", None))
#if QT_CONFIG(tooltip)
        self.checkOther.setToolTip(QCoreApplication.translate("MainWindow", u"Create \"Other\" folders in assets/shots ", None))
#endif // QT_CONFIG(tooltip)
        self.checkOther.setText(QCoreApplication.translate("MainWindow", u"Other", None))
#if QT_CONFIG(tooltip)
        self.checkUnreal.setToolTip(QCoreApplication.translate("MainWindow", u"Link assets to Unreal Project Content_Source", None))
#endif // QT_CONFIG(tooltip)
        self.checkUnreal.setText(QCoreApplication.translate("MainWindow", u"Unreal", None))
#if QT_CONFIG(tooltip)
        self.checkLivePlate.setToolTip(QCoreApplication.translate("MainWindow", u"Generate folders for footage, roto, 3d tracking", None))
#endif // QT_CONFIG(tooltip)
        self.checkLivePlate.setText(QCoreApplication.translate("MainWindow", u"Footage", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Realtime Engine Integration", None))
        self.setUnrealButton.setText(QCoreApplication.translate("MainWindow", u"Set Unreal Project", None))
#if QT_CONFIG(tooltip)
        self.dropProjectButton.setToolTip(QCoreApplication.translate("MainWindow", u"Sets current project to None", None))
#endif // QT_CONFIG(tooltip)
        self.dropProjectButton.setText(QCoreApplication.translate("MainWindow", u"Drop Project", None))
#if QT_CONFIG(tooltip)
        self.newProjectButton.setToolTip(QCoreApplication.translate("MainWindow", u"Create new project and make it active", None))
#endif // QT_CONFIG(tooltip)
        self.newProjectButton.setText(QCoreApplication.translate("MainWindow", u"Create New Project", None))
#if QT_CONFIG(tooltip)
        self.archiveProjectButton.setToolTip(QCoreApplication.translate("MainWindow", u"Remove temporary files and empty folders. Prepares for archiving", None))
#endif // QT_CONFIG(tooltip)
        self.archiveProjectButton.setText(QCoreApplication.translate("MainWindow", u"Clean and Archive", None))
#if QT_CONFIG(tooltip)
        self.updateProjectButton.setToolTip(QCoreApplication.translate("MainWindow", u"Update project configuration and create new folders if necessary", None))
#endif // QT_CONFIG(tooltip)
        self.updateProjectButton.setText(QCoreApplication.translate("MainWindow", u"Update Current Project", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Project), QCoreApplication.translate("MainWindow", u"Project", None))
        self.setHoudiniButton.setText(QCoreApplication.translate("MainWindow", u"Set Houdini", None))
        self.runHoudiniButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.setBlenderButton.setText(QCoreApplication.translate("MainWindow", u"Set Blender", None))
        self.runBlenderButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.setBlenderButton_2.setText(QCoreApplication.translate("MainWindow", u"Set Maya", None))
        self.runMayaButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.setBlenderButton_3.setText(QCoreApplication.translate("MainWindow", u"Set C4D", None))
        self.runC4DButton.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Apps), QCoreApplication.translate("MainWindow", u"Apps", None))
    # retranslateUi

