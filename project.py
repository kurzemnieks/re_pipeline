import json
import os
import subprocess
import re
from collections import namedtuple
from pathlib import Path


#########################################################################################################

_RE_PROJECT_ROOT = ''
_RE_PROJECT_INITIALIZED = False
_RE_PROJECT_CFG_NAME = '.projcfg'

_RE_PROJECT_VERSION = 1.0
_RE_PROJECT_ASSET_LIB = 'F:/Drive/Assets/Textures'
_RE_PROJECT_DEFAULT_FPS = 30.0
_RE_PROJECT_DEFAULT_REZ = {'x':1920, 'y':1080}

#########################################################################################################

AppConfig = namedtuple('AppConfig',['blender','houdini','c4d','maya','usd'])
_RE_PROJECT_APP_CONFIG = AppConfig(blender=False,houdini=False,c4d=False,maya=False,usd=False)

_RE_PROJECT_HAS_FOOTAGE = False #Project has footage, uses roto, tracking for comp

#########################################################################################################
def set_current_root_dir( path ):
    # Initialize project root folder. 
    # If project exists in this path, it will be loaded and initialized
    
    global _RE_PROJECT_ROOT

    _RE_PROJECT_ROOT = os.path.normpath( path )

    if not _try_load_project(_RE_PROJECT_ROOT):
        print('Info: Project not found at location: ' + _RE_PROJECT_ROOT)
        return False
    else:
        print('Info: Project found at current location')
        return True

def is_project_initialized():
    if not _RE_PROJECT_ROOT:
        return False

    if len(_RE_PROJECT_ROOT)==0:
        return False

    if not os.path.exists(_RE_PROJECT_ROOT):
        return False

    return _RE_PROJECT_INITIALIZED

def get_project_root():
    assert(_RE_PROJECT_INITIALIZED)
    return _RE_PROJECT_ROOT

def get_project_app_config():
    assert(_RE_PROJECT_INITIALIZED)
    return _RE_PROJECT_APP_CONFIG

def get_project_default_rez():
    assert(_RE_PROJECT_INITIALIZED)
    return _RE_PROJECT_DEFAULT_REZ

def get_project_default_fps():
    assert(_RE_PROJECT_INITIALIZED)
    return _RE_PROJECT_DEFAULT_FPS

def get_project_ext_asset_lib():
    assert(_RE_PROJECT_INITIALIZED)
    return _RE_PROJECT_ASSET_LIB    

#########################################################################################################
# internals
#########################################################################################################

def _try_load_project( path ):
    
    global _RE_PROJECT_ASSET_LIB
    global _RE_PROJECT_APP_CONFIG
    global _RE_PROJECT_DEFAULT_FPS
    global _RE_PROJECT_DEFAULT_REZ
    global _RE_PROJECT_INITIALIZED

    cfg_file_path = os.path.join(path, _RE_PROJECT_CFG_NAME)

    if os.path.isfile( cfg_file_path ):
        
        with open(cfg_file_path) as inCfgFile:
            
            project_cfg = json.load(inCfgFile)

            if _RE_PROJECT_VERSION != project_cfg['version']:
                raise ValueError('Project version does not match! Need {}, got {}'.format(_RE_PROJECT_VERSION, project_cfg['version']))

            _RE_PROJECT_ASSET_LIB = "" 
            _RE_PROJECT_ASSET_LIB = project_cfg['ext_lib']
            if not os.path.exists(_RE_PROJECT_ASSET_LIB):
                print('Error: ' + _RE_PROJECT_ASSET_LIB + ' external asset library path does not exist!')

            _RE_PROJECT_DEFAULT_FPS = project_cfg['fps']
            _RE_PROJECT_DEFAULT_REZ = project_cfg['rez']

            apps_cfg = project_cfg['apps']
            _RE_PROJECT_APP_CONFIG = AppConfig( **apps_cfg )

            _RE_PROJECT_INITIALIZED = True
        return True

    else:
        return False
    
