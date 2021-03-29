import hou
import os
import re_project
import re_project_manager

class HoudiniProjectManagerUI( re_project_manager.ProjectManagerUI):
    def __init__(self):
        super().__init__()

    def onClickLoadAsset(self):
        print("ON CLICK LOAD ASSET HOUDINI!!!") 
        hou.hipFile.clear()


def _getProjectManagerWidget():
    pmUI = HoudiniProjectManagerUI()
    return pmUI