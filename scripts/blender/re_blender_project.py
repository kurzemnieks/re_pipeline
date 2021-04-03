import sys

my_python_path = "C:/Users/gatis/AppData/Local/Programs/Python/Python39/Lib/site-packages"
sys.path.insert(0, my_python_path)
import PySide2


import os
import re_project
import re_project_manager

from PySide2 import QtWidgets


class BlenderProjectManagerUI( re_project_manager.ProjectManagerUI):
    def __init__(self):
        super().__init__()
        self.show()

    def onClickLoadAsset(self):                
        item = self.assetList.selectedItems()[0]        
        asset_path = re_project.get_asset_path(item.text())
        asset_path = asset_path / "blender"

    def onClickLoadShot(self):    
        item = self.shotsList.selectedItems()[0]        
        shot_path = re_project.get_shot_path(re_project.get_shot_data_from_name(item.text()))
        shot_path = shot_path / "blender"

#if __name__ == "__main__":
#    app = QtWidgets.QApplication([])
#    app.setStyle("fusion")
#    pmUI = BlenderProjectManagerUI()
#    pmUI.show()
#    app.exec_()
    