def _get_project_folder_struct():

    """ Return master project folder structure.
    """

    #shared assets between shots
    ASSETS = [
        ['2d',[
            ['artworks', []],
            ['footage',[],None, _RE_PROJECT_HAS_FOOTAGE],
            ['roto',[],None, _RE_PROJECT_HAS_FOOTAGE],
            ['tracking',[],None, _RE_PROJECT_HAS_FOOTAGE],
            ]            
        ],
        ['3d',[
            ['fbx',[]],
            ['abc',[]],
            ['obj',[]],
            ['blend',[],None, _RE_PROJECT_APP_CONFIG.blender],
            ['hda',[],None, _RE_PROJECT_APP_CONFIG.houdini],
            ['c4d',[],None, _RE_PROJECT_APP_CONFIG.c4d],
            ['usd',[],None, _RE_PROJECT_APP_CONFIG.usd],
            ]
        ],
        ['tex',[
            ['library',[],_RE_PROJECT_ASSET_LIB, len(_RE_PROJECT_ASSET_LIB)>0]
        ]
        ],
        ['lib',[]
        ]        
    ]

    #folder where assets are being built
    BUILD = [
    ]

    #shot assembly folder
    SHOTS = [

    ]

    #render outputs (sequences)
    RENDER = [
        ['previs',[]
        ],
        ['shots', []
        ]
    ]

    #movies, screenshots, images (valuable and final outputs)
    OUT = [
        ['previs',[]],
        ['review',[]],
        ['images',[]],
        ['deliver',[]]
    ]

    #caches, temp sequences - stuff that can be deleted during cleanup/archiving
    TEMP = [
        ['assets',[]],
        ['shots',[]]
    ]

    #Combine in one structure
    FOLDERS = [
        ['assets',ASSETS],
        ['build',BUILD],
        ['shots',SHOTS],
        ['render',RENDER],
        ['out',OUT],
        ['temp',TEMP]
    ]

    return FOLDERS


def _create_project_folders( path="", template=[], create_missing_links=False ):    
    if not template:
        return False

    for folder in template:
        folder_name = folder[0]

        folder_link_target = None
        folder_bool = True

        if len(folder)>2:
            folder_link_target = folder[2] #if this is valid string, this will be a symlink to this path
        if len(folder)>3:
            folder_bool = folder[3] #use 4th param as optional bool - so we can create some folders based on configuration

        if folder_bool:
            #folder_path = '{}/{}'.format(path, folder_name)
            folder_path = os.path.join(path, folder_name)

            #if isinstance(folder_link_target, bool):
            #    print(folder)

            if folder_link_target and len(folder_link_target)==0:
                folder_link_target = None

            if folder_link_target:

                #create symlink 
                if not os.path.exists(folder_path):
                    
                    #make sure target folder exists
                    print(_RE_PROJECT_ROOT)
                    symlink_target = os.path.join(_RE_PROJECT_ROOT, folder_link_target)
                    symlink_target = os.path.normpath(symlink_target.lower())
                    
                    #calculate relative path
                    symlink_rel_target = os.path.relpath(symlink_target, folder_path)
                    if symlink_rel_target.startswith("..\\"):
                        symlink_rel_target = symlink_rel_target[3:]

                    print("Link: " + folder_path + " ==> " + symlink_target + " ==> " + symlink_rel_target)

                    if not os.path.exists(symlink_target) and create_missing_links:
                        os.makedirs(symlink_target)                        
                    
                    if os.path.exists(symlink_target):
                        old_cwd = os.getcwd()
                        os.chdir(path)                                        
                        with open(os.devnull, "w") as FNULL:
                            subprocess.check_call('mklink /D {} {}'.format(folder_name, symlink_rel_target), shell=True, stdout=FNULL)
                        os.chdir(old_cwd)
                    else:
                        raise ValueError("Can't create symlink. Dest path does not exist: " + symlink_target)

            else:
                #create regular folder
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
            
            _create_project_folders(folder_path, folder[1], create_missing_links)

    return True


