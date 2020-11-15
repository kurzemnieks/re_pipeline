import json
import os
import subprocess
from collections import namedtuple


#########################################################################################################

_RE_PROJECT_ROOT = ''
_RE_PROJECT_INITIALIZED = False
_RE_PROJECT_CFG_NAME = '.projcfg'

_RE_PROJECT_VERSION = 1.0
_RE_PROJECT_ASSET_LIB = 'F:/Drive/Assets'
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

    SHARED = [
        ['2d',[
            ['artworks', []],
            ['footage',[],'shared/2d/footage', _RE_PROJECT_HAS_FOOTAGE],
            ['roto',[],'shared/2d/roto', _RE_PROJECT_HAS_FOOTAGE],
            ['tracking',[],'shared/2d/roto', _RE_PROJECT_HAS_FOOTAGE],
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
        ['tex',[]
        ],
        ['lib',[]
        ]        
    ]

    BUILD = [
    ]


    SHOTS = [

    ]

    RENDER = [
        ['previs',[]
        ],
        ['shots', []
        ]
    ]

    OUT = [
        ['previs',[]],
        ['review',[]],
        ['images',[]],
        ['deliver',[]]
    ]

    TEMP = [
        ['shared',[]],
        ['shots',[]]
    ]

    #Combine in one structure
    FOLDERS = [
        ['shared',SHARED],
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

            if folder_link_target and len(folder_link_target)==0:
                folder_link_target = None

            if folder_link_target:

                #create symlink 
                if not os.path.exists(folder_path):
                    
                    #make sure target folder exists
                    symlink_target = os.path.join(_RE_PROJECT_ROOT, folder_link_target)
                    symlink_target = os.path.normpath(symlink_target.lower())
                    if not os.path.exists(symlink_target) and create_missing_links:
                        os.makedirs(symlink_target)
                    
                    if os.path.exists(symlink_target):                                        
                        with open(os.devnull, "w") as FNULL:
                            subprocess.check_call('mklink /D {} {}'.format(folder_path, symlink_target), shell=True, stdout=FNULL)
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
    _create_project_folders(_RE_PROJECT_ROOT, _get_project_folder_struct())    


def update_project_app_config(app_config):
    if not _RE_PROJECT_INITIALIZED:
        raise ValueError("Project not initialized")
        return

    global _RE_PROJECT_APP_CONFIG
    _RE_PROJECT_APP_CONFIG = app_config    

    create_project_folders()

def asset_exists( assetName ):
    assetName = assetName.lower()
    asset_root = os.path.join(_RE_PROJECT_ROOT, 'build')
    asset_folder = os.path.join( asset_root, assetName)
    asset_folder = os.path.normpath(asset_folder)
    return os.path.exists(asset_folder)

def create_asset_folders( assetName ):

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

    ASSET_FOLDERS = _get_app_folders( "asset", assetName )

    OTHER = [
        ['tex',[],'shared/tex'],
        ['fbx',[],'shared/3d/fbx'],
        ['usd',[],'shared/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['abc',[],'shared/3d/abc'],
        ['render',[],'render/assets/' + assetName],
        ['tmp',[],'temp/assets/{}'.format(assetName)],
        ['lib',[],'shared/lib']
    ]

    TEXTURES = [
        ['tex',[],'shared/tex']
    ]

    ASSET_FOLDERS.append(['other', OTHER])
    ASSET_FOLDERS.append(['textures',TEXTURES])
    
    _create_project_folders(asset_folder, ASSET_FOLDERS, True)


def get_shot_name( sequence, shot_number ):
    shot_name = "shot_{}{}".format(str(sequence), str(shot_number).zfill(2))
    shot_name = shot_name.lower()
    return shot_name

def get_shot_path(sequence, shot_number):
    shot_path = os.path.join( _RE_PROJECT_ROOT, "shots" )
    shot_path = os.path.join( shot_path, get_shot_name(sequence, shot_number) )
    shot_path = os.path.normpath(shot_path)
    return shot_path

def shot_exists( sequence, shot_number ):
    return os.path.exists( get_shot_path(sequence, shot_number) )

def create_shot( sequence, shot_number):    
    shot_name = get_shot_name( sequence, shot_number)
    shot_path = get_shot_path(sequence, shot_number)

    if os.path.exists(shot_path):
        print("Warning: Shot already exists. Generating missing folders")
    else:
        os.makedirs(shot_path)

    SHOT_FOLDERS = _get_app_folders( "shot", shot_name )

    COMP = [
        ['previs',[],'render/previs/{}'.format(shot_name)],
        ['render',[],'render/shots/{}'.format(shot_name)],        
        ['out',[],'out'],
        ['artworks',[],'shared/2d/artworks'],
        ['footage',[],'shared/2d/footage/{}'.format(shot_name), _RE_PROJECT_HAS_FOOTAGE],
        ['roto',[],'shared/2d/roto/{}'.format(shot_name), _RE_PROJECT_HAS_FOOTAGE],
        ['tracking',[],'shared/2d/roto/{}'.format(shot_name), _RE_PROJECT_HAS_FOOTAGE],
    ]

    SHOT_FOLDERS.append(['comp', COMP])    
    
    _create_project_folders(shot_path, SHOT_FOLDERS, True)


############################################################

def _get_app_folders( category, name ):

    HOUDINI = [
        ['geo',[],'temp/{}/{}/geo'.format(category, name)],
        ['hda',[],'shared/3d/hda'],
        ['fbx',[],'shared/3d/fbx'],
        ['usd',[],'shared/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['sim',[],'temp/{}/{}/sim'.format(category, name)],
        ['abc',[],'shared/3d/abc'],
        ['tex',[],'shared/tex'],

        ['render',[],'render/{}/{}'.format(category, name)],
        ['flip',[],'temp/{}/{}/flip'.format(category, name)],

        ['scripts',[]],
        ['lib',[],'shared/lib']
    ]

    BLENDER = [
        ['tex',[],'shared/tex'],
        ['fbx',[],'shared/3d/fbx'],
        ['usd',[],'shared/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['abc',[],'shared/3d/abc'],
        ['render',[],'render/{}/{}'.format(category, name)],
        ['tmp',[],'temp/{}/{}'.format(category, name)],
        ['lib',[],'shared/lib']
    ]

    C4D = [
        ['tex',[],'shared/tex'],
        ['fbx',[],'shared/3d/fbx'],
        ['usd',[],'shared/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['abc',[],'shared/3d/abc'],
        ['render',[],'render/{}/{}'.format(category, name)],
        ['tmp',[],'temp/{}/{}'.format(category, name)],
        ['lib',[],'shared/lib']
    ]

    MAYA = [
        ['scenes',[]],
        ['clips',[]],
        ['sourceimages',[],'shared/tex'],
        ['fbx',[],'shared/3d/fbx'],
        ['usd',[],'shared/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['abc',[],'shared/3d/abc'],
        ['image',[],'render/{}/{}'.format(category, name)],
        ['movies',[],'render/{}/{}/playblast'.format(category, name)],
        ['data',[],'temp/{}/{}'.format(category, name)],
        ['lib',[],'shared/lib'],
        ['scripts',[]],
    ]

    FOLDERS = [
        ['houdini', HOUDINI, None, _RE_PROJECT_APP_CONFIG.houdini],
        ['blender', BLENDER, None, _RE_PROJECT_APP_CONFIG.blender],
        ['c4d', C4D, None, _RE_PROJECT_APP_CONFIG.c4d],
        ['maya', MAYA, None, _RE_PROJECT_APP_CONFIG.maya]
    ]

    return FOLDERS

