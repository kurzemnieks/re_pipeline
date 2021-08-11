import json
import os
import subprocess
import re
import sys
from collections import namedtuple
from pathlib import Path
from typing import List, Set, Dict, Tuple, Optional


#########################################################################################################

_RE_PROJECT_ROOT : Path = None
_RE_PROJECT_INITIALIZED : bool = False
_RE_PROJECT_CFG_NAME : str = '.projcfg'

_RE_PROJECT_VERSION : float = 1.0
_RE_PROJECT_DEFAULT_FPS : float = 30.0
_RE_PROJECT_DEFAULT_REZ : Dict[str,int] = {'x':1920, 'y':1080}

_RE_PROJECT_NAME_PREFIX : str = ""

ExtLibEntry = Tuple[str, str, str]
_RE_PROJECT_EXTERNAL_LIBS : List[ExtLibEntry] = []

_RE_PROJECT_UNREAL_PROJECT : str = ""

class DccApp(object):
    BLENDER = "blender"
    HOUDINI = "houdini"
    MAYA = "maya"
    C4D = "c4d"

_RE_DCC_APP : str = ''

#########################################################################################################

ProjectFeatures = Dict[str, bool]
_RE_PROJECT_FEATURES : ProjectFeatures = {}

#########################################################################################################
def is_in_houdini() -> bool:
    if os.getenv("HOUDINI_PATH") is not None:
        return True
    return False

def is_in_blender() -> bool:
    if 'blender.exe' in sys.argv[0].lower():
        return True
    return False

def is_in_dcc_app() -> bool:
    return is_in_houdini() or is_in_blender() 
#########################################################################################################

def is_project_initialized() -> bool:
    if not _RE_PROJECT_ROOT:
        return False

    if not _RE_PROJECT_ROOT.exists():
        return False

    return _RE_PROJECT_INITIALIZED

#########################################################################################################
# Get project settings
#########################################################################################################
def set_project_root_folder( path : str ) -> bool:
    # Initialize project root folder. 
    # If project exists in this path, it will be loaded and initialized
    
    global _RE_PROJECT_ROOT
    global _RE_DCC_APP
    global _RE_PROJECT_NAME_PREFIX

    _RE_PROJECT_ROOT = Path(path)

    _RE_PROJECT_NAME_PREFIX = _RE_PROJECT_ROOT.name

    if is_in_houdini():
        _RE_DCC_APP = DccApp.HOUDINI
    if is_in_blender():
        _RE_DCC_APP = DccApp.BLENDER

    #_RE_DCC_APP = DccApp.BLENDER

    if not _try_load_project(_RE_PROJECT_ROOT):
        print('Info: Project not found at location: ' + _RE_PROJECT_ROOT.as_posix())
        return False
    else:
        print('Info: Project found at: ' + _RE_PROJECT_ROOT.as_posix())
        save_project_config()
        return True

def get_project_root() -> Path:
    assert(_RE_PROJECT_INITIALIZED)
    return _RE_PROJECT_ROOT

def get_project_features() -> ProjectFeatures:
    assert(_RE_PROJECT_INITIALIZED)
    return _RE_PROJECT_FEATURES

def get_project_default_rez() -> Dict[str,int]:
    assert(_RE_PROJECT_INITIALIZED)
    return _RE_PROJECT_DEFAULT_REZ

def get_project_default_fps() -> float:
    assert(_RE_PROJECT_INITIALIZED)
    return _RE_PROJECT_DEFAULT_FPS

def get_project_name_prefix() -> str:
    assert(_RE_PROJECT_INITIALIZED)
    return _RE_PROJECT_NAME_PREFIX

def get_project_unreal_project() -> str:
    if len(_RE_PROJECT_UNREAL_PROJECT) > 1:
        return Path(_RE_PROJECT_UNREAL_PROJECT).as_posix()
    else:
        return ""

def get_project_external_libs() -> List[Tuple[str, str, str]]:
    return _RE_PROJECT_EXTERNAL_LIBS