################################################################################
def create_project(app_config):
    # Try creating new project at current root location
    # app_config: AppConfig configure which applications will be used in project
    #             Appropriate subfolders will be created. 

    global _RE_PROJECT_APP_CONFIG
    global _RE_PROJECT_INITIALIZED
    _RE_PROJECT_APP_CONFIG = app_config
    
    if not os.path.exists(_RE_PROJECT_ROOT):
        os.makedirs(_RE_PROJECT_ROOT)

    project_cfg = {}
    project_cfg['version'] = _RE_PROJECT_VERSION
    project_cfg['ext_lib'] = _RE_PROJECT_ASSET_LIB
    project_cfg['apps'] = _RE_PROJECT_APP_CONFIG._asdict()
    project_cfg['fps'] = _RE_PROJECT_DEFAULT_FPS
    project_cfg['rez'] = _RE_PROJECT_DEFAULT_REZ

    if os.path.exists(_RE_PROJECT_ROOT):
        cfg_file_path = os.path.join( _RE_PROJECT_ROOT, _RE_PROJECT_CFG_NAME)
        with open(cfg_file_path, 'w') as outCfgFile:
            json.dump(project_cfg, outCfgFile, indent=4, sort_keys=True)

        print('Project config created..')
        _RE_PROJECT_INITIALIZED = True
        return True
    else:
        return False

def create_project_folders():
    # Create project folder structure based on configuration
    # Use this also to generate new folders if the configuration changes
    return _create_project_folders(_RE_PROJECT_ROOT, _get_project_folder_struct())    


def update_project_app_config(app_config):
    if not _RE_PROJECT_INITIALIZED:
        raise ValueError("Project not initialized")
        return

    global _RE_PROJECT_APP_CONFIG
    _RE_PROJECT_APP_CONFIG = app_config    

    create_project_folders()

def asset_exists( assetName ):
    assert(_RE_PROJECT_INITIALIZED)
    assetName = assetName.lower()
    asset_root = os.path.join(_RE_PROJECT_ROOT, 'build')
    asset_folder = os.path.join( asset_root, assetName)
    asset_folder = os.path.normpath(asset_folder)
    return os.path.exists(asset_folder)

