import hou
import os
import re_project
import re_project_manager

from PySide2 import QtWidgets
from pathlib import Path
class HoudiniProjectManagerUI( re_project_manager.ProjectManagerUI):
    def __init__(self):
        super().__init__()
        self.sceneDCCExtensions = ["*.hip", "*.hiplc", "*.hipnc"]

    def onClickLoadAsset(self):        
        hou.hipFile.clear()
        self._activateCurrentAsset()

    def onClickLoadShot(self):
        hou.hipFile.clear()
        self._activateCurrentShot()

    def onOpenAssetFileClick(self):
        if hou.hipFile.isLoadingHipFile():
            return

        asset_file = Path(self.assetFileList.selectedItems()[0].text(0))
        asset_item = self.assetList.selectedItems()[0].text()
        asset_path : Path = re_project.get_asset_path(asset_item)
        asset_path = asset_path / re_project._RE_DCC_APP
        asset_file = asset_path / asset_file
        
        if asset_file.exists():
            hou.hipFile.load(asset_file.as_posix())        
            self._activateCurrentAsset()

    def onNewAssetFileClick(self):
        if hou.hipFile.isLoadingHipFile():
            return

        self._checkFileNeedsSave()

        hou.hipFile.clear()

        self.newFileDialog.setTitle("New Houdini Scene")
        self.newFileDialog.setQuestion("File name:")
        self.newFileDialog.setCreateCallback(self._onNewHoudiniFile)

        asset_item = self.assetList.selectedItems()[0].text()        
        asset_path : Path = re_project.get_asset_path(asset_item)
        dcc_asset_path = asset_path / re_project._RE_DCC_APP  
        self.newFileDialog.setBasePath(dcc_asset_path.as_posix())
        self.newFileDialog.exec_()
        
        self._activateCurrentAsset()
        self.UpdateFileList(asset_path, self.assetFileList)


    def onOpenShotFileClick(self):
        if hou.hipFile.isLoadingHipFile():
            return

        shot_file = Path(self.shotFileList.selectedItems()[0].text(0))
        shot_item = self.shotsList.selectedItems()[0].text()
        shot_data = re_project.get_shot_data_from_name(shot_item)    
        shot_path : Path = re_project.get_shot_path(shot_data[0], shot_data[1])
        shot_path = shot_path / re_project._RE_DCC_APP
        shot_file = shot_path / shot_file
        if shot_file.exists():
            hou.hipFile.load(shot_file.as_posix())
            self._activateCurrentShot()

    def onNewShotFileClick(self):
        if hou.hipFile.isLoadingHipFile():
            return

        self._checkFileNeedsSave()

        self.newFileDialog.setTitle("New Houdini Scene")
        self.newFileDialog.setQuestion("File name:")
        self.newFileDialog.setCreateCallback(self._onNewHoudiniFile)

        shot_item = self.shotsList.selectedItems()[0].text()   
        shot_data = re_project.get_shot_data_from_name(shot_item)    
        shot_path : Path = re_project.get_shot_path(shot_data[0], shot_data[1])
        dcc_shot_path = shot_path / re_project._RE_DCC_APP  
        self.newFileDialog.setBasePath(dcc_shot_path.as_posix())

        self.newFileDialog.exec_()

        self._activateCurrentShot()
        self.UpdateFileList(shot_path, self.shotFileList)
        
#############################################################################################################################################################################################
    def getExtension() -> str:
        if hou.licenseCategory() == hou.licenseCategoryType.Indie:
            return ".hiplc"
        if hou.licenseCategory() == hou.licenseCategoryType.Commercial:
            return ".hip"
        if hou.licenseCategory() == hou.licenseCategoryType.Apprentice:
            return ".hipnc"
        return ".hipnc"
    
    def _activateCurrentAsset(self):
        item = self.assetList.selectedItems()[0]        
        asset_path = re_project.get_asset_path(item.text())
        asset_path = asset_path / "houdini"

        if hou.getenv("JOB") != asset_path.as_posix():
            hou.putenv("JOB", asset_path.as_posix())
        if hou.getenv("HIP") != asset_path.as_posix():            
            hou.putenv("HIP", asset_path.as_posix())
        
        #hip_path = Path(hou.hipFile.path())
        #hou.putenv("HIPFILE", hip_path.as_posix())
        #         
        temp_path = asset_path / "tmp"
        if hou.getenv("TEMP") != temp_path.as_posix(): 
            hou.putenv("TEMP", temp_path.as_posix())        

    def _activateCurrentShot(self):
        item = self.shotsList.selectedItems()[0]  
        shot_data = re_project.get_shot_data_from_name(item.text())
        shot_path = re_project.get_shot_path(shot_data[0], shot_data[1])
        shot_path = shot_path / "houdini"

        if hou.getenv("JOB") != shot_path.as_posix():
            hou.putenv("JOB", shot_path.as_posix())
        if hou.getenv("HIP") != shot_path.as_posix(): 
            hou.putenv("HIP", shot_path.as_posix())

        #hip_path = Path(hou.hipFile.path())
        #hou.putenv("HIPFILE", hip_path.as_posix())
        temp_path = shot_path / "tmp"
        if hou.getenv("TEMP") != temp_path.as_posix(): 
            hou.putenv("TEMP", temp_path.as_posix())

    def _checkFileNeedsSave(self):
        if hou.hipFile.hasUnsavedChanges() and hou.hipFile.name() != 'untitled.hip':
            hou.hipFile.save()

    def _onNewHoudiniFile(self, name:str):
        default_ext = HoudiniProjectManagerUI.getExtension()
        if not name.lower().endswith(default_ext):
            name = name + default_ext
        
        new_file_name = Path(name)

        if new_file_name.exists():
            QtWidgets.QMessageBox.question(self, "File already exists!", "File with this name already exists!", QtWidgets.QMessageBox.Ok)
        else:            
            hou.hipFile.clear()
            hou.hipFile.setName(new_file_name.as_posix())

            hou.hscript("set -g HRES={}".format(re_project.get_project_default_rez()['x']))
            hou.hscript("set -g VRES={}".format(re_project.get_project_default_rez()['y']))
            #hou.hscript("set -g FPS={}".format(re_project.get_project_default_fps()))
            hou.setFps(re_project.get_project_default_fps())

            hou.hipFile.save()
            self.statusBar.showMessage("New Houdini file {} created".format(new_file_name.name))




def _getProjectManagerWidget():
    pmUI = HoudiniProjectManagerUI()
    return pmUI