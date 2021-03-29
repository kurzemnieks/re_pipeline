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
        MainWindow.resize(363, 715)
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
        self.assetList = QListWidget(self.tab_Assets)
        self.assetList.setObjectName(u"assetList")
        self.assetList.setStyleSheet(u"background-color: rgb(80, 80, 80);")

        self.verticalLayout.addWidget(self.assetList)

        self.assetActions = QWidget(self.tab_Assets)
        self.assetActions.setObjectName(u"assetActions")
        self.assetActionLayout = QHBoxLayout(self.assetActions)
        self.assetActionLayout.setObjectName(u"assetActionLayout")
        self.newAssetButton = QPushButton(self.assetActions)
        self.newAssetButton.setObjectName(u"newAssetButton")

        self.assetActionLayout.addWidget(self.newAssetButton)

        self.loadAssetButton = QPushButton(self.assetActions)
        self.loadAssetButton.setObjectName(u"loadAssetButton")
        self.loadAssetButton.setEnabled(True)

        self.assetActionLayout.addWidget(self.loadAssetButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.assetActionLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.assetActions)

        self.mainTabs.addTab(self.tab_Assets, "")
        self.tab_Shots = QWidget()
        self.tab_Shots.setObjectName(u"tab_Shots")
        self.verticalLayout_3 = QVBoxLayout(self.tab_Shots)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.shotsList = QListWidget(self.tab_Shots)
        self.shotsList.setObjectName(u"shotsList")
        self.shotsList.setStyleSheet(u"background-color: rgb(80, 80, 80);")

        self.verticalLayout_3.addWidget(self.shotsList)

        self.shotActions = QWidget(self.tab_Shots)
        self.shotActions.setObjectName(u"shotActions")
        self.shotActionLayout = QHBoxLayout(self.shotActions)
        self.shotActionLayout.setObjectName(u"shotActionLayout")
        self.newShotButton = QPushButton(self.shotActions)
        self.newShotButton.setObjectName(u"newShotButton")

        self.shotActionLayout.addWidget(self.newShotButton)

        self.loadShotButton = QPushButton(self.shotActions)
        self.loadShotButton.setObjectName(u"loadShotButton")
        self.loadShotButton.setEnabled(True)

        self.shotActionLayout.addWidget(self.loadShotButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.shotActionLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.shotActions)

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
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.formLayout_3 = QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.checkBlender = QCheckBox(self.groupBox)
        self.checkBlender.setObjectName(u"checkBlender")
        self.checkBlender.setChecked(True)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.checkBlender)

        self.checkHoudini = QCheckBox(self.groupBox)
        self.checkHoudini.setObjectName(u"checkHoudini")
        self.checkHoudini.setMaximumSize(QSize(70, 16777215))
        self.checkHoudini.setChecked(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.checkHoudini)

        self.checkC4D = QCheckBox(self.groupBox)
        self.checkC4D.setObjectName(u"checkC4D")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.checkC4D)

        self.checkMaya = QCheckBox(self.groupBox)
        self.checkMaya.setObjectName(u"checkMaya")
        self.checkMaya.setMaximumSize(QSize(70, 16777215))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.checkMaya)

        self.checkUSD = QCheckBox(self.groupBox)
        self.checkUSD.setObjectName(u"checkUSD")
        self.checkUSD.setMaximumSize(QSize(70, 16777215))

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.checkUSD)

        self.checkOther = QCheckBox(self.groupBox)
        self.checkOther.setObjectName(u"checkOther")
        self.checkOther.setMaximumSize(QSize(70, 16777215))

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.checkOther)


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
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.newProjectButton = QPushButton(self.widget)
        self.newProjectButton.setObjectName(u"newProjectButton")

        self.verticalLayout_6.addWidget(self.newProjectButton)

        self.dropProjectButton = QPushButton(self.widget)
        self.dropProjectButton.setObjectName(u"dropProjectButton")
        self.dropProjectButton.setEnabled(False)

        self.verticalLayout_6.addWidget(self.dropProjectButton)

        self.archiveProjectButton = QPushButton(self.widget)
        self.archiveProjectButton.setObjectName(u"archiveProjectButton")
        self.archiveProjectButton.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.archiveProjectButton.sizePolicy().hasHeightForWidth())
        self.archiveProjectButton.setSizePolicy(sizePolicy3)

        self.verticalLayout_6.addWidget(self.archiveProjectButton)

        self.updateProjectButton = QPushButton(self.widget)
        self.updateProjectButton.setObjectName(u"updateProjectButton")
        self.updateProjectButton.setEnabled(False)

        self.verticalLayout_6.addWidget(self.updateProjectButton)


        self.verticalLayout_4.addWidget(self.widget)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.mainTabs.addTab(self.tab_Project, "")
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

        self.horizontalLayout_21.addWidget(self.runBlenderButton)


        self.verticalLayout_20.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_3)

        self.mainTabs.addTab(self.tab_Apps, "")

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
        QWidget.setTabOrder(self.loadShotButton, self.editHRes)
        QWidget.setTabOrder(self.editHRes, self.editVRes)
        QWidget.setTabOrder(self.editVRes, self.editFPS)
        QWidget.setTabOrder(self.editFPS, self.checkLivePlate)
        QWidget.setTabOrder(self.checkLivePlate, self.archiveProjectButton)
        QWidget.setTabOrder(self.archiveProjectButton, self.updateProjectButton)

        self.retranslateUi(MainWindow)

        self.mainTabs.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Project Manager", None))
        self.setRootButton.setText(QCoreApplication.translate("MainWindow", u"Set Project", None))
        self.projectRootLabel.setText(QCoreApplication.translate("MainWindow", u"C:/Projects/ProjectRoot", None))
        self.newAssetButton.setText(QCoreApplication.translate("MainWindow", u"Create New Asset", None))
        self.loadAssetButton.setText(QCoreApplication.translate("MainWindow", u"Set Active", None))
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Assets), QCoreApplication.translate("MainWindow", u"Assets", None))
        self.newShotButton.setText(QCoreApplication.translate("MainWindow", u"Create New Shot", None))
        self.loadShotButton.setText(QCoreApplication.translate("MainWindow", u"Set Active", None))
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
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("MainWindow", u"Create work folders for these apps", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"App Folders", None))
        self.checkBlender.setText(QCoreApplication.translate("MainWindow", u"Blender", None))
        self.checkHoudini.setText(QCoreApplication.translate("MainWindow", u"Houdini", None))
        self.checkC4D.setText(QCoreApplication.translate("MainWindow", u"Cinema 4D", None))
        self.checkMaya.setText(QCoreApplication.translate("MainWindow", u"Maya", None))
        self.checkUSD.setText(QCoreApplication.translate("MainWindow", u"USD", None))
        self.checkOther.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Additional folders", None))
#if QT_CONFIG(tooltip)
        self.checkLivePlate.setToolTip(QCoreApplication.translate("MainWindow", u"Generate folders for footage, roto, tracking", None))
#endif // QT_CONFIG(tooltip)
        self.checkLivePlate.setText(QCoreApplication.translate("MainWindow", u"Live plate compositing", None))
#if QT_CONFIG(tooltip)
        self.newProjectButton.setToolTip(QCoreApplication.translate("MainWindow", u"Create new project and make it active", None))
#endif // QT_CONFIG(tooltip)
        self.newProjectButton.setText(QCoreApplication.translate("MainWindow", u"Create New Project", None))
#if QT_CONFIG(tooltip)
        self.dropProjectButton.setToolTip(QCoreApplication.translate("MainWindow", u"Sets current project to None", None))
#endif // QT_CONFIG(tooltip)
        self.dropProjectButton.setText(QCoreApplication.translate("MainWindow", u"Drop Project", None))
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
        self.mainTabs.setTabText(self.mainTabs.indexOf(self.tab_Apps), QCoreApplication.translate("MainWindow", u"App Config", None))
    # retranslateUi

