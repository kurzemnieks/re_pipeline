import sys
import os
import project

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
        

    def closeEvent(self, event):
        self.SaveConfig()
        event.accept()

    def SaveConfig(self):
        if not self.configParser.has_section("Defaults"):
            self.configParser.add_section("Defaults")

        if project._RE_PROJECT_INITIALIZED:
            self.configParser.set("Defaults", "last_project", project.get_project_root())

        self.configParser.set("Defaults", "projectsroot", os.path.normpath(self.defaultNewProjectRoot))

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

    def setProjectRootOrCreate(self, defaultRootDir=None):
        
        if not defaultRootDir:
            dlg = QtWidgets.QFileDialog()
            dlg.setFileMode( QtWidgets.QFileDialog.Directory )

            if dlg.exec_():
                folder = dlg.selectedFiles()
                if len(folder) > 0:
                    defaultRootDir = folder[0]

        if defaultRootDir:
            result = project.set_current_root_dir(defaultRootDir)
            if not result:
                self.updateAppConfig()
                project.create_project(self.appConfig)
                project.create_project_folders()
            

            self.onProjectLoaded()

            self.projectRootLabel.setText(project.get_project_root())        

    def onCreateNewAsset(self, name):
        if project.create_asset_folders(name):
            self.updateAssetList()  
            self.statusBar.showMessage("New asset created!")

    def onCreateNewShot(self, sequenceNum, shotNum):
        if project.create_shot(sequenceNum, shotNum):
            self.updateShotList()
            self.statusBar.showMessage("New shot created!")

    def onUpdateCurrentProject(self):
        if project.create_project_folders():
            self.statusBar.showMessage("Project folders updated! Missing ones created!")

    def onCreateNewProject(self, projectPath):
        self.setProjectRootOrCreate(projectPath)
        #self.updateAppConfig()
        #project.create_project(self.appConfig)
        #project.create_project_folders()
        #self.setProjectRoot(projectPath)

    def onArchiveCurrentProject(self):
        print("Not implemented")

    def onCleanCurrentProject(self):
        print("Not implemented")

    def updateAppConfig(self):
        self.appConfig = project.AppConfig( self.checkBlender.isChecked(),
                                            self.checkHoudini.isChecked(),
                                            self.checkMaya.isChecked(),
                                            self.checkC4D.isChecked(),
                                            self.checkUSD.isChecked())

    def onProjectLoaded(self):

        self.statusBar.showMessage("Project loaded!")

        proj_app_cfg = project.get_project_app_config()
        self.checkBlender.setChecked( proj_app_cfg.blender )
        self.checkHoudini.setChecked( proj_app_cfg.houdini )
        self.checkMaya.setChecked( proj_app_cfg.maya )
        self.checkC4D.setChecked( proj_app_cfg.c4d )
        self.checkUSD.setChecked( proj_app_cfg.usd )

        self.editHRes.setText(str(project.get_project_default_rez()['x']))
        self.editVRes.setText(str(project.get_project_default_rez()['y']))
        self.editFPS.setText(str(project.get_project_default_fps()))

        self.labelExtTexPath.setText(project.get_project_ext_asset_lib())

        self.archiveProjectButton.setEnabled(True)
        self.cleanProjectButton.setEnabled(True)
        self.updateProjectButton.setEnabled(True)

        self.updateAssetList()
        self.updateShotList()

    def updateAssetList(self):
        self.assetList.clear()
        all_assets = project.scan_project_assets()
        for asset_name in all_assets:
            asset_item = QtWidgets.QListWidgetItem(asset_name, self.assetList)

    def updateShotList(self):
        self.shotsList.clear()
        all_shots = project.scan_project_shots()
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

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("fusion")
    pmUI = ProjectManagerUI()
    pmUI.show()
    app.exec_()