def get_empty_project_features() -> ProjectFeatures:
    app_config : ProjectFeatures = { "blender":False, "houdini":False, "c4d":False, "maya":False, "usd":False, "other":False, "unreal":False, "footage":False }
    return app_config

#########################################################################################################
# Set project settings
#########################################################################################################

def update_project_features_config(project_features : ProjectFeatures, generate_folders : bool = False):
    if not _RE_PROJECT_INITIALIZED:
        raise ValueError("Project not initialized")
        return

    global _RE_PROJECT_FEATURES
    _RE_PROJECT_FEATURES = project_features    

    if generate_folders:
        create_project_folders()

def reset_project_features():
    global _RE_PROJECT_FEATURES
    _RE_PROJECT_FEATURES = get_empty_project_features()

def set_project_default_fps( fps : float):
    assert(_RE_PROJECT_INITIALIZED)
    global _RE_PROJECT_DEFAULT_FPS
    _RE_PROJECT_DEFAULT_FPS = fps

def set_project_name_prefix( name_prefix : str):
    assert(_RE_PROJECT_INITIALIZED)
    global _RE_PROJECT_NAME_PREFIX
    _RE_PROJECT_NAME_PREFIX = name_prefix

def set_project_default_rez( x:int, y:int):
    assert(_RE_PROJECT_INITIALIZED)
    global _RE_PROJECT_DEFAULT_REZ
    _RE_PROJECT_DEFAULT_REZ = {"x":x, "y":y}

def set_project_unreal_project_path( path : str):
    assert(_RE_PROJECT_INITIALIZED)
    global _RE_PROJECT_UNREAL_PROJECT
    unreal_project_path = Path(path)
    if not unreal_project_path.exists():
        print("Trying to set nonexisting Unreal Project path: " + path)
        _RE_PROJECT_UNREAL_PROJECT = ""
        return

    _RE_PROJECT_UNREAL_PROJECT = Path(path).as_posix()
#########################################################################################################
# internals
#########################################################################################################

def _try_load_project( path : Path ) -> bool:
    
    global _RE_PROJECT_EXTERNAL_LIBS
    global _RE_PROJECT_FEATURES
    global _RE_PROJECT_DEFAULT_FPS
    global _RE_PROJECT_DEFAULT_REZ
    global _RE_PROJECT_INITIALIZED
    global _RE_PROJECT_UNREAL_PROJECT
    global _RE_PROJECT_NAME_PREFIX

    if path is None:
        return False

    if not path.exists():
        return False
    
    cfg_file_path = path / _RE_PROJECT_CFG_NAME

    _RE_PROJECT_UNREAL_PROJECT = ""
    
    if cfg_file_path.is_file():
        
        with open(cfg_file_path) as inCfgFile:
            
            project_cfg = json.load(inCfgFile)

            if _RE_PROJECT_VERSION != project_cfg['version']:
                raise ValueError('Project version does not match! Need {}, got {}'.format(_RE_PROJECT_VERSION, project_cfg['version']))
            
            _RE_PROJECT_DEFAULT_FPS = project_cfg['fps']
            _RE_PROJECT_DEFAULT_REZ = project_cfg['rez']

            if 'name_prefix' in project_cfg:
                _RE_PROJECT_NAME_PREFIX = project_cfg['name_prefix']
            
            reset_project_features()

            if 'apps' in project_cfg:
                apps_cfg = project_cfg['apps']
                for key in apps_cfg:                    
                    _RE_PROJECT_FEATURES[key] = apps_cfg[key]

            if 'ext_libs' in project_cfg:
                _RE_PROJECT_EXTERNAL_LIBS = project_cfg['ext_libs']
                create_external_lib_folders(_RE_PROJECT_EXTERNAL_LIBS)        

            if 'unreal_project' in project_cfg:
                _RE_PROJECT_UNREAL_PROJECT = project_cfg['unreal_project']    

            _RE_PROJECT_INITIALIZED = True
        return True

    else:
        return False

