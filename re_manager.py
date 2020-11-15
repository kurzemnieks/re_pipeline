import os
import project

#Set active project root
#Create folder structure at a location

#Create new asset
#Create new shot


path = os.path.dirname(__file__)
path = os.path.join( path, "TestProj")

appConfig = project.AppConfig(blender=True, houdini=True, maya = False, c4d = True, usd = True)
#appConfig = project.AppConfig(blender=False, houdini=False, maya = False, c4d = False, usd = False)

result = project.set_current_root_dir(path)
if not result:
    project.create_project(appConfig)
    project.create_project_folders()

project.update_project_app_config( appConfig )
project.create_asset_folders("Env_Lab")
project.create_shot(1,2)