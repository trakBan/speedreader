from setuptools import setup
import os
from platform import system as platform

def Setup():
    setup(
        name="speedreader",
        version="0.2",
        scripts=[
            "speedreader",
        ]
    )

if platform() not in ["Linux", "Darwin"]:
    print("The OS you are currently using is not supported!")
    raise SystemExit()

try:
    # Config file ~/.config/speedreader/config.py
    # Creating directory 
    path = f'/home/{os.environ["SUDO_USER"]}/.config/speedreader'

    try:
        os.system(f"mkdir {path}")
    except:
        print("Config file detected!")
        Setup()
        raise SystemExit()

    # Copying the file to {path}
    path = path + "/config.py"
    os.system(f"cp config.py {path}")

    print("\033[0;32mConfig file succesfully moved!\033[0m")

except:
    print("\033[0;31mConfig file unsuccesfully moved!\033[0m")
    print("You will have to mannualy move config.py in ~/.config/speedreader/config.py")
    raise SystemExit()

Setup()