TemplateEntry = Tuple[str,List['TemplateEntry'], Optional[str], Optional[bool], Optional[bool]]

def _get_project_folder_struct() -> List[TemplateEntry]:

    """ Return master project folder structure.
    [ folder_name, [list_child_templates], symlink_path, bool_create_this, use_absolute_symlink_path]
    """ 

    #shared assets between shots
    ASSETS = [
        ('2d',[
            ('artworks', []),
            ('references', []),
            ('footage',[],None, _RE_PROJECT_FEATURES["footage"]),
            ('roto',[],None, _RE_PROJECT_FEATURES["footage"]),            
            ]            
        ),
        ('3d',[
            ('fbx',[]),
            ('abc',[]),
            ('obj',[]),
            ('tracking',[],None, _RE_PROJECT_FEATURES["footage"]),
            ('blend',[],None, _RE_PROJECT_FEATURES["blender"]),
            ('hda',[],None, _RE_PROJECT_FEATURES["houdini"]),
            ('c4d',[],None, _RE_PROJECT_FEATURES["c4d"]),
            ('usd',[],None, _RE_PROJECT_FEATURES["usd"]),
            ]
        ),
        ('tex',[]),
        ('lib',[])        
    ]

    #folder where assets are being built
    BUILD = [
    ]

    #shot assembly folder
    SHOTS = [

    ]

    #render outputs (sequences)
    RENDER = [
        ('previs',[]
        ),
        ('shots', []
        )
    ]

    #movies, screenshots, images (valuable and final outputs)
    OUT = [
        ('previs',[]),
        ('review',[]),
        ('images',[]),
        ('deliver',[])
    ]

    #caches, temp sequences - stuff that can be deleted during cleanup/archiving
    TEMP = [
        ('assets',[]),
        ('shots',[])
    ]

    #Combine in one structure
    FOLDERS = [
        ('assets',ASSETS),
        ('build',BUILD),
        ('shots',SHOTS),
        ('render',RENDER),
        ('out',OUT),
        ('temp',TEMP)
    ]

    return FOLDERS

def _get_unreal_project_folder_struct() -> List[TemplateEntry]:
    FOLDERS = [
        ('Content_Source',[
            ('3d',[
                ('fbx',[],'assets/3d/fbx'),
                ('abc',[],'assets/3d/abc'),
                ('hda',[],'assets/3d/hda', _RE_PROJECT_FEATURES["houdini"]),
                ('usd',[],'assets/3d/usd', _RE_PROJECT_FEATURES["usd"])
                ]
            ),
            ('tex',[],'assets/tex')
            ]
        ),        
        ('Render',[],'render/unreal')
    ]

    return FOLDERS

def _list_folder_template_items( template : TemplateEntry, list : List[str], parent:str=None ):
    if list is None:
        return

    enabled = True
    if len(template)>3:
        enabled = template[3]

    folder_name = template[0]    
    if parent is not None:        
        folder_name = parent + "/" + folder_name

    if enabled:
        list.append(folder_name)

    if len(template) > 1 and len(template[1])>0:
        for e in template[1]:
            _list_folder_template_items( e, list, folder_name )
        
