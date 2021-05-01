import os
import subprocess
from pathlib import Path

def run_blender(blender_executable, re_root, project_path=None):

    python_path = Path(re_root)
    python_path = python_path / "scripts"
    os.environ['PYTHONPATH'] = python_path.as_posix()
    
    if project_path is not None:
        os.environ['RE_PROJECT_ROOT'] = project_path.as_posix()
        
    os.environ['RE_ROOT'] = str(re_root); #location of RE_Pipeline root

    cmd = blender_executable.as_posix()
    cmd = cmd + " -P " + re_root.as_posix() + "/tools/blender/scripts/blender_start.py"

    subprocess.Popen(cmd)
