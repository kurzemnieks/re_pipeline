import os
import subprocess
from pathlib import Path

def run_houdini(houdini_executable, re_root, project_path=None):

    python_path = Path(re_root)
    python_path = python_path / "scripts"
    os.environ['PYTHONPATH'] = python_path.as_posix()

    houdini_path = Path(re_root)
    houdini_path = houdini_path / "tools/houdini/settings"
    os.environ['HOUDINI_PATH'] = houdini_path.as_posix() + ";&"
    
    if project_path is not None:
        os.environ['JOB'] = project_path.as_posix()
        os.environ['RE_PROJECT_ROOT'] = project_path.as_posix()

    os.environ['RE_ROOT'] = str(re_root); #location of RE_Pipeline root

    print("Running houdini: " + houdini_executable.as_posix())
    subprocess.Popen(houdini_executable.as_posix())


