import sys

#REPLACE THIS WITH YOUR OWN PATH or install PySide2 directly into blender folder
#my_python_path = "C:/Users/gatis/AppData/Local/Programs/Python/Python39/Lib/site-packages"
#sys.path.insert(0, my_python_path)

from PySide2 import QtWidgets, QtCore

import bpy

import re_project
from blender.qtutils import QtWindowEventLoop
from blender import re_blender_project

class CustomWindowOperator(QtWindowEventLoop):
    bl_idname = 'screen.re_project_manager'
    bl_label = 'RE Project Manager'

    def __init__(self):
        super().__init__(re_blender_project.BlenderProjectManagerUI)
                


bpy.utils.register_class(CustomWindowOperator)
bpy.ops.screen.re_project_manager()



