import json
import os

_RE_PROJECT_ROOT = ""
_RE_PROJECT_CFG_NAME = ".projcfg"

_RE_PROJECT_VERSION = 1.0
_RE_EXT_ASSET_LIB = "F:/Drive/Assets"

def SetCurrentRootDir( path ):

    _RE_PROJECT_ROOT = os.path.normpath( path )

    if not TryLoadProject(_RE_PROJECT_ROOT):
        if not CreateProject( _RE_PROJECT_ROOT ):
            print("Can't create project folder!")
            return
    pass


def TryLoadProject( path ):
    cfg_file_path = os.path.join(path, _RE_PROJECT_CFG_NAME)

    if os.path.isfile( cfg_file_path ):

        print("Project config found..")
        
        with open(cfg_file_path) as inCfgFile:
            project_cfg = json.load(inCfgFile)
            _RE_EXT_ASSET_LIB = project_cfg['ext_lib']
            if not os.path.exists(_RE_EXT_ASSET_LIB):
                print("Error: " + _RE_EXT_ASSET_LIB + " external asset library path does not exist!")

        return True

    else:
        return False
    

def CreateProject( path ):
    if not os.path.exists(path):
        os.makedirs(path)

    project_cfg = {}
    project_cfg['version'] = _RE_PROJECT_VERSION
    project_cfg['ext_lib'] = _RE_EXT_ASSET_LIB

    if os.path.exists(path):
        cfg_file_path = os.path.join( path, _RE_PROJECT_CFG_NAME)
        with open(cfg_file_path, 'w') as outCfgFile:
            json.dump(project_cfg, outCfgFile, indent=4)

        print("Project config created..")
        return True
    else:
        return False

def GenerateFolderStructure( path ):
    pass


def AddNewAsset( assetName, path ):
    pass