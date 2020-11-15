import os
import project

#Set active project root
#Create folder structure at a location

#Create new asset
#Create new shot


path = os.path.dirname(__file__)
path = os.path.join( path, "TestProj")

project.SetCurrentRootDir(path)

#print(os.getcwd())