def _create_project_folders( base_path_str:str="", template:List[TemplateEntry]=[], create_missing_links:bool=False, update_symlinks:bool=True ) -> bool:    
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
                        #symlink_rel_target = new_folder_path.relative_to( symlink_target ) #this does not work.. use old                        
                        symlink_rel_target = Path(os.path.relpath( symlink_target.as_posix(), new_folder_path.as_posix() ))
                        print(symlink_rel_target.as_posix())

                        if symlink_rel_target.as_posix().startswith("../"):
                            symlink_rel_target = Path(symlink_rel_target.as_posix()[3:])

                    except ValueError as err:
                        symlink_rel_target = symlink_target
                        print(err)

                    #print("Link: " + new_folder_path.as_posix() + " ==> " + symlink_target.as_posix() + " ==> " + symlink_rel_target.as_posix())
                
                if update_symlinks and new_folder_path.is_symlink():

                    #old_symlink_target = Path(os.readlink(str(new_folder_path)))

                    #Python 3.8 changed how some path functions regarding symlinks work.. it's confusing
                    old_symlink_target = Path(os.readlink(new_folder_path.as_posix()))
                    if sys.version_info[1] > 7:
                        old_symlink_target = Path(os.path.realpath(new_folder_path))

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
                            subprocess.check_call('mklink /D "{}" "{}"'.format(folder_name, symlink_rel_target), shell=True, stdout=FNULL)
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
def create_project(app_config : ProjectFeatures) -> bool:
    # Try creating new project at current root location
    # app_config: AppConfig configure which applications will be used in project
    #             Appropriate subfolders will be created. 

    global _RE_PROJECT_FEATURES
    global _RE_PROJECT_INITIALIZED
    _RE_PROJECT_FEATURES = app_config
    
    if not _RE_PROJECT_ROOT.exists():
        _RE_PROJECT_ROOT.mkdir(parents=True)

    if _RE_PROJECT_ROOT.exists():
        save_project_config()
        _RE_PROJECT_INITIALIZED = True
        return True
    else:
        return False

#unitiailize current project
def drop_project():
    global _RE_PROJECT_EXTERNAL_LIBS
    global _RE_PROJECT_FEATURES
    global _RE_PROJECT_DEFAULT_FPS
    global _RE_PROJECT_DEFAULT_REZ
    global _RE_PROJECT_INITIALIZED
    global _RE_PROJECT_VERSION
    global _RE_PROJECT_ROOT
    
    #set defaults
    _RE_PROJECT_ROOT = None
    _RE_PROJECT_INITIALIZED = False
    _RE_PROJECT_VERSION = 1.0
    _RE_PROJECT_EXTERNAL_LIBS = []
    _RE_PROJECT_DEFAULT_FPS = 30.0
    _RE_PROJECT_DEFAULT_REZ = {'x':1920, 'y':1080}
    reset_project_features()

def save_project_config():
    global _RE_PROJECT_FEATURES
    project_cfg = {}
    project_cfg['version'] = _RE_PROJECT_VERSION
    project_cfg['apps'] = _RE_PROJECT_FEATURES #._asdict()
    project_cfg['fps'] = _RE_PROJECT_DEFAULT_FPS
    project_cfg['rez'] = _RE_PROJECT_DEFAULT_REZ
    project_cfg['ext_libs'] = _RE_PROJECT_EXTERNAL_LIBS
    project_cfg['unreal_project'] = _RE_PROJECT_UNREAL_PROJECT
    project_cfg['name_prefix'] = _RE_PROJECT_NAME_PREFIX

    try:
        cfg_file_path = _RE_PROJECT_ROOT / _RE_PROJECT_CFG_NAME
        with open(cfg_file_path, 'w') as outCfgFile:
            json.dump(project_cfg, outCfgFile, indent=4, sort_keys=True)
    except IOError:
        print("RE Pipeline error: Can't write project config file to: " + cfg_file_path.as_posix())

def create_project_folders() -> bool:
    # Create project folder structure based on configuration
    # Use this also to generate new folders if the configuration changes
    return _create_project_folders(_RE_PROJECT_ROOT.as_posix(), _get_project_folder_struct()) and create_unreal_project_folders()

def create_unreal_project_folders() -> bool:
    if _RE_PROJECT_FEATURES["unreal"] is False:
        return True

    unrealProjectPath = Path(_RE_PROJECT_UNREAL_PROJECT)
    if not unrealProjectPath.exists():
        print("Unreal Project folder does not exist: " + _RE_PROJECT_UNREAL_PROJECT)
        return False

    print("Creating unreal project folders!")
    return _create_project_folders( unrealProjectPath.as_posix(), _get_unreal_project_folder_struct(), create_missing_links=True )

