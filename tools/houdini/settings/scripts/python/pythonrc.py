import re_project
import os

result = re_project.set_current_root_dir(os.getenv('RE_PROJECT_ROOT'))
#if result:
#    print(re_project.scan_project_assets())