def create_asset_folders( assetName ):
    assert(_RE_PROJECT_INITIALIZED)
    if not _RE_PROJECT_INITIALIZED:
        raise ValueError("Project not initialized")
        return False

    # Add new asset under build. Generates necessary folders and symlinks. 
    assetName = assetName.lower()
    asset_root = os.path.join(_RE_PROJECT_ROOT, 'build')
    asset_folder = os.path.join( asset_root, assetName)
    asset_folder = os.path.normpath(asset_folder)

    if os.path.exists(asset_folder):
        print("Warning: Asset already exists. Generating missing folders")
    else:
        os.makedirs(asset_folder)

    ASSET_FOLDERS = _get_app_folders( "assets", assetName )

    OTHER = [
        ['tex',[],'assets/tex'],
        ['fbx',[],'assets/3d/fbx'],
        ['usd',[],'assets/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['abc',[],'assets/3d/abc'],
        ['render',[],'render/assets/' + assetName],
        ['tmp',[],'temp/assets/{}'.format(assetName)],
        ['lib',[],'assets/lib']
    ]

    TEXTURES = [
        ['tex',[],'assets/tex']
    ]

    ASSET_FOLDERS.append(['other', OTHER])
    ASSET_FOLDERS.append(['textures',TEXTURES])
    
    return _create_project_folders(asset_folder, ASSET_FOLDERS, True)


def get_shot_name( sequence, shot_number ):
    assert(_RE_PROJECT_INITIALIZED)
    shot_name = "shot_{}{}".format(str(sequence), str(shot_number).zfill(2))
    shot_name = shot_name.lower()
    return shot_name

def get_shot_path(sequence, shot_number):
    assert(_RE_PROJECT_INITIALIZED)
    shot_path = os.path.join( _RE_PROJECT_ROOT, "shots" )
    shot_path = os.path.join( shot_path, get_shot_name(sequence, shot_number) )
    shot_path = os.path.normpath(shot_path)
    return shot_path

def shot_exists( sequence, shot_number ):
    assert(_RE_PROJECT_INITIALIZED)
    return os.path.exists( get_shot_path(sequence, shot_number) )

def create_shot( sequence, shot_number):  
    assert(_RE_PROJECT_INITIALIZED)  
    shot_name = get_shot_name( sequence, shot_number)
    shot_path = get_shot_path(sequence, shot_number)

    if os.path.exists(shot_path):
        print("Warning: Shot already exists. Generating missing folders")
    else:
        os.makedirs(shot_path)

    SHOT_FOLDERS = _get_app_folders( "shots", shot_name )

    COMP = [
        ['previs',[],'render/previs/{}'.format(shot_name)],
        ['render',[],'render/shots/{}'.format(shot_name)],        
        ['out',[],'out'],
        ['artworks',[],'assets/2d/artworks'],
        ['footage',[],'assets/2d/footage/{}'.format(shot_name), _RE_PROJECT_HAS_FOOTAGE],
        ['roto',[],'assets/2d/roto/{}'.format(shot_name), _RE_PROJECT_HAS_FOOTAGE],
        ['tracking',[],'assets/2d/roto/{}'.format(shot_name), _RE_PROJECT_HAS_FOOTAGE],
    ]

    SHOT_FOLDERS.append(['comp', COMP])    
    
    return _create_project_folders(shot_path, SHOT_FOLDERS, True)
############################################################

def scan_project_assets():
    assert(_RE_PROJECT_INITIALIZED)
    build_root = os.path.join( _RE_PROJECT_ROOT, "build" )
    build_root = os.path.normpath(build_root)

    all_dirs = os.listdir(build_root)    

    return all_dirs

def scan_project_shots():
    assert(_RE_PROJECT_INITIALIZED)
    shots_root = os.path.join( _RE_PROJECT_ROOT, "shots" )
    shots_root = os.path.normpath(shots_root)

    all_dirs = os.listdir(shots_root)
    shot_dirs = [dir for dir in all_dirs if re.match(r"shot_\d{3}d?", dir)] 

    return shot_dirs
    

############################################################

def _get_app_folders( category, name ):
    """ Return folder structures for DCC applications based
        on project app config.
        Used in asset and shot structures. 
    """

    HOUDINI = [
        ['geo',[],'temp/{}/{}/geo'.format(category, name)],
        ['hda',[],'assets/3d/hda'],
        ['fbx',[],'assets/3d/fbx'],
        ['usd',[],'assets/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['sim',[],'temp/{}/{}/sim'.format(category, name)],
        ['abc',[],'assets/3d/abc'],
        ['tex',[],'assets/tex'],

        ['render',[],'render/{}/{}'.format(category, name)],
        ['flip',[],'temp/{}/{}/flip'.format(category, name)],

        ['scripts',[]],
        ['lib',[],'assets/lib']
    ]

    BLENDER = [
        ['tex',[],'assets/tex'],
        ['fbx',[],'assets/3d/fbx'],
        ['usd',[],'assets/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['abc',[],'assets/3d/abc'],
        ['render',[],'render/{}/{}'.format(category, name)],
        ['tmp',[],'temp/{}/{}'.format(category, name)],
        ['lib',[],'assets/lib']
    ]

    C4D = [
        ['tex',[],'assets/tex'],
        ['fbx',[],'assets/3d/fbx'],
        ['usd',[],'assets/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['abc',[],'assets/3d/abc'],
        ['render',[],'render/{}/{}'.format(category, name)],
        ['tmp',[],'temp/{}/{}'.format(category, name)],
        ['lib',[],'assets/lib']
    ]

    MAYA = [
        ['scenes',[]],
        ['clips',[]],
        ['sourceimages',[],'assets/tex'],
        ['fbx',[],'assets/3d/fbx'],
        ['usd',[],'assets/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['abc',[],'assets/3d/abc'],
        ['image',[],'render/{}/{}'.format(category, name)],
        ['movies',[],'render/{}/{}/playblast'.format(category, name)],
        ['data',[],'temp/{}/{}'.format(category, name)],
        ['lib',[],'assets/lib'],
        ['scripts',[]],
    ]

    FOLDERS = [
        ['houdini', HOUDINI, None, _RE_PROJECT_APP_CONFIG.houdini],
        ['blender', BLENDER, None, _RE_PROJECT_APP_CONFIG.blender],
        ['c4d', C4D, None, _RE_PROJECT_APP_CONFIG.c4d],
        ['maya', MAYA, None, _RE_PROJECT_APP_CONFIG.maya]
    ]

    return FOLDERS

