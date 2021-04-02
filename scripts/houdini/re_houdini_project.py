import hou
import os
import re_project
import re_project_manager

class HoudiniProjectManagerUI( re_project_manager.ProjectManagerUI):
    def __init__(self):
        super().__init__()

    def onClickLoadAsset(self):        
        hou.hipFile.clear()
        item = self.assetList.selectedItems()[0]        
        asset_path = re_project.get_asset_path(item.text())
        asset_path = asset_path / "houdini"
        hou.putenv("JOB", asset_path.as_posix())
        hou.putenv("HIP", asset_path.as_posix())

        hip_path = asset_path / "untitled.hip"
        hou.putenv("HIPFILE", hip_path.as_posix())

        temp_path = asset_path / "tmp"
        hou.putenv("TEMP", temp_path.as_posix())

    def onClickLoadShot(self):
        hou.hipFile.clear()
        item = self.shotsList.selectedItems()[0]        
        shot_path = re_project.get_shot_path(re_project.get_shot_data_from_name(item.text()))
        shot_path = shot_path / "houdini"
        hou.putenv("JOB", shot_path.as_posix())
        hou.putenv("HIP", shot_path.as_posix())

        hip_path = shot_path / "untitled.hip"
        hou.putenv("HIPFILE", hip_path.as_posix())

        temp_path = shot_path / "tmp"
        hou.putenv("TEMP", temp_path.as_posix())


def _getProjectManagerWidget():
    pmUI = HoudiniProjectManagerUI()
    return pmUI