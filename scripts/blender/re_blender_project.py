import sys

#TODO FIX THIS SOMEHOW !?
my_python_path = "C:/Users/gatis/AppData/Local/Programs/Python/Python39/Lib/site-packages"
sys.path.insert(0, my_python_path)
import PySide2

import os
import re_project
import re_project_manager
from pathlib import Path

from PySide2 import QtWidgets, QtGui

import bpy


class BlenderProjectManagerUI( re_project_manager.ProjectManagerUI):
    def __init__(self):
        super().__init__()

        self.sceneDCCExtensions = ["*.blend"]
        
        self.loadShotButton.hide()
        self.loadAssetButton.hide()

        self.show()

    def onClickLoadAsset(self):                
        item = self.assetList.selectedItems()[0]        
        asset_path = re_project.get_asset_path(item.text())
        asset_path = asset_path / "blender"
        print("NOT IMPLEMENTED")

    def onClickLoadShot(self):    
        item = self.shotsList.selectedItems()[0]        
        shot_path = re_project.get_shot_path(re_project.get_shot_data_from_name(item.text()))
        shot_path = shot_path / "blender"
        print("NOT IMPLEMENTED")

    def onOpenAssetFileClick(self):
        asset_file = Path(self.assetFileList.selectedItems()[0].text(0))
        asset_item = self.assetList.selectedItems()[0].text()
        asset_path : Path = re_project.get_asset_path(asset_item)
        asset_path = asset_path / re_project._RE_DCC_APP
        asset_file = asset_path / asset_file
        if asset_file.exists():
            self._openBlenderFile(asset_file.as_posix())

    def onNewAssetFileClick(self):
        self._checkFileNeedsSave()

        self.newFileDialog.setTitle("New Blender Scene")
        self.newFileDialog.setQuestion("File name:")
        self.newFileDialog.setCreateCallback(self._onNewBlenderFile)

        asset_item = self.assetList.selectedItems()[0].text()        
        asset_path : Path = re_project.get_asset_path(asset_item)
        dcc_asset_path = asset_path / re_project._RE_DCC_APP  
        self.newFileDialog.setBasePath(dcc_asset_path.as_posix())
        self.newFileDialog.exec_()
        
        self.UpdateFileList(asset_path, self.assetFileList)


    def onOpenShotFileClick(self):
        shot_file = Path(self.shotFileList.selectedItems()[0].text(0))
        shot_item = self.shotsList.selectedItems()[0].text()
        shot_data = re_project.get_shot_data_from_name(shot_item)    
        shot_path : Path = re_project.get_shot_path(shot_data[0], shot_data[1])
        shot_path = shot_path / re_project._RE_DCC_APP
        shot_file = shot_path / shot_file
        if shot_file.exists():
            self._openBlenderFile(shot_file.as_posix())

    def onNewShotFileClick(self):
        self._checkFileNeedsSave()

        self.newFileDialog.setTitle("New Blender Scene")
        self.newFileDialog.setQuestion("File name:")
        self.newFileDialog.setCreateCallback(self._onNewBlenderFile)

        shot_item = self.shotsList.selectedItems()[0].text()   
        shot_data = re_project.get_shot_data_from_name(shot_item)    
        shot_path : Path = re_project.get_shot_path(shot_data[0], shot_data[1])
        dcc_shot_path = shot_path / re_project._RE_DCC_APP  
        self.newFileDialog.setBasePath(dcc_shot_path.as_posix())

        self.newFileDialog.exec_()
        self.UpdateFileList(shot_path, self.shotFileList)
#############################################################################################################################################################################################
    def _onNewBlenderFile(self, name:str):
        if not name.lower().endswith(".blend"):
            name = name + ".blend"
        
        new_file_name = Path(name)

        if new_file_name.exists():
            QtWidgets.QMessageBox.question(self, "File already exists!", "File with this name already exists!", QtWidgets.QMessageBox.Ok)
        else:
            bpy.ops.wm.read_homefile(app_template="") 
            bpy.ops.wm.save_as_mainfile(filepath=new_file_name.as_posix())             
            self.statusBar.showMessage("New Blender file {} created".format(new_file_name.name))
    
    def _openBlenderFile(self, file_name:str):
        if bpy.data.is_saved and bpy.data.is_dirty:
            ret = QtWidgets.QMessageBox.question(self, "Save Changes?", "Current file has unsaved changes! Save before opening new file?", QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            if ret == QtWidgets.QMessageBox.Yes:
                bpy.ops.wm.save_mainfile()
        bpy.ops.wm.open_mainfile(filepath=file_name)
        self.statusBar.showMessage("Blender file {} opened".format(Path(file_name).name))

    def _checkFileNeedsSave(self):
        if bpy.data.is_saved and bpy.data.is_dirty:
            ret = QtWidgets.QMessageBox.question(self, "Save Changes?", "Current file has unsaved changes! Save before opening new file?", QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            if ret == QtWidgets.QMessageBox.Yes:
                bpy.ops.wm.save_mainfile()
