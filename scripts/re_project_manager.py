import sys
import os
import winreg
import re_project
import re_houdini_launcher
import re_blender_launcher
from pathlib import Path
from configparser import ConfigParser 
import math
import datetime

from PySide2 import QtWidgets, QtCore, QtGui
from ui import projman, assetdialog, shotdialog, projectdialog

class NewFileDialogUI( QtWidgets.QDialog, assetdialog.Ui_AssetDialog):

    ASSET_TYPE_ASSET = 1
    ASSET_TYPE_SHOT = 2

    def __init__(self, parent=None):
        super(NewFileDialogUI, self).__init__(parent=parent)
        self.setupUi(self)    

        self.parent = parent
        self.buttonBox.accepted.connect(self.create_new_asset)
        self.buttonBox.rejected.connect(self.close)
        self.editAssetName.setText("")

        self.base_path:Path = None
        self.create_callback = None

        self.asset_main_name = ""

        self.asset_type = 0

    def setCreateCallback( self, callback_func ):
        self.create_callback = callback_func

    def setQuestion(self, question:str):
        self.nameLabel = question

    def setDefaultName(self, name:str):
        self.editAssetName.setText(name)
    
    def setTitle(self, title:str):
        self.windowTitle = title

    def setAssetMainName(self, main_name:str):
        self.asset_main_name = main_name

    def setBasePath( self, path:str):
        if path is None:
            self.base_path = None
        else:
            self.base_path = Path(path)

    def create_new_asset(self):        
        if self.create_callback is not None:
            if self.base_path is not None:
                full_path= self.base_path / self.editAssetName.text()
            else:
                full_path = Path(self.editAssetName.text())
            self.create_callback(full_path.as_posix(), self)
        self.close()
