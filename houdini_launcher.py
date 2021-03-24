import os
import subprocess

def run_houdini(houdini_path, project_folder, scene_path=None):
    subprocess.Popen(houdini_path)