def update_all_asset_folders() -> bool:
    all_assets = scan_project_assets()

    for asset_name in all_assets:
        if not create_asset_folders(asset_name):
            return False

    return True    

def update_all_shot_folders() -> bool:
    all_shots = scan_project_shots()

    for shot_name in all_shots:
        shot_id = get_shot_data_from_name(shot_name)
        if not create_shot(shot_id[0], shot_id[1]):
            return False

    return True

def add_external_lib_folder( name : str, base_path : str, target_path : str ) -> bool:
    base_folder_path = _RE_PROJECT_ROOT / base_path    
    target_folder_path = Path(target_path)

    if not target_folder_path.exists():
        raise IOError("Bad project config. External library target path not found: " + target_path)
        return False

    i = is_external_lib(name, base_path, target_path)
    if i is not None:
        if _RE_PROJECT_EXTERNAL_LIBS[i][2] != target_folder_path.as_posix():
            print("REPLACING EXTERNAL LIB: " + _RE_PROJECT_EXTERNAL_LIBS[i][2] + " with: " + target_folder_path.as_posix())
            _RE_PROJECT_EXTERNAL_LIBS[i][2] = target_folder_path.as_posix()
    else:
        print("Adding new external lib!")
        _RE_PROJECT_EXTERNAL_LIBS.append([name,base_path,target_path])
    
    if _create_project_folders(base_folder_path.as_posix(), [(name, [], target_folder_path.as_posix(), True, True)]):
        save_project_config()
        return True
    
    return False
            
def is_external_lib( name : str, base_path : str, target : str) -> int:    
    for lib in _RE_PROJECT_EXTERNAL_LIBS:
        if lib[0] == name.lower() and lib[1] == base_path.lower():
            return _RE_PROJECT_EXTERNAL_LIBS.index(lib)
    return None

def create_external_lib_folders( ext_libs : List[ExtLibEntry] ):
    for lib in ext_libs:
        add_external_lib_folder(lib[0], lib[1], lib[2])
    
def asset_exists( assetName : str ) -> bool:
    assert(_RE_PROJECT_INITIALIZED)
    return get_asset_path(assetName).exists()

def get_asset_path( assetName : str ) -> Path:
    asset_root = _RE_PROJECT_ROOT / 'build'     
    asset_folder = asset_root / assetName
    return asset_folder

def create_asset_folders( assetName : str ) -> bool:
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

    ASSET_FOLDERS = _get_app_folders( "assets", assetName, is_shot=False )

    # Any other 3d app work files goes there.  
    OTHER = [
        ('tex',[],'assets/tex'),
        ('fbx',[],'assets/3d/fbx'),
        ('usd',[],'assets/3d/usd', _RE_PROJECT_FEATURES["usd"]),
        ('abc',[],'assets/3d/abc'),
        ('render',[],'render/assets/' + assetName),
        ('tmp',[],'temp/assets/{}'.format(assetName)),
        ('lib',[],'assets/lib')
    ]

    TEXTURES = [
        ('tex',[],'assets/tex')
    ]

    if _RE_PROJECT_FEATURES["other"]:
        ASSET_FOLDERS.append(('other', OTHER))

    ASSET_FOLDERS.append(('textures',TEXTURES))
        
    return _create_project_folders(asset_folder.as_posix(), ASSET_FOLDERS, True)

def get_shot_name( sequence : int, shot_number : int ) -> str:
    assert(_RE_PROJECT_INITIALIZED)
    shot_name = "shot_{}{}".format(str(sequence), str(shot_number).zfill(2))
    shot_name = shot_name.lower()
    return shot_name

def get_shot_path(sequence : int, shot_number : int) -> Path:
    assert(_RE_PROJECT_INITIALIZED)
    shot_path = _RE_PROJECT_ROOT / "shots" 
    shot_path = shot_path / get_shot_name(sequence, shot_number) 
    return shot_path