class ProjectManagerUI( QtWidgets.QMainWindow, projman.Ui_MainWindow ):
    def __init__(self):
        super(ProjectManagerUI, self).__init__()
        self.setupUi(self)
        
        self.configParser = ConfigParser()
        
        self.defaultNewProjectRoot = "C:\\Projects\\"

        self.sceneDCCExtensions = ["*.*"] #override this for DCC app PM implementations to return specific scene file types

        self.active_file : re_project.ActiveFile = None

        self._resetPMUI()

        self.newFileDialog = NewFileDialogUI(self)
        self.newShotDialog = ShotDialogUI(self)
        self.newProjectDialog = ProjectDialogUI(self)


        self.newProjectButton.clicked.connect(self.newProjectDialog.exec_)
        self.archiveProjectButton.clicked.connect(self.onArchiveCurrentProject)        
        self.updateProjectButton.clicked.connect(self.onUpdateCurrentProject)
        self.dropProjectButton.clicked.connect(self.dropCurrentProject)

        self.loadPMConfig()

        if len(self.houdiniPathEdit.text()) == 0:
            houdini_path = self.tryGetDefaultHoudiniPath()
            if houdini_path is not None:
                self.houdiniPathEdit.setText(houdini_path.as_posix())

        self.getProjectFeaturesFromUI()


        self.editHRes.setValidator( QtGui.QIntValidator(1, 32000))        
        self.editVRes.setValidator( QtGui.QIntValidator(1, 32000))        
        self.editFPS.setValidator( QtGui.QDoubleValidator(1.0, 500.0, 3))

        self.setRootButton.clicked.connect(self.setProjectRootOrCreate)
        self.newAssetButton.clicked.connect(self.onNewAssetClick)
        self.newShotButton.clicked.connect(self.newShotDialog.exec_)

        self.assetList.itemClicked.connect(self.onAssetItemClick)              
        self.assetFileList.itemClicked.connect(self.onAssetFileSelect)

        self.shotsList.itemClicked.connect(self.onShotItemClick)
        self.shotFileList.itemClicked.connect(self.onShotFileSelect)

        self.setHoudiniButton.clicked.connect(self.onClickSetHoudini)
        self.setBlenderButton.clicked.connect(self.onClickSetBlender)

        self.runHoudiniButton.clicked.connect(self.onRunHoudini)
        self.runBlenderButton.clicked.connect(self.onRunBlender)

        self.loadAssetButton.clicked.connect(self.onClickLoadAsset)
        self.loadShotButton.clicked.connect(self.onClickLoadShot)

        #self.buttonExtTextures.clicked.connect(self.onClickExtTextLink)
        self.addNewExtLibButton.clicked.connect(self.onClickAddExtLib)
        self.browseExtLibTargetButton.clicked.connect(self.onClickBrowseExtLibTarget)

        self.editHRes.editingFinished.connect(self.onModifyProjectConfig)
        self.editVRes.editingFinished.connect(self.onModifyProjectConfig)
        self.editFPS.editingFinished.connect(self.onModifyProjectConfig)

        self.checkBlender.clicked.connect(self.onModifyProjectConfig)
        self.checkHoudini.clicked.connect(self.onModifyProjectConfig)
        self.checkC4D.clicked.connect(self.onModifyProjectConfig)
        self.checkMaya.clicked.connect(self.onModifyProjectConfig)
        self.checkOther.clicked.connect(self.onModifyProjectConfig)
        self.checkUSD.clicked.connect(self.onModifyProjectConfig)
        self.checkUnreal.clicked.connect(self.onModifyProjectConfig)
        self.checkLivePlate.clicked.connect(self.onModifyProjectConfig)

        self.editShotNamePrefix.editingFinished.connect(self.onModifyProjectConfig)

        if not re_project.is_in_dcc_app():
            self.loadShotButton.hide()
            self.loadAssetButton.hide()

            self.assetLayout.removeWidget(self.assetFileList)
            self.assetFileList.deleteLater()
            self.assetFileList = None
            
            self.assetFileActionGroup.removeWidget(self.openAssetFileButton)
            self.assetFileActionGroup.removeWidget(self.newAssetFileButton)
            #self.assetFileActionGroup.removeWidget(self.versionUpAssetButton)
            #self.assetFileActionGroup.removeWidget(self.publishAssetButton)
            self.openAssetFileButton.deleteLater()
            self.newAssetFileButton.deleteLater()
            #self.versionUpAssetButton.deleteLater()
            #self.publishAssetButton.deleteLater()

            self.openAssetFileButton = None
            self.newAssetFileButton = None
            self.publishAssetButton = None
            self.versionUpAssetButton = None

            self.assetLayout.removeItem(self.assetFileActionGroup)
            self.assetFileActionGroup.deleteLater()
            self.assetFileActionGroup = None

            self.shotLayout.removeWidget(self.shotFileList)
            self.shotFileList.deleteLater()
            self.shotFileList = None
            
            self.shotFileActionGroup.removeWidget(self.openShotFileButton)
            self.shotFileActionGroup.removeWidget(self.newShotFileButton)
            #self.shotFileActionGroup.removeWidget(self.versionUpShotButton)
            #self.shotFileActionGroup.removeWidget(self.publishShotButton)
            self.openShotFileButton.deleteLater()
            self.newShotFileButton.deleteLater()
            #self.publishShotButton.deleteLater()
            #self.versionUpShotButton.deleteLater()

            self.openShotFileButton = None
            self.newShotFileButton = None
            self.versionUpShotButton = None
            self.publishShotButton = None

            self.shotLayout.removeItem(self.shotFileActionGroup)            
            self.shotFileActionGroup.deleteLater()
            self.shotFileActionGroup = None

            self.setUnrealButton.clicked.connect(self.onChooseUnrealProject)

            self.mainTabs.removeTab(self.mainTabs.indexOf(self.tab_Edit))
            #self.tab_Edit.children
            #self.mainTabs.findChild()

        else:
            self.mainTabs.removeTab(self.mainTabs.indexOf(self.tab_Apps))
            self.openAssetFileButton.clicked.connect(self.onOpenAssetFileClick)
            self.newAssetFileButton.clicked.connect(self.onNewAssetFileClick)
            self.openShotFileButton.clicked.connect(self.onOpenShotFileClick)
            self.newShotFileButton.clicked.connect(self.onNewShotFileClick)
            #self.versionUpAssetButton.clicked.connect(self.onVersionUpAssetClick)
            #self.versionUpShotButton.clicked.connect(self.onVersionUpShotClick)
            #self.publishAssetButton.clicked.connect(self.onPublishAssetClick)
            #self.publishShotButton.clicked.connect(self.onPublishShotClick)

    def _resetPMUI(self):
        self.assetList.clear()
        self.shotsList.clear() 
        self.loadAssetButton.setEnabled(False)
        self.loadShotButton.setEnabled(False)
        self.newAssetButton.setEnabled(False)
        self.newShotButton.setEnabled(False)

        self.updateProjectSettingsUI()

        self.editShotNamePrefix.setText("project_name")

        self.archiveProjectButton.setEnabled(False)
        self.updateProjectButton.setEnabled(False)
        self.dropProjectButton.setEnabled(False)

        self.extLibBaseDropdown.setEnabled(False)
        self.extLibBaseDropdown.clear()

        if self.assetFileActionGroup is not None:
            self.openAssetFileButton.setEnabled(False)
            self.newAssetFileButton.setEnabled(True)
            #self.versionUpAssetButton.setEnabled(False)
            #self.publishAssetButton.setEnabled(False)
            self.assetFileList.clear()   

        if self.shotFileActionGroup is not None:
            self.openShotFileButton.setEnabled(False)
            self.newShotFileButton.setEnabled(True)
            #self.versionUpShotButton.setEnabled(False)
            #self.publishShotButton.setEnabled(False)
            self.shotFileList.clear()                       

        self.projectRootLabel.setText("")
        self.extLibsList.clear()

        self.statusBar.showMessage("No project selected!")
              
    def closeEvent(self, event):
        self.savePMConfig()
        event.accept()

    def savePMConfig(self):
        if not self.configParser.has_section("Defaults"):
            self.configParser.add_section("Defaults")

        if re_project._RE_PROJECT_INITIALIZED:
            self.configParser.set("Defaults", "last_project", re_project.get_project_root().as_posix())

        self.configParser.set("Defaults", "projectsroot", Path(self.defaultNewProjectRoot).as_posix())

        if len(self.houdiniPathEdit.text()) > 0:
            self.configParser.set("Defaults", "houdini_path", self.houdiniPathEdit.text())
        if len(self.blenderPathEdit.text()) > 0:
            self.configParser.set("Defaults", "blender_path", self.blenderPathEdit.text())

        with open('config.ini', "w") as f:
            self.configParser.write(f)

    def loadPMConfig(self):
        self.configParser.read('config.ini')
        if self.configParser.has_section("Defaults"):
            if self.configParser.has_option("Defaults", "last_project"):
                defaultProjRootDir = Path(self.configParser.get("Defaults", "last_project"))
                
                if defaultProjRootDir.exists():
                    self.setProjectRootOrCreate(defaultProjRootDir.as_posix())

            if self.configParser.has_option("Defaults","projectsroot"):
                self.defaultNewProjectRoot = Path(self.configParser.get("Defaults", "projectsroot")).as_posix()

            if self.configParser.has_option("Defaults", "houdini_path"):
                self.houdiniPathEdit.setText( Path(self.configParser.get("Defaults","houdini_path")).as_posix())

            if self.configParser.has_option("Defaults", "blender_path"):
                self.blenderPathEdit.setText( Path(self.configParser.get("Defaults","blender_path")).as_posix())

    def tryGetDefaultHoudiniPath(self):
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)        
            hkey = winreg.OpenKey(reg, r"SOFTWARE\Side Effects Software\Houdini")
            key_value = winreg.EnumValue(hkey, 0)
            houdini_path = Path(key_value[1]) / "bin/houdini.exe"            
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
            result = re_project.set_project_root_folder(defaultRootDir)
            if not result:
                newAppConfig = self.getProjectFeaturesFromUI()
                re_project.create_project(newAppConfig)
                re_project.create_project_folders()
            
            self._resetPMUI()
            self.onProjectLoaded()

            self.projectRootLabel.setText(re_project.get_project_root().as_posix())        

    def onCreateNewAsset(self, name, file_dialog : NewFileDialogUI):
        if re_project.create_asset_folders(name):
            self.updateAssetList()              
            self.statusBar.showMessage("New asset created!")

    def onCreateNewShot(self, sequenceNum, shotNum):
        if re_project.create_shot(sequenceNum, shotNum):
            self.updateShotList()
            self.statusBar.showMessage("New shot created!")

    def onUpdateCurrentProject(self):
        if re_project.create_project_folders() and re_project.update_all_asset_folders() and re_project.update_all_shot_folders():
            self.statusBar.showMessage("Project updated!")
        re_project.save_project_config()

    def dropCurrentProject(self):
        re_project.drop_project()
        self._resetPMUI()    
   
    def onCreateNewProject(self, projectPath):
        self.setProjectRootOrCreate(projectPath)

    def onArchiveCurrentProject(self):
        print("Not implemented")

    def onCleanCurrentProject(self):
        print("Not implemented")

    def onChooseUnrealProject(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode( QtWidgets.QFileDialog.Directory )

        unrealProjectFolder = Path("")

        if dlg.exec_():
            folder = dlg.selectedFiles()
            if len(folder) > 0:
                unrealProjectFolder = Path(folder[0])
                self.unrealProjectPathEdit.setText(unrealProjectFolder.as_posix())
                self.onModifyProjectConfig()

    def onClickSetHoudini(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode( QtWidgets.QFileDialog.ExistingFile )
        dlg.setDefaultSuffix("exe")
        dlg.setNameFilter("houdini.exe")
        hpath = Path("C:/Program Files/Side Effects Software/")
        if hpath.exists():
            dlg.setDirectory(str(hpath))
        else:
            dlg.setDirectory(str(Path("C:/Program Files/")))

        if dlg.exec_():
            houdini_path = dlg.selectedFiles()
            if len(houdini_path) > 0:
                self.houdiniPathEdit.setText(Path(houdini_path[0]).as_posix())

    def onRunHoudini(self):
        houdini_path = Path(self.houdiniPathEdit.text()) #houdini executable path
        
        re_root_str : str = os.getenv("RE_ROOT")

        if re_root_str is None:
            re_root_str = "G:\My Drive\Tools\Pipeline\re_pipeline"

        re_root = Path(re_root_str) #pipeline root dir

        re_houdini_launcher.run_houdini(houdini_path, re_root , re_project.get_project_root())    
        self.close()            

    def onRunBlender(self):
        blender_path = Path(self.blenderPathEdit.text())

        re_root_str : str = os.getenv("RE_ROOT")

        if re_root_str is None:
            re_root_str = "G:\My Drive\Tools\Pipeline\re_pipeline"

        re_root = Path(re_root_str) #pipeline root dir

        re_blender_launcher.run_blender(blender_path, re_root, re_project.get_project_root())
        self.close()

    def onClickSetBlender(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode( QtWidgets.QFileDialog.ExistingFile )
        dlg.setDefaultSuffix("exe")
        dlg.setNameFilter("blender.exe")
        bpath = Path("C:/Program Files/Blender Foundation/")
        if bpath.exists():
            dlg.setDirectory(str(bpath))
        else:
            dlg.setDirectory(str(Path("C:/Program Files/")))

        if dlg.exec_():
            blender_path = dlg.selectedFiles()
            if len(blender_path) > 0:
                self.blenderPathEdit.setText(Path(blender_path[0]).as_posix())

    def getProjectFeaturesFromUI(self):
        proj_features_cfg : re_project.ProjectFeatures = re_project.get_empty_project_features()
        proj_features_cfg["blender"] = self.checkBlender.isChecked()
        proj_features_cfg["houdini"] = self.checkHoudini.isChecked()
        proj_features_cfg["c4d"] = self.checkC4D.isChecked()
        proj_features_cfg["maya"] = self.checkMaya.isChecked()
        proj_features_cfg["usd"] = self.checkUSD.isChecked()
        proj_features_cfg["other"] = self.checkOther.isChecked()
        proj_features_cfg["unreal"] = self.checkUnreal.isChecked()
        proj_features_cfg["footage"] = self.checkLivePlate.isChecked()

        return proj_features_cfg

    def onProjectLoaded(self):

        self.statusBar.showMessage("Project loaded!")

        self.updateProjectSettingsUI()

        self.archiveProjectButton.setEnabled(True)
        self.updateProjectButton.setEnabled(True)
        self.dropProjectButton.setEnabled(True)
        self.newAssetButton.setEnabled(True)
        self.newShotButton.setEnabled(True)

        self.extLibBaseDropdown.setEnabled(True)        
        base_folder_scruct = re_project._get_project_folder_struct()
        asset_folders = base_folder_scruct[0]
        folder_list = []
        re_project._list_folder_template_items(asset_folders, folder_list)
        folder_list.remove("assets")
        self.extLibBaseDropdown.addItems(folder_list)

        ext_libs_list = re_project.get_project_external_libs()
        for ext_lib in ext_libs_list:
             self.extLibsList.addTopLevelItem(QtWidgets.QTreeWidgetItem( [ext_lib[0], ext_lib[1], ext_lib[2]] ))

        self.updateAssetList()
        self.updateShotList()
    
    def updateProjectSettingsUI(self):
        if re_project.is_project_initialized():
            
            proj_features_cfg = re_project.get_project_features()

            self.checkBlender.setChecked( proj_features_cfg["blender"] )
            self.checkHoudini.setChecked( proj_features_cfg["houdini"] )
            self.checkMaya.setChecked( proj_features_cfg["maya"] )
            self.checkC4D.setChecked( proj_features_cfg["c4d"] )
            self.checkUSD.setChecked( proj_features_cfg["usd"] )
            self.checkOther.setChecked( proj_features_cfg["other"] )
            self.checkUnreal.setChecked( proj_features_cfg["unreal"] )
            self.checkLivePlate.setChecked( proj_features_cfg["footage"])

            self.editHRes.setText(str(re_project.get_project_default_rez()['x']))
            self.editVRes.setText(str(re_project.get_project_default_rez()['y']))
            self.editFPS.setText(str(re_project.get_project_default_fps()))

            self.unrealProjectPathEdit.setText(re_project.get_project_unreal_project())

            self.editShotNamePrefix.setText( re_project._RE_PROJECT_NAME_PREFIX )

            #self.labelExtTexPath.setText(re_project.get_project_ext_asset_lib())
            #TODO: external textures lib

    def onModifyProjectConfig(self, value=None):
        if re_project.is_project_initialized():
            new_proj_featues_cfg = self.getProjectFeaturesFromUI()
            re_project.update_project_features_config(new_proj_featues_cfg, False)

            fps = float(self.editFPS.text())
            re_project.set_project_default_fps(fps)

            hres = int(self.editHRes.text())
            vres = int(self.editVRes.text())
            re_project.set_project_default_rez(hres, vres)        

            name_prefix = self.editShotNamePrefix.text()
            re_project.set_project_name_prefix(name_prefix)    

            re_project.set_project_unreal_project_path(self.unrealProjectPathEdit.text())       

            re_project.save_project_config()

    def updateAssetList(self):
        if not re_project.is_project_initialized():
            return

        old_item = self.assetList.currentItem()
        old_item_name = None if old_item is None else old_item.text()
        
        self.assetList.clear()
        all_assets = re_project.scan_project_assets()
        for asset_path in all_assets:
            asset_item = QtWidgets.QListWidgetItem(asset_path, self.assetList)

        if old_item_name is not None:
            items = self.assetList.findItems(old_item_name, QtCore.Qt.MatchExactly)
            if len(items)>0:
                self.assetList.setCurrentItem(items[0])

    def updateShotList(self):
        if not re_project.is_project_initialized():
            return

        self.shotsList.clear()
        all_shots = re_project.scan_project_shots()
        for shot_name in all_shots:
            shot_item = QtWidgets.QListWidgetItem(shot_name, self.shotsList)

    def onAssetItemClick(self, item : QtWidgets.QListWidgetItem):
        if item is not None:
            self.loadAssetButton.setEnabled(True)
            if re_project._RE_DCC_APP != '':
                asset_path : Path = re_project.get_asset_path(item.text())
                self.openAssetFileButton.setEnabled(False)
                self.UpdateFileList(asset_path, self.assetFileList)

    def onShotItemClick(self, item : QtWidgets.QListWidgetItem):
        if item is not None:
            self.loadShotButton.setEnabled(True)
            if re_project._RE_DCC_APP != '':
                shot_data = re_project.get_shot_data_from_name(item.text())
                shot_path : Path = re_project.get_shot_path(shot_data[0], shot_data[1])
                self.openShotFileButton.setEnabled(False)
                self.UpdateFileList(shot_path, self.shotFileList)

    def onClickLoadAsset(self):
        print("NOT SUPPOSED TO BE CALLED")

    def onClickLoadShot(self):
        print("NOT SUPPOSED TO BE CALLED")

    def onClickExtTextLink(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode( QtWidgets.QFileDialog.Directory )

        texFolder = ''
        folders = None
        if dlg.exec_():
            folders = dlg.selectedFiles()
            if len(folders) > 0:
                texFolder = folders[0]
        
        #print("Setting external texture lib to: " + texFolder)
        re_project.change_external_texture_lib(texFolder)
        self.updateProjectSettingsUI()

    def onClickAddExtLib(self):
        folder_name = self.extLibFolderName.text()
        base_folder = self.extLibBaseDropdown.currentText()
        target_path = self.extLibTargetPath.text()

        if len(folder_name) == 0 or len(base_folder)==0 or len(target_path)==0:
            print("Error: Can't add external asset library. You must fill all fields!")
            return

        if re_project.add_external_lib_folder(folder_name, base_folder, target_path):
            self.extLibsList.addTopLevelItem(QtWidgets.QTreeWidgetItem([folder_name, base_folder, target_path]))

    def onClickBrowseExtLibTarget(self):        
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode( QtWidgets.QFileDialog.Directory )

        libTargetFolder = ''
        folders = None
        if dlg.exec_():
            folders = dlg.selectedFiles()
            if len(folders) > 0:
                libTargetFolder = folders[0]
        
        self.extLibTargetPath.setText( Path(libTargetFolder).as_posix())

    def convert_file_size(size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    def UpdateFileList(self, baseFolder  : Path, fileList : QtWidgets.QTreeWidget):        
        assert(fileList)
        assert(baseFolder)
        asset_path = baseFolder / re_project._RE_DCC_APP
            
        fileList.clear()
        
        for pattern in self.sceneDCCExtensions:
            filelist_gen = asset_path.glob(pattern)
            file_list = list(filelist_gen)
            for file_path in file_list:
                rel_path : Path = file_path.relative_to( asset_path )
                #print(rel_path.as_posix())
                file_stats : os.stat_result = file_path.stat()
                mtime = file_stats.st_mtime
                timestamp_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d-%H:%M')
                fileList.addTopLevelItem(QtWidgets.QTreeWidgetItem( [rel_path.as_posix(), timestamp_str, ProjectManagerUI.convert_file_size(file_stats.st_size)] ))

        fileList.resizeColumnToContents(0)
        fileList.resizeColumnToContents(2)

    def onAssetFileSelect(self, item):
        self.openAssetFileButton.setEnabled(True)

    def onShotFileSelect(self, item):
        self.openShotFileButton.setEnabled(True)        

    def onNewAssetClick(self):
        self.newFileDialog.setTitle("New Asset")
        self.newFileDialog.setQuestion("Asset name:")
        self.newFileDialog.setCreateCallback(self.onCreateNewAsset)
        self.newFileDialog.setDefaultName("")
        self.newFileDialog.setAssetMainName("")
        self.newFileDialog.setBasePath(None)
        self.newFileDialog.exec_()
        
    def onNewAssetFileClick(self):
        pass        

    def onOpenAssetFileClick(self):
        pass

    def onNewShotFileClick(self):
        pass   

    def onOpenShotFileClick(self):
        pass
    
    def onVersionUpAssetClick(self):
        pass

    def onVersionUpShotClick(self):
        pass

    def onPublishAssetClick(self):
        pass

    def onPublishShotClick(self):
        pass

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
        projPath = Path(self.labelProjectRoot.text()) / self.editProjectName.text()
        self.parent.onCreateNewProject(projPath)
        self.close() 

    def browseProjectRoot(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode( QtWidgets.QFileDialog.Directory )
        path = Path(self.labelProjectRoot.text())
        if path.exists():
            dlg.setDirectory(str(path))

        if dlg.exec_():
            folder = dlg.selectedFiles()
            if len(folder) > 0:
                self.labelProjectRoot.setText(Path(folder[0]).as_posix())
                self.parent.defaultNewProjectRoot = Path(folder[0]).as_posix()

def _getProjectManagerWidget():
    pmUI = ProjectManagerUI()
    return pmUI

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("fusion")
    pmUI = ProjectManagerUI()
    pmUI.show()
    app.exec_()
    