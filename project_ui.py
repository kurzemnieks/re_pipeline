import sys
import project

from Qt import QtWidgets, QtCore, QtGui
from ui import projman

class ProjectManagerUI( QtWidgets.QMainWindow, projman.Ui_MainWindow ):
    def __init__(self):
        super(ProjectManagerUI, self).__init__()
        self.setupUi(self)

        self.updateAppConfig()

        self.editHRes.setValidator( QtGui.QIntValidator(1, 32000))        
        self.editVRes.setValidator( QtGui.QIntValidator(1, 32000))        
        self.editFPS.setValidator( QtGui.QDoubleValidator(1.0, 500.0, 3))

        self.setRootButton.clicked.connect(self.setProjectRoot)

    def setProjectRoot(self):

        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode( QtWidgets.QFileDialog.Directory )
        if dlg.exec_():
            folder = dlg.selectedFiles()
            if len(folder) > 0:
                result = project.set_current_root_dir(folder[0])
                if not result:
                    self.updateAppConfig()
                    project.create_project(self.appConfig)
                    project.create_project_folders()
                else:
                    self.onProjectLoaded()

                self.projectRootLabel.setText(project.get_project_root())


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
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("fusion")
    pmUI = ProjectManagerUI()
    pmUI.show()
    app.exec_()