def get_shot_data_from_name( shot_name : str ) -> Tuple[int,int]:
    last_part = shot_name[shot_name.rfind('_')+1:]
    shot_num_str = last_part[-2:]
    seq_num_str = last_part[:-2] 
    return (int(seq_num_str),int(shot_num_str))

def shot_exists( sequence : int, shot_number : int ) -> bool:
    assert(_RE_PROJECT_INITIALIZED)
    return get_shot_path(sequence, shot_number).exists()

def create_shot( sequence : int, shot_number : int) -> bool:  
    assert(_RE_PROJECT_INITIALIZED)  
    shot_name = get_shot_name( sequence, shot_number)
    shot_path = get_shot_path(sequence, shot_number)

    if shot_path.exists():
        print("Warning: Shot already exists. Generating missing folders")
    else:
        shot_path.mkdir(parents=True)

    SHOT_FOLDERS = _get_app_folders( "shots", shot_name, is_shot=True )

    COMP = [
        ('previs',[],'render/previs/{}'.format(shot_name)),
        ('render',[],'render/shots/{}'.format(shot_name)),        
        ('out',[],'out'),
        ('artworks',[],'assets/2d/artworks'),
        ('footage',[],'assets/2d/footage/{}'.format(shot_name), _RE_PROJECT_FEATURES["footage"]),
        ('roto',[],'assets/2d/roto/{}'.format(shot_name), _RE_PROJECT_FEATURES["footage"]),
        ('tracking',[],'assets/3d/tracking/{}'.format(shot_name), _RE_PROJECT_FEATURES["footage"])
    ]

    SHOT_FOLDERS.append(('comp', COMP))    
    
    return _create_project_folders(shot_path.as_posix(), SHOT_FOLDERS, True)
############################################################

def scan_project_assets() -> List[str]:
    assert(_RE_PROJECT_INITIALIZED)
    build_root = _RE_PROJECT_ROOT / "build" 

    all_dirs = build_root.iterdir()
    return [x.name for x in all_dirs]    

def scan_project_shots() -> List[str]:
    assert(_RE_PROJECT_INITIALIZED)
    shots_root = _RE_PROJECT_ROOT / "shots"     

    all_dirs = shots_root.iterdir()
    shot_dirs = [dir.name for dir in all_dirs if re.match(r"shot_\d{3}d?", dir.name)] 

    return shot_dirs
    
############################################################

def _get_app_folders( category : str, name : str, is_shot : bool ) -> List[TemplateEntry]:
    """ Return folder structures for DCC applications based
        on project app config.
        Used in asset and shot structures. 
    """

    HOUDINI = [
        ('geo',[],'temp/{}/{}/geo'.format(category, name)),
        ('hda',[],'assets/3d/hda', _RE_PROJECT_FEATURES["houdini"]),
        ('fbx',[],'assets/3d/fbx'),
        ('obj',[],'assets/3d/obj'),
        ('usd',[],'assets/3d/usd', _RE_PROJECT_FEATURES["usd"]),
        ('sim',[],'temp/{}/{}/sim'.format(category, name)),
        ('abc',[],'assets/3d/abc'),
        ('tex',[],'assets/tex'),
        ('tmp',[],'temp/{}/{}'.format(category, name)),

        ('render',[],'render/{}/{}'.format(category, name)),
        ('flip',[],'temp/{}/{}/flip'.format(category, name)),

        ('scripts',[]),
        ('lib',[],'assets/lib'),

        ('footage',[],'assets/2d/footage/{}'.format(name), _RE_PROJECT_FEATURES["footage"] and is_shot),
        ('tracking',[],'assets/3d/tracking/{}'.format(name), _RE_PROJECT_FEATURES["footage"] and is_shot)

    ]

    BLENDER = [
        ('tex',[],'assets/tex'),
        ('fbx',[],'assets/3d/fbx'),
        ('obj',[],'assets/3d/obj'),
        ('blend',[],'assets/3d/blend', _RE_PROJECT_FEATURES["blender"]),
        ('usd',[],'assets/3d/usd', _RE_PROJECT_FEATURES["usd"]),
        ('abc',[],'assets/3d/abc'),
        ('render',[],'render/{}/{}'.format(category, name)),
        ('tmp',[],'temp/{}/{}'.format(category, name)),
        ('lib',[],'assets/lib'),
        ('footage',[],'assets/2d/footage/{}'.format(name), _RE_PROJECT_FEATURES["footage"] and is_shot),
        ('tracking',[],'assets/3d/tracking/{}'.format(name), _RE_PROJECT_FEATURES["footage"] and is_shot)
    ]

    C4D = [
        ('tex',[],'assets/tex'),
        ('fbx',[],'assets/3d/fbx'),
        ('obj',[],'assets/3d/obj'),
        ('c4d',[],'assets/3d/c4d', _RE_PROJECT_FEATURES["c4d"]),
        ('usd',[],'assets/3d/usd', _RE_PROJECT_FEATURES["usd"]),
        ('abc',[],'assets/3d/abc'),
        ('render',[],'render/{}/{}'.format(category, name)),
        ('tmp',[],'temp/{}/{}'.format(category, name)),
        ('lib',[],'assets/lib'),
        ('footage',[],'assets/2d/footage/{}'.format(name), _RE_PROJECT_FEATURES["footage"] and is_shot),
        ('tracking',[],'assets/3d/tracking/{}'.format(name), _RE_PROJECT_FEATURES["footage"] and is_shot)

    ]

    MAYA = [
        ('scenes',[]),
        ('clips',[]),
        ('sourceimages',[],'assets/tex'),
        ('fbx',[],'assets/3d/fbx'),
        ('obj',[],'assets/3d/obj'),
        ('usd',[],'assets/3d/usd', _RE_PROJECT_FEATURES["usd"]),
        ('abc',[],'assets/3d/abc'),
        ('image',[],'render/{}/{}'.format(category, name)),
        ('movies',[],'render/{}/{}/playblast'.format(category, name)),
        ('data',[],'temp/{}/{}'.format(category, name)),
        ('lib',[],'assets/lib'),
        ('tmp',[],'temp/{}/{}'.format(category, name)),
        ('scripts',[]),
        ('footage',[],'assets/2d/footage/{}'.format(name), _RE_PROJECT_FEATURES["footage"] and is_shot),
        ('tracking',[],'assets/3d/tracking/{}'.format(name), _RE_PROJECT_FEATURES["footage"] and is_shot)

    ]

    FOLDERS = [
        ('houdini', HOUDINI, None, _RE_PROJECT_FEATURES["houdini"]),
        ('blender', BLENDER, None, _RE_PROJECT_FEATURES["blender"]),
        ('c4d', C4D, None, _RE_PROJECT_FEATURES["c4d"]),
        ('maya', MAYA, None, _RE_PROJECT_FEATURES["maya"])
    ]

    return FOLDERS

if __name__ != "__main__":
    drop_project()


# Currently active file (asset or shot)
# inside DCC app. Only valid when running from inside DCC app 
# Holds information about current file
class ActiveFile():    
    def __init__(self, name : str, extension : str, path : Path ) -> None:
        self.name = name        
        self.ext = extension
        self.path = path
        self.versions : List[int] = []

    def __init__(self, path:Path) -> None:
        self.path = path
        self.name = self.path.stem
        self.ext = self.path.suffix
        
        #TODO: regex match to asset name or shot name. Try to extract shot number and shot version
        # try to extract asset version

        #m = re.match("\w*_v\d{2}", self.name)
        re_match = re.search("_v\d{2}", self.name)
        if re_match is not None:
            version_str : str = re_match.group()

        if self.path.exists():
            pass
        else:
            pass

        pass

    def scan_versions() -> None:
        pass

    def get_last_version_number() -> int:
        return 0

    def get_published_name() -> str:
        return ""
