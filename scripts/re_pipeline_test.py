import os
import re_project

#Set active project root
#Create folder structure at a location

#Create new asset
#Create new shot


path = os.path.dirname(__file__)
path = os.path.join( path, "TestProj")

appConfig = re_project.ProjectFeatures(blender=True, houdini=True, maya = False, c4d = True, usd = True)
#appConfig = project.AppConfig(blender=False, houdini=False, maya = False, c4d = False, usd = False)

result = re_project.set_project_root_folder(path)
if not result:
    re_project.create_project(appConfig)
    re_project.create_project_folders()

re_project.update_project_features_config( appConfig )
re_project.create_asset_folders("Env_Lab")
re_project.create_shot(1,2)
re_project.create_shot(1,3)

print(re_project.scan_project_assets())