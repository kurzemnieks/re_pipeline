import json
import os
import subprocess
import re
from collections import namedtuple
from pathlib import Path


#########################################################################################################

_RE_PROJECT_ROOT = None
_RE_PROJECT_INITIALIZED = False
_RE_PROJECT_CFG_NAME = '.projcfg'

_RE_PROJECT_VERSION = 1.0
_RE_PROJECT_EXT_TEX_LIB = 'F:/Drive/Assets/Textures'
_RE_PROJECT_DEFAULT_FPS = 30.0
_RE_PROJECT_DEFAULT_REZ = {'x':1920, 'y':1080}

_RE_PROJECT_EXTERNAL_LIBS = []

#########################################################################################################

AppConfig = namedtuple('AppConfig',['blender','houdini','c4d','maya','usd','other'])
_RE_PROJECT_APP_CONFIG = AppConfig(blender=False,houdini=False,c4d=False,maya=False,usd=False,other=False)

_RE_PROJECT_HAS_FOOTAGE = False #Project has footage, uses roto, tracking for comp

#########################################################################################################
def set_current_root_dir( path ):
    # Initialize project root folder. 
    # If project exists in this path, it will be loaded and initialized
    
    global _RE_PROJECT_ROOT

    _RE_PROJECT_ROOT = Path(path)

    if not _try_load_project(_RE_PROJECT_ROOT):
        print('Info: Project not found at location: ' + _RE_PROJECT_ROOT.as_posix())
        return False
    else:
        print('Info: Project found at: ' + _RE_PROJECT_ROOT.as_posix())
        save_project_config()
        return True

def is_project_initialized():
    if not _RE_PROJECT_ROOT:
        return False

    if not _RE_PROJECT_ROOT.exists():
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
    return _RE_PROJECT_EXT_TEX_LIB    

def is_in_houdini():
    if os.getenv("HOUDINI_PATH") is not None:
        return True
    return False

#unitiailize current project
def drop_project():
    global _RE_PROJECT_EXT_TEX_LIB
    global _RE_PROJECT_APP_CONFIG
    global _RE_PROJECT_DEFAULT_FPS
    global _RE_PROJECT_DEFAULT_REZ
    global _RE_PROJECT_INITIALIZED
    global _RE_PROJECT_VERSION
    global _RE_PROJECT_ROOT
    global _RE_PROJECT_HAS_FOOTAGE
    
    #set defaults
    _RE_PROJECT_ROOT = None
    _RE_PROJECT_INITIALIZED = False
    _RE_PROJECT_VERSION = 1.0
    _RE_PROJECT_EXT_TEX_LIB = 'F:/Drive/Assets/Textures'
    _RE_PROJECT_DEFAULT_FPS = 30.0
    _RE_PROJECT_DEFAULT_REZ = {'x':1920, 'y':1080}
    _RE_PROJECT_APP_CONFIG = AppConfig(blender=False,houdini=False,c4d=False,maya=False,usd=False,other=False)
    _RE_PROJECT_HAS_FOOTAGE = False #Project has footage, uses roto, tracking for comp
    
#########################################################################################################
# internals
#########################################################################################################

def _try_load_project( path ):
    
    global _RE_PROJECT_EXT_TEX_LIB
    global _RE_PROJECT_APP_CONFIG
    global _RE_PROJECT_DEFAULT_FPS
    global _RE_PROJECT_DEFAULT_REZ
    global _RE_PROJECT_INITIALIZED
    global _RE_PROJECT_EXTERNAL_LIBS

    if path is None:
        return False

    if not path.exists():
        return False
    
    cfg_file_path = path / _RE_PROJECT_CFG_NAME
    
    if cfg_file_path.is_file():
        
        with open(cfg_file_path) as inCfgFile:
            
            project_cfg = json.load(inCfgFile)

            if _RE_PROJECT_VERSION != project_cfg['version']:
                raise ValueError('Project version does not match! Need {}, got {}'.format(_RE_PROJECT_VERSION, project_cfg['version']))

            #TODO: remove this
            _RE_PROJECT_EXT_TEX_LIB = "" 
            _RE_PROJECT_EXT_TEX_LIB = project_cfg['ext_lib']
                        
            if not os.path.exists(_RE_PROJECT_EXT_TEX_LIB):
                print('Error: ' + _RE_PROJECT_EXT_TEX_LIB + ' external asset library path does not exist!')

            _RE_PROJECT_DEFAULT_FPS = project_cfg['fps']
            _RE_PROJECT_DEFAULT_REZ = project_cfg['rez']

            if 'apps' in project_cfg:
                apps_cfg = project_cfg['apps']
                _RE_PROJECT_APP_CONFIG = AppConfig( **apps_cfg )

            if 'ext_libs' in project_cfg:
                _RE_PROJECT_EXTERNAL_LIBS = project_cfg['ext_libs']
                create_external_lib_folders(_RE_PROJECT_EXTERNAL_LIBS)            

            _RE_PROJECT_INITIALIZED = True
        return True

    else:
        return False
    
