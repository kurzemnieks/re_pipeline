import sys
import os
import winreg
import re_project
import re_houdini_launcher

from configparser import ConfigParser 

from PySide2 import QtWidgets, QtCore, QtGui
from ui import projman, assetdialog, shotdialog, projectdialog


class ProjectManagerUI( QtWidgets.QMainWindow, projman.Ui_MainWindow ):
    def __init__(self):
        super(ProjectManagerUI, self).__init__()
        self.setupUi(self)
        
        self.configParser = ConfigParser()
        
        self.defaultNewProjectRoot = "C:\\Projects\\"

        self.archiveProjectButton.setEnabled(False)
        self.archiveProjectButton.clicked.connect(self.onArchiveCurrentProject)
        self.cleanProjectButton.setEnabled(False)
        self.cleanProjectButton.clicked.connect(self.onCleanCurrentProject)
        self.updateProjectButton.setEnabled(False)
        self.updateProjectButton.clicked.connect(self.onUpdateCurrentProject)

        self.LoadConfig()

        if len(self.houdiniPathEdit.text()) == 0:
            houdini_path = self.TryGetDefaultHoudiniPath()
            if houdini_path is not None:
                self.houdiniPathEdit.setText(houdini_path)

        self.updateAppConfig()

        self.newAssetDialog = AssetDialogUI(self)
        self.newShotDialog = ShotDialogUI(self)
        self.newProjectDialog = ProjectDialogUI(self)

        self.editHRes.setValidator( QtGui.QIntValidator(1, 32000))        
        self.editVRes.setValidator( QtGui.QIntValidator(1, 32000))        
        self.editFPS.setValidator( QtGui.QDoubleValidator(1.0, 500.0, 3))

        self.setRootButton.clicked.connect(self.setProjectRootOrCreate)
        self.newAssetButton.clicked.connect(self.newAssetDialog.exec_)
        self.newShotButton.clicked.connect(self.newShotDialog.exec_)
        self.newProjectButton.clicked.connect(self.newProjectDialog.exec_)

        self.setHoudiniButton.clicked.connect(self.onClickSetHoudini)
        self.setBlenderButton.clicked.connect(self.onClickSetBlender)

        self.runHoudiniButton.clicked.connect(self.onRunHoudini)
        
        if re_project.is_in_houdini():
            self.mainTabs.removeTab(self.mainTabs.indexOf(self.tab_Apps))
        else:
            self.loadShotButton.hide()
            self.loadAssetButton.hide()
              
    def closeEvent(self, event):
        self.SaveConfig()
        event.accept()

    def SaveConfig(self):
        if not self.configParser.has_section("Defaults"):
            self.configParser.add_section("Defaults")

        if re_project._RE_PROJECT_INITIALIZED:
            self.configParser.set("Defaults", "last_project", re_project.get_project_root())

        self.configParser.set("Defaults", "projectsroot", os.path.normpath(self.defaultNewProjectRoot))

        if len(self.houdiniPathEdit.text()) > 0:
            self.configParser.set("Defaults", "houdini_path", self.houdiniPathEdit.text())
        if len(self.blenderPathEdit.text()) > 0:
            self.configParser.set("Defaults", "blender_path", self.blenderPathEdit.text())

        with open('config.ini', "w") as f:
            self.configParser.write(f)

    def LoadConfig(self):
        self.configParser.read('config.ini')
        if self.configParser.has_section("Defaults"):
            if self.configParser.has_option("Defaults", "last_project"):
                defaultProjRootDir = self.configParser.get("Defaults", "last_project")
                
                if os.path.exists(defaultProjRootDir):
                    self.setProjectRootOrCreate(defaultProjRootDir)

            if self.configParser.has_option("Defaults","projectsroot"):
                self.defaultNewProjectRoot = self.configParser.get("Defaults", "projectsroot")

            if self.configParser.has_option("Defaults", "houdini_path"):
                self.houdiniPathEdit.setText( self.configParser.get("Defaults","houdini_path"))

            if self.configParser.has_option("Defaults", "blender_path"):
                self.blenderPathEdit.setText( self.configParser.get("Defaults","blender_path"))

    def TryGetDefaultHoudiniPath(self):
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)        
            hkey = winreg.OpenKey(reg, r"SOFTWARE\Side Effects Software\Houdini")
            key_value = winreg.EnumValue(hkey, 0)
            houdini_path = key_value[1] + r"bin\houdini.exe"
            houdini_path = os.path.normpath(houdini_path)
            return houdini_path
        except OSError:
            return None


    def setProjectRootOrCreate(self, defaultRootDir=None):
        
        if not defaultRootDir:
            dlg = QtWidgets.QFileDialog()
            dlg.setFileMode( QtWidgets.QFileDialog.Directory )

            if dlg.exec_():
                folder = dlg.selectedFiles()
                if len(folder) > 0:
                    defaultRootDir = folder[0]

        if defaultRootDir:
            result = re_project.set_current_root_dir(defaultRootDir)
            if not result:
                self.updateAppConfig()
                re_project.create_project(self.appConfig)
                re_project.create_project_folders()
            

            self.onProjectLoaded()

            self.projectRootLabel.setText(re_project.get_project_root())        

    def onCreateNewAsset(self, name):
        if re_project.create_asset_folders(name):
            self.updateAssetList()  
            self.statusBar.showMessage("New asset created!")

    def onCreateNewShot(self, sequenceNum, shotNum):
        if re_project.create_shot(sequenceNum, shotNum):
            self.updateShotList()
            self.statusBar.showMessage("New shot created!")

    def onUpdateCurrentProject(self):
        if re_project.create_project_folders():
            self.statusBar.showMessage("Project folders updated! Missing ones created!")

    def onCreateNewProject(self, projectPath):
        self.setProjectRootOrCreate(projectPath)
        #self.updateAppConfig()
        #re_project.create_project(self.appConfig)
        #re_project.create_project_folders()
        #self.setProjectRoot(projectPath)

    def onArchiveCurrentProject(self):
        print("Not implemented")

    def onCleanCurrentProject(self):
        print("Not implemented")

    def onClickSetHoudini(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode( QtWidgets.QFileDialog.ExistingFile )
        dlg.setDefaultSuffix("exe")
        dlg.setNameFilter("houdini.exe")
        if os.path.exists("C:\\Program Files\\Side Effects Software\\"):
            dlg.setDirectory("C:\\Program Files\\Side Effects Software\\")
        else:
            dlg.setDirectory("C:\\Program Files\\")

        if dlg.exec_():
            houdini_path = dlg.selectedFiles()
            if len(houdini_path) > 0:
                self.houdiniPathEdit.setText(os.path.normpath(houdini_path[0]))

    def onRunHoudini(self):
        houdini_path = self.houdiniPathEdit.text()
        re_root = os.getenv("RE_ROOT")
        re_houdini_launcher.run_houdini(houdini_path, re_root , re_project._RE_PROJECT_ROOT)                

    def onClickSetBlender(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode( QtWidgets.QFileDialog.ExistingFile )
        dlg.setDefaultSuffix("exe")
        dlg.setNameFilter("blender.exe")
        if os.path.exists("C:\\Program Files\\Blender Foundation\\"):
            dlg.setDirectory("C:\\Program Files\\Blender Foundation\\")
        else:
            dlg.setDirectory("C:\\Program Files\\")

        if dlg.exec_():
            blender_path = dlg.selectedFiles()
            if len(blender_path) > 0:
                self.blenderPathEdit.setText(os.path.normpath(blender_path[0]))

    def updateAppConfig(self):
        self.appConfig = re_project.AppConfig( self.checkBlender.isChecked(),
                                            self.checkHoudini.isChecked(),
                                            self.checkMaya.isChecked(),
                                            self.checkC4D.isChecked(),
                                            self.checkUSD.isChecked(),
                                            self.checkOther.isChecked())

    def onProjectLoaded(self):

        self.statusBar.showMessage("Project loaded!")

        proj_app_cfg = re_project.get_project_app_config()
        self.checkBlender.setChecked( proj_app_cfg.blender )
        self.checkHoudini.setChecked( proj_app_cfg.houdini )
        self.checkMaya.setChecked( proj_app_cfg.maya )
        self.checkC4D.setChecked( proj_app_cfg.c4d )
        self.checkUSD.setChecked( proj_app_cfg.usd )
        self.checkOther.setChecked( proj_app_cfg.other )

        self.editHRes.setText(str(re_project.get_project_default_rez()['x']))
        self.editVRes.setText(str(re_project.get_project_default_rez()['y']))
        self.editFPS.setText(str(re_project.get_project_default_fps()))

        self.labelExtTexPath.setText(re_project.get_project_ext_asset_lib())

        self.archiveProjectButton.setEnabled(True)
        self.cleanProjectButton.setEnabled(True)
        self.updateProjectButton.setEnabled(True)

        self.updateAssetList()
        self.updateShotList()

    def updateAssetList(self):
        self.assetList.clear()
        all_assets = re_project.scan_project_assets()
        for asset_name in all_assets:
            asset_item = QtWidgets.QListWidgetItem(asset_name, self.assetList)

    def updateShotList(self):
        self.shotsList.clear()
        all_shots = re_project.scan_project_shots()
        for shot_name in all_shots:
            shot_item = QtWidgets.QListWidgetItem(shot_name, self.shotsList)
        
class AssetDialogUI( QtWidgets.QDialog, assetdialog.Ui_AssetDialog):
    def __init__(self, parent=None):
        super(AssetDialogUI, self).__init__(parent=parent)
        self.setupUi(self)    

        self.parent = parent
        self.buttonBox.accepted.connect(self.create_new_asset)
        self.buttonBox.rejected.connect(self.close)

    def create_new_asset(self):
        #print(self.editAssetName.text())   
        self.parent.onCreateNewAsset(self.editAssetName.text())     
        self.close()


class ShotDialogUI( QtWidgets.QDialog, shotdialog.Ui_ShotDialog):
    def __init__(self, parent=None):
        super(ShotDialogUI, self).__init__(parent=parent)
        self.setupUi(self)
        
        self.parent = parent
        self.buttonBox.accepted.connect(self.create_new_shot)
        self.buttonBox.rejected.connect(self.close)

    def create_new_shot(self):
        self.parent.onCreateNewShot(self.spinSequence.value(), self.spinShot.value())
        self.close() 

class ProjectDialogUI( QtWidgets.QDialog, projectdialog.Ui_ProjectDialog):
    def __init__(self, parent=None):
        super(ProjectDialogUI, self).__init__(parent=parent)
        self.setupUi(self)
        
        self.parent = parent
        self.buttonBox.accepted.connect(self.create_new_project)
        self.buttonBox.rejected.connect(self.close)

        self.browseButton.clicked.connect(self.browseProjectRoot)

    def showEvent(self, event):
        super(ProjectDialogUI, self).showEvent(event)
        self.labelProjectRoot.setText(self.parent.defaultNewProjectRoot)

    def create_new_project(self):
        projPath = os.path.join(self.labelProjectRoot.text(), self.editProjectName.text())
        self.parent.onCreateNewProject(projPath)
        self.close() 

    def browseProjectRoot(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode( QtWidgets.QFileDialog.Directory )
        if os.path.exists(self.labelProjectRoot.text()):
            dlg.setDirectory(self.labelProjectRoot.text())

        if dlg.exec_():
            folder = dlg.selectedFiles()
            if len(folder) > 0:
                self.labelProjectRoot.setText(folder[0])
                self.parent.defaultNewProjectRoot = self.labelProjectRoot.text()

def _getProjectManagerWidget():
    pmUI = ProjectManagerUI()
    return pmUI

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("fusion")
    pmUI = ProjectManagerUI()
    pmUI.show()
    app.exec_()