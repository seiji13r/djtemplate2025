import sys
import os
from pathlib import Path

cmd_obj = {
    "1": "podman ps -a",
    "build": "podman compose -f compose-dev.yml up -d --build",
    "up": "podman compose -f compose-dev.yml up -d",
    "up2": "podman compose -f compose-dev.yml up",
    "down": "podman compose -f compose-dev.yml down",

    "t-web": "podman exec -it djtemplate2025-webapp-1 /bin/bash",
    "logs-web": "podman logs djtemplate2025-webapp-1",
    "start-web": "podman start djtemplate2025-webapp-1",
}

def show_options(obj):
    for key, cmd in obj.items():
        print("{0:>10} : {1:>8}".format(key, cmd))

def exec_option(obj, option):
    cmd = obj[option]
    print(cmd)
    os.system(cmd)

def build_required_dirs():
    this_path = Path(__file__).parent
    proj_path = this_path.joinpath("webapp")
    if proj_path.exists():
        dev_dirs = [
            "z_static",
            "z_media",
        ]
        for dir_name in dev_dirs:
            new_dir = this_path.joinpath(dir_name)
            new_dir.mkdir(exist_ok=True)
            print(f"Created new dir: {new_dir}")

if __name__ == "__main__":
    build_required_dirs()
    if len(sys.argv) != 2:
        show_options(cmd_obj)
    else:
        option = sys.argv[1]
        exec_option(cmd_obj, option)