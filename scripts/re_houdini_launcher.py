import os
import subprocess

def run_houdini(houdini_path, re_root, project_path=None):
    os.environ['PYTHONPATH'] = '{0}/scripts'.format(re_root)
    os.environ['HOUDINI_PATH'] = '{0}/tools/houdini/settings;&'.format(re_root)
    
    if project_path is not None:
        os.environ['JOB'] = project_path
        os.environ['RE_PROJECT_ROOT'] = project_path 

    os.environ['RE_ROOT'] = re_root; #location of RE_Pipeline root

    subprocess.Popen(houdini_path)