def _get_project_folder_struct():

    """ Return master project folder structure.
    [ folder_name, [list_child_templates], symlink_path, bool_create_this, use_absolute_symlink_path]
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
            ['library',[],_RE_PROJECT_EXT_TEX_LIB, len(_RE_PROJECT_EXT_TEX_LIB)>0, True]
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

def _create_project_folders( base_path_str="", template=[], create_missing_links=False, update_symlinks=True ):    
    if not template:
        return False

    for template_item in template:
        folder_name = template_item[0]

        folder_link_target = None
        create_this_folder = True
        absolute_link_paths = False

        if len(template_item)>2:
            folder_link_target = template_item[2] #if this is valid string, this will be a symlink to this path
        if len(template_item)>3:
            create_this_folder = template_item[3] #use 4th param as optional bool - so we can create some folders based on configuration
        if len(template_item)>4:
            absolute_link_paths = template_item[4] #5th param indicates if symlink path should be absolue or relative 

        base_path = Path(base_path_str)

        if create_this_folder:            
            
            new_folder_path = base_path / folder_name
            
            if folder_link_target and len(folder_link_target)==0:
                folder_link_target = None

            if folder_link_target:
                symlink_target = Path(folder_link_target)                
                symlink_rel_target = symlink_target    

                if not absolute_link_paths:
                    symlink_target = _RE_PROJECT_ROOT / folder_link_target                    
                        
                    #calculate relative path
                    try:
                        symlink_rel_target = symlink_target.relative_to( new_folder_path )
                        if symlink_rel_target.startswith("..\\"):
                            symlink_rel_target = Path(symlink_rel_target[3:])
                    except ValueError:
                        symlink_rel_target = symlink_target

                    #print("Link: " + folder_path + " ==> " + symlink_target + " ==> " + symlink_rel_target)
                
                if update_symlinks and new_folder_path.exists() and new_folder_path.is_symlink():
                    old_symlink_target = Path(os.readlink(str(new_folder_path)))
                    if old_symlink_target != symlink_rel_target:
                        print("Re-creating symlink: " + new_folder_path.as_posix() + ": " + old_symlink_target.as_posix() + " ==> " + symlink_rel_target.as_posix())
                        new_folder_path.rmdir()

                #create symlink 
                if not new_folder_path.exists():
                    if not symlink_target.exists() and create_missing_links:
                        symlink_target.mkdir(parents=True)
                    
                    old_cwd = Path.cwd()
                    
                    if symlink_target.exists():                        
                        #This needs Python 3.8 to run on Windows without admin privilegies
                        #new_folder_path.symlink_to(symlink_rel_target, True)

                        os.chdir(base_path_str)                        
                        with open(os.devnull, "w") as FNULL:
                            subprocess.check_call('mklink /D {} {}'.format(folder_name, symlink_rel_target), shell=True, stdout=FNULL)
                    else:
                        raise ValueError("Can't create symlink. Dest path does not exist: " + symlink_target)

                    os.chdir(old_cwd)

            else:
                #create regular folder
                if not new_folder_path.exists():
                    new_folder_path.mkdir(parents=True)
                                
            _create_project_folders(new_folder_path.as_posix(), template_item[1], create_missing_links)

    return True

################################################################################
def create_project(app_config):
    # Try creating new project at current root location
    # app_config: AppConfig configure which applications will be used in project
    #             Appropriate subfolders will be created. 

    global _RE_PROJECT_APP_CONFIG
    global _RE_PROJECT_INITIALIZED
    _RE_PROJECT_APP_CONFIG = app_config
    
    if not _RE_PROJECT_ROOT.exists():
        _RE_PROJECT_ROOT.mkdir(parents=True)

    if _RE_PROJECT_ROOT.exists():
        save_project_config()
        _RE_PROJECT_INITIALIZED = True
        return True
    else:
        return False

def save_project_config():
    global _RE_PROJECT_APP_CONFIG
    project_cfg = {}
    project_cfg['version'] = _RE_PROJECT_VERSION
    project_cfg['ext_lib'] = _RE_PROJECT_EXT_TEX_LIB
    project_cfg['apps'] = _RE_PROJECT_APP_CONFIG._asdict()
    project_cfg['fps'] = _RE_PROJECT_DEFAULT_FPS
    project_cfg['rez'] = _RE_PROJECT_DEFAULT_REZ
    project_cfg['ext_libs'] = _RE_PROJECT_EXTERNAL_LIBS

    try:
        cfg_file_path = _RE_PROJECT_ROOT / _RE_PROJECT_CFG_NAME
        with open(cfg_file_path, 'w') as outCfgFile:
            json.dump(project_cfg, outCfgFile, indent=4, sort_keys=True)
    except IOError:
        print("RE Pipeline error: Can't write project config file to: " + cfg_file_path.as_posix())

def create_project_folders():
    # Create project folder structure based on configuration
    # Use this also to generate new folders if the configuration changes
    return _create_project_folders(_RE_PROJECT_ROOT.as_posix(), _get_project_folder_struct())    

def update_all_asset_folders():
    all_assets = scan_project_assets()

    for asset_name in all_assets:
        if not create_asset_folders(asset_name):
            return False

    return True    

def update_all_shot_folders():
    all_shots = scan_project_shots()

    for shot_name in all_shots:
        shot_id = get_shot_data_from_name(shot_name)
        if not create_shot(shot_id[0], shot_id[1]):
            return False

    return True

#TODO: remove this
def change_external_texture_lib( lib_path ):
    global _RE_PROJECT_EXT_TEX_LIB
    if not os.path.exists(lib_path):
        print("Error: Can't set external tex lib path to non-existing folder:" + lib_path)
        return
    
    _RE_PROJECT_EXT_TEX_LIB = lib_path

    #remove old PROJECT_ROOT/assets/tex/library symlink and create new symlink
    if _create_project_folders(_RE_PROJECT_ROOT, _get_project_folder_struct(), False, True):
        save_project_config()

def update_project_app_config(app_config, generate_folders=False):
    if not _RE_PROJECT_INITIALIZED:
        raise ValueError("Project not initialized")
        return

    global _RE_PROJECT_APP_CONFIG
    _RE_PROJECT_APP_CONFIG = app_config    

    if generate_folders:
        create_project_folders()

def add_external_lib_folder( name, base_path, target ):
    base_folder_path = _RE_PROJECT_ROOT / base_path    
    target_path = Path(target)

    i = is_external_lib(name, base_path, target)
    if i is not None:
        if _RE_PROJECT_EXTERNAL_LIBS[i][2] != target_path.as_posix():
            print("REPLACING EXTERNAL LIB: " + _RE_PROJECT_EXTERNAL_LIBS[i][2] + " with: " + target_path.as_posix())
            _RE_PROJECT_EXTERNAL_LIBS[i][2] = target_path.as_posix()
    else:
        print("Adding new external lib!")
        _RE_PROJECT_EXTERNAL_LIBS.append([name,base_path,target_path])
    
    _create_project_folders(base_folder_path.as_posix(), [[name, [], target_path.as_posix(), True, True]]) 
            
def is_external_lib( name, base_path, target):    
    for lib in _RE_PROJECT_EXTERNAL_LIBS:
        if lib[0] == name.lower() and lib[1] == base_path.lower():
            return _RE_PROJECT_EXTERNAL_LIBS.index(lib)
    return None

def create_external_lib_folders( ext_libs ):
    for lib in ext_libs:
        add_external_lib_folder(lib[0], lib[1], lib[2])

def asset_exists( assetName ):
    assert(_RE_PROJECT_INITIALIZED)
    asset_root = _RE_PROJECT_ROOT / 'build'     
    asset_folder = asset_root / assetName    
    return asset_folder.exists()

def create_asset_folders( assetName ):
    assert(_RE_PROJECT_INITIALIZED)
    if not _RE_PROJECT_INITIALIZED:
        raise ValueError("Project not initialized")
        return False

    # Add new asset under build. Generates necessary folders and symlinks. 
    assetName = assetName.lower()
    asset_root = _RE_PROJECT_ROOT / 'build'
    asset_folder = asset_root / assetName

    if asset_folder.exists():
        print("Warning: Asset already exists. Generating missing folders")
    else:
        asset_folder.mkdir(parents=True)

    ASSET_FOLDERS = _get_app_folders( "assets", assetName )

    # Any other 3d app work files goes there.  
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

    if _RE_PROJECT_APP_CONFIG.other:
        ASSET_FOLDERS.append(['other', OTHER])
    ASSET_FOLDERS.append(['textures',TEXTURES])
    
    return _create_project_folders(asset_folder.as_posix(), ASSET_FOLDERS, True)

def get_shot_name( sequence, shot_number ):
    assert(_RE_PROJECT_INITIALIZED)
    shot_name = "shot_{}{}".format(str(sequence), str(shot_number).zfill(2))
    shot_name = shot_name.lower()
    return shot_name

def get_shot_path(sequence, shot_number):
    assert(_RE_PROJECT_INITIALIZED)
    shot_path = _RE_PROJECT_ROOT / "shots" 
    shot_path = shot_path / get_shot_name(sequence, shot_number) 
    return shot_path

def get_shot_data_from_name( shot_name ):
    last_part = shot_name[shot_name.rfind('_')+1:]
    shot_num_str = last_part[-2:]
    seq_num_str = last_part[:-2] 
    return (int(seq_num_str),int(shot_num_str))

def shot_exists( sequence, shot_number ):
    assert(_RE_PROJECT_INITIALIZED)
    return get_shot_path(sequence, shot_number).exists()

def create_shot( sequence, shot_number):  
    assert(_RE_PROJECT_INITIALIZED)  
    shot_name = get_shot_name( sequence, shot_number)
    shot_path = get_shot_path(sequence, shot_number)

    if shot_path.exists():
        print("Warning: Shot already exists. Generating missing folders")
    else:
        shot_path.mkdir(parents=True)

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
    
    return _create_project_folders(shot_path.as_posix(), SHOT_FOLDERS, True)
############################################################

def scan_project_assets():
    assert(_RE_PROJECT_INITIALIZED)
    build_root = _RE_PROJECT_ROOT / "build" 

    all_dirs = build_root.iterdir()
    return [x.name for x in all_dirs]    

def scan_project_shots():
    assert(_RE_PROJECT_INITIALIZED)
    shots_root = _RE_PROJECT_ROOT / "shots"     

    all_dirs = shots_root.iterdir()
    shot_dirs = [dir.name for dir in all_dirs if re.match(r"shot_\d{3}d?", dir.name)] 

    return shot_dirs
    
############################################################

def _get_app_folders( category, name ):
    """ Return folder structures for DCC applications based
        on project app config.
        Used in asset and shot structures. 
    """

    HOUDINI = [
        ['geo',[],'temp/{}/{}/geo'.format(category, name)],
        ['hda',[],'assets/3d/hda', _RE_PROJECT_APP_CONFIG.houdini],
        ['fbx',[],'assets/3d/fbx'],
        ['obj',[],'assets/3d/obj'],
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
        ['obj',[],'assets/3d/obj'],
        ['blend',[],'assets/3d/blend', _RE_PROJECT_APP_CONFIG.blender],
        ['usd',[],'assets/3d/usd', _RE_PROJECT_APP_CONFIG.usd],
        ['abc',[],'assets/3d/abc'],
        ['render',[],'render/{}/{}'.format(category, name)],
        ['tmp',[],'temp/{}/{}'.format(category, name)],
        ['lib',[],'assets/lib']
    ]

    C4D = [
        ['tex',[],'assets/tex'],
        ['fbx',[],'assets/3d/fbx'],
        ['obj',[],'assets/3d/obj'],
        ['c4d',[],'assets/3d/c4d', _RE_PROJECT_APP_CONFIG.c4d],
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
        ['obj',[],'assets/3d/obj'],
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

if __name__ != "__main__":
    